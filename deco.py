# coding=utf-8
from time import ctime


def tsfunc(mytime):
    def dec(fn):
        def test():
            print '[%s] %s() called  %s' % (ctime(), fn.__name__, mytime)
        return test
    return dec


@tsfunc('完成')
def show():
    print 'hello'


show()
