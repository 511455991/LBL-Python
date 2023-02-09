# encoding=utf-8

"""
文件读写，基础文件txt、二进制文件(图片、音频)
author：LBL
date:2023-2-9
"""


def read_fun():
    """ 写入文件 """
    f = open(r"./a.txt", "a")  # 指定打开方式创建文件对象,r读w写a追加，rb二进制读
    f.write("hello\n")         # 写入数据
    f.write("hello pyth")      # 关闭文件前可多次写入
    f.close()  # 关闭文件


def write_fun():
    """ 读取文件 """
    f = open("./a.txt", "r", encoding="utf-8")
    data = f.read()
    f.close()
    print(data)


if __name__ == "__main__":
    # 普通方式读写文件，需要手动关闭文件，基本不用
    # write_fun()
    # read_fun()

    # 简化方式读写文件，不需要手动关闭文件对象
    with open("a.txt","r") as f:
        # f.read()          # read()方法读取全部剩余文本
        # f.readline()      #readline()方法读取一行，每次调用指针下移一行。到末尾返回""
        # f.readlines()     #readlines()方法读取为列表，每行是一个元素（带换行符）
        while True:
            data = f.readline()
            if data == "":
                break
            print("data")

    # 二进制方式复制文件
    with open("a.txt","rb") as f:
        data = f.read()
    with open("b.txt","wb") as f2:
        f2.write(data)



















