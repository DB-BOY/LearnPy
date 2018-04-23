# -*- coding: utf-8 -*-
import os

'操作文件&目录'

# 系统名字
# 如果是posix，说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统。
print(os.name)
print('windows 不提供uname()')
uname = os.uname()
print(uname)

print('环境变量 environ')
ev = os.environ
print(ev)

# 具体key 值获取

print(' 具体key 值获取: os.environ.get(key)')
path = ev.get("PYTHONPATH")
print(path)

defaut = os.environ.get('x', 'default')
print(defaut)

# 操作目录
print('操作目录')

abspath = os.path.abspath('.')
print(abspath)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 拼接目录名,使用join,统一路径分隔符
newPath = os.path.join(os.path.abspath('.'), 'new')
print(newPath)

# 创建新目录
os.mkdir(newPath)
# 删除目录
os.rmdir(newPath)

# 拆分路径
print(' 拆分路径')
splitpath = os.path.split('/Users/pro/Python/LearnPy/src/base/base.py')
print(splitpath)

splitpath = os.path.splitext('/Users/pro/Python/LearnPy/src/io/test.txt')
print(splitpath)
splitpath = os.path.splitext('/Users/pro/Python/LearnPy/src/base/base.py')
print(splitpath)

# 重命名
# os.rename('/Users/pro/Python/LearnPy/src/io/test.txt','/Users/pro/Python/LearnPy/src/io/test.txt')

# os.remove('test.txt')


#
# 当前目录下所有目录
print(' 当前目录下所有目录')
dir = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dir)

# 当前目录下所有py文件
print(' 当前目录下所有py文件')
py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(py)
