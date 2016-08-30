# coding=utf-8
# this example is to test the re for unicode

import re

CODEC = 'utf-8'

f = open('test.txt', 'r')
bytes_in = f.read()
f.close()

hello_in = bytes_in.decode(CODEC)
hello_list = re.split(u'\s|，|。|', hello_in)
for work in hello_list:
    m = re.match(u'.+大', work)
    if m is not None:
        print m.group()


