import os
from aiohttp import web

from subprocess import check_output

app = web.Application()


def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


with open(get_file_path('index.html')) as f:
    index_html = f.read()

with open(get_file_path('shuffled.html')) as f:
    shuffle_html = f.read()

with open(get_file_path('style.css')) as f:
    style_css = f.read()


async def style(request):
    return web.Response(text=style_css, content_type='text/css')


async def shuffle(request):
    shuffle_response = check_output(['mpc', 'shuffle'])
    print(shuffle_response)
    return web.Response(
        text=shuffle_html.format(shuffle_response.decode('utf-8')),
        content_type='text/html')


async def index(request):
    return web.Response(text=index_html, content_type='text/html')


if __name__ == '__main__':
    app.router.add_get('/', index)
    app.router.add_get('/style', style)
    app.router.add_post('/', shuffle)

    web.run_app(app, host='0.0.0.0', port=6681)
