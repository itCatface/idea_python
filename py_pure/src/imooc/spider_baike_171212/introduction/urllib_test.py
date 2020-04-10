# encoding=utf-8

from urllib import request
import http.cookiejar

# 读取网页内容
url = 'http://www.baidu.com'

print("方法一:")
response = request.urlopen(url)
print(response.getcode())
print(response.read())
print(len(response.read()))

print("方法二:")
req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response = request.urlopen(req)
print(response.getcode())
print(response.read())
print(len(response.read()))

print("方法三:")
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response = request.urlopen(url)
print(response.getcode())
print(response.read())
print(len(response.read()))
