# coding=utf-8

from time import ctime, sleep


def tsfunc(func):
    def wrappedfunc():
        print '[%s] %s() called' % (ctime(), func.__name__) #双下划线
        return func
    return wrappedfunc


@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
