"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/3 10:39"
"""
import os
import shutil


# 重命名操作
def func_os_rename():
    # 重命名文件
    os.rename('sample/test_rename.txt', 'sample/test_rename1.txt')
    # 重命名目录
    os.rename('sample', 'sample1')


# 重命名操作： 树状结构
def func_os_renames():
    os.renames('sample1/test_rename1.txt', 'sample/test_rename.txt')


# 删除文件
def func_os_remove():
    # 删除文件，如果文件不存在则报错
    os.remove('sample/test_rename.txt')


# 删除目录
def func_os_rmdir():
    # 1.不能递归删除目录
    # 2.如果文件夹非空，则报错
    os.rmdir('sample')


def func_os_removedirs():
    # 1.可以递归删除目录（删除路径上所有空文件夹）
    # 2.如果文件夹非空，则报错
    os.removedirs('sample')


def func_shutil_rmtree():
    shutil.rmtree('sample')


# 创建目录
def func_os_mkdir():
    # 不支持多级目录创建
    os.mkdir('sample')


def func_os_makedirs():
    os.makedirs('sample/test', exist_ok=True)


# 获取当前目录
def func_os_getcwd():
    print(os.getcwd())


# 文件复制操作
def func_file_copy1():
    shutil.copyfile('sample/test_rename.txt', 'sample/test_rename1.txt')


def func_file_copy2():
    shutil.copy('sample/test_rename.txt', 'sample/test_rename1.txt')


def func_file_copy3():
    src = open('sample/test_rename.txt', 'rb')
    target = open('sample/test_rename1.txt', 'wb')
    shutil.copyfileobj(src, target)
    src.close()
    target.close()


def func_file_copy4():
    shutil.copy2('sample/test_rename.txt', 'sample/test_rename1.txt')


if __name__ == '__main__':
    func_file_copy4()

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/3 10:39"
"""
