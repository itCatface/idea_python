# -操作文件和目录
import os

print(os.name)

print(os.environ)

print(os.environ.get('PATH'))

print(os.path.abspath('.'))

dir = os.path.join('../../introduction_dir', 'tt')
print(dir)

# os.mkdir(dir)
# os.rmdir(dir)

dir = os.path.split('/Users/michael/testdir/file.txt')
print(dir)

dir = os.path.splitext('/path/to/file.txt')
print(dir)

# os.rename('../../newDir/girl_copy1.jpg', '../../newDir/girl_copy.jpg')
# remove 删除文件

l = [x for x in os.listdir('.') if os.path.isfile(x)]
print(l)

l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l)

l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[0].__contains__('d')]
print(l)
