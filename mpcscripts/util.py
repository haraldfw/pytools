def spotify_open_urls_to_file(urls):
    ids = []
    for line in urls:
        ids.append(line.replace('https://open.spotify.com', 'spotify').replace('/', ':').strip())
    return ids
