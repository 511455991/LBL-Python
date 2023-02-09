# encoding=utf-8

"""
常用模块：sys、os的使用，可操作系统
author：LBL
date:2023-2-9
"""
import os
import sys      # sys可控制python shell窗口，退出sys.exit(0)

if __name__ == "__main__":
    # 获取操作系统类型，nt是Windows，posix是linux、unix或mac
    print(os.name)
    # 打印系统环境变量，全部变量字典、单个变量值
    print(os.environ)
    print(os.environ.get('path'))
    print(os.getcwd())                  # 查看当前工作目录
    print(os.path.abspath("."))         # 查看某目录绝对路径
    print(os.path.relpath("E://","."))  # 查看当前文件至E://的相对路径
    print(os.path.split("/data/code/test.py"))      # 拆分文件和目录('/data/code', 'test.py')
    print(os.path.splitext("/data/code/test.py"))   # 拆分到扩展名('/data/code/test', '.py')
    path = "a.txt"
    """ 路径检查 """
    os.path.exists(path)    # 查看某路径是否存在
    os.path.isabs(path)     # 查看路径是否是绝对路径
    os.path.isdir(path)     # 查看路径是否是文件夹
    os.path.isfile(path)    # 查看路径是否是文件
    """ 路径增删改查 """
    os.mkdir(path)                  # 建立目录
    os.rmdir(path)                  # 删除空目录
    os.remove(path)                 # 删除文件
    os.rename("old.py","new.py")    # 文件重命名
    os.chdir(path)                  # 更改当前工作目录
    os.listdir(".")                 # 获取目录下所有子目录


    # 打开其他程序
    os.startfile("D:\微信\Tencent\QQ\Bin\QQScLauncher.exe")



















