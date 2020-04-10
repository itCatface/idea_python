# -contextlib[只要正确实现上下文管理的对象就可以用于with语句]
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('enter...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error...')
        else:
            print('end...')

    def query(self):
        print('query info about:', self.name)


with Query('catface') as q:
    q.query()

# 使用@contextmanager简化上述操作[让我们通过编写generator简化上下文管理]
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about:', self.name)


@contextmanager
def create_query(name):
    print('enter...')
    q = Query(name)
    yield q
    print('end...')


with create_query('catface') as q:
    q.query()


# 在某段代码执行前后加特定代码
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)


with tag('h1'):
    print('hello')
    print('world')

# -@closing[没有实现上下文的对象不用用于with语句，可以用cloding将对象变为上下文对象]
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的简单的generator
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
