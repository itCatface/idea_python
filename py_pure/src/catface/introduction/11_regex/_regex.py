# -正则表达式
import re

name = 'catface'
url = 'www.catface.cc'
print(re.match('www', url).span())
print(re.match(name, url))

r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
if r == True:
    print('true')
else:
    print('false')
