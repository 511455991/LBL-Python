# encoding=utf-8

"""
压缩和解压缩zip文件
author：LBL
date:2023-2-10
"""
import os.path
import zipfile


def uncompress_zip(file):
    """ 解压缩指定文件到当前目录 """
    print("正在解压缩文件")
    z = zipfile.ZipFile(file, "r")
    z.extractall()


def zip_file(file):
    """ 压缩单个文件"""
    with zipfile.ZipFile(file + ".zip","w") as z:
        z.write(file)


# 程序主入口
if __name__ == "__main__":
    path = "./testdir/test.zip"
    uncompress_zip(path)
    print("解压完成")





