import gevent

def foo():
    print('Running in foo')

f = gevent.spawn(foo)