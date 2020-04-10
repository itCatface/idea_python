# -hmac[加盐算哈希值，注意msg和key均为bytes类型]
import hmac

msg = b'hello world!'
key = b'salt'
h = hmac.new(key, msg, digestmod='MD5')
r = h.hexdigest()
print('r=>', r)
