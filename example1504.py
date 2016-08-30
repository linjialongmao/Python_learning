# coding=utf-8

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime
import re

f = open('test1504.txt', 'w')
doms = ('com', 'edu', 'net', 'org', 'gov')
for i in range(randint(5, 10)):
    dtint = randint(0, maxint-1)
    dtstr = ctime(dtint)
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)
    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)
    f.write('%s::%s@%s.%s::%d-%d-%d\n'% (dtstr, em, dn, choice(doms), dtint, shorter, longer))
f.close()

f = open('test1504.txt', 'r')
strlist = []
for fileline in f:
    strlist.append((re.match(r'.+?(\d+-\d+-\d)', fileline)).group(1))
f.close()
print strlist, len(strlist)