import socket

## A. 客户端

# 创建一个基于TCP连接的socket
# -p AF_INET --> IPv4协议
# -p SOCK_STREAM --> 面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1. 创建socket对象
s.connect(('www.sina.com.cn', 80))  # 2. 连接到服务器
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  # 3. 像服务器发送请求

# 接收数据
buffer = []
while True:
    d = s.recv(1024)  # 4. 指定一次最多接收的字节数
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()  # 5. 关闭socket

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)

## B. 服务器
import threading, time


def tcplink(sock, addr):
    print('accept new connection from %s:%s...' % addr)
    sock.send(b'hello!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))  # 2. 监听端口
s.listen(5)
print('waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
