# -struct[解决bytes和其他二进制数据类型的转换]
import struct

# pack()将任意数据类型转换成bytes[第一个参数为处理指令I表示4字节无符号整数]
r = struct.pack('>I', 1234567)
print('pack=>', r)

# unpack()将bytes转换相应的数据类型[H表示2字节无符号整数]
r = struct.unpack('>IH', b'\x00\x12\xd6\x87\xfd\x4b')
print('unpack=>', r)
