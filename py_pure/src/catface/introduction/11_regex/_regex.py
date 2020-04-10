### 正则表达式
import re

r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
if r == True:
    print('true')
else:
    print('false')
