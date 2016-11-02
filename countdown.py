# coding: utf-8
__author__ = 'Harald Floor Wilhelmsen'

import sys
from datetime import datetime
from time import strftime, localtime

filepath = '/home/staff/drift/countdownoutput.txt'

s1 = sys.argv[1]
s2 = strftime('%Y.%m.%d %H:%M:%S', localtime())
FMT = '%Y.%m.%d %H:%M:%S'
d1 = datetime.strptime(s1, FMT)
d2 = datetime.strptime(s2, FMT)
tdelta = 0
if d1 > d2:
    tdelta = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
else:
    tdelta = '-' + str(datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT))
print(tdelta)