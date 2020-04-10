# 实现web应用程序的wsgi处理函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hello, web</h1>']
