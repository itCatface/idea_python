# -hashlib[提供常用摘要算法MD5、SHA1等]
import hashlib

md5 = hashlib.md5()
# update可分多次调用结果一样
md5.update('catface7'.encode('utf-8'))
md5.update('wang ye han'.encode('utf-8'))
print('md5=>', md5.hexdigest())

sha1 = hashlib.sha1()
# update可分多次调用结果一样
sha1.update('catface7'.encode('utf-8'))
sha1.update('wang ye han'.encode('utf-8'))
print('sha1=>', sha1.hexdigest())
