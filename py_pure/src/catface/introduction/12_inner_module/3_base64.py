# -base64是一种用64个字符来表示任意二进制数据的方法

import base64

encode = base64.b64encode(b'asdfafga-q4r2i3t40i\xb7\x1d\s\jo][];vsai\xb7\x1d\xfb\xef\xff')
print(encode)
decode = base64.b64decode(encode)
print(decode)
encode = base64.b64encode('asdfafga-q4r2i3t40i\xb7\x1d\s\jo][];vsai\xb7\x1d\xfb\xef\xffasd第三方'.encode('utf-8'))
print(encode)
decode = base64.b64decode(encode)
print(decode)

# url safe base64[把字符+和/分别变成-和_]
encode = base64.urlsafe_b64encode(b'asdfafga-q4r2i3t40i\xb7\x1d\s\jo][];vsai\xb7\x1d\xfb\xef\xff')
print(encode)
decode = base64.urlsafe_b64decode(encode)
print(decode)
