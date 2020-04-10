import os, sys, struct

print(os.getcwd())

# print(os.path)


# 目标目录
dir_des = os.getcwd() + '/decode'
print(dir_des)
if os.path.exists(dir_des):
    pass
else:
    os.mkdir(dir_des)
    pass


def enc(path, key):
    path_ret = ""
    for i in range(0, int(len(path) / 4)):
        # path_ret += struct.pack("<L", struct.unpack("<L", path[i * 4: (i * 4) + 4])[0] ^ key)
        path_ret += struct.pack("<L", struct.unpack("<L", path[i * 4: (i * 4) + 4])[0] ^ key)

    return path_ret


def xor_img(path):
    # 文件对象[可读 | 编码]
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())
        # for line in f.readline():
        #     print(line)


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        print(filepath)
        xor_img(filepath)

# print(enc("daniel King ", 0x0))
# print(enc("daniel King ", 0xFFFFFFFF))
# print(enc(enc("daniel King ", 0xFFFFFFFF), 0xFFFFFFFF))
