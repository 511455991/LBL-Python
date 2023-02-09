# encoding=utf-8

"""
异常Exception的处理
author：LBL
date:2023-2-9
"""


def main():
    """ 程序运行出错就会抛出异常给调用者，一层层向外抛，最终导致程序运行终止 """
    # try跟可能出异常的代码，也可主动抛出异常
    try:
        # if...:raise Exception()  在某种情况发生时主动抛出异常，捕获后进行处理
        result = 8/0
        print(result)
    # 捕获异常后的处理,可自定义输出信息或输出异常本身
    except Exception as e:
        print("ZeroDivisionError")
        print(e)
    # 可写可不写
    else:
        print("未匹配到异常，执行正确")
    finally:
        print("出不出异常都会最终执行的代码")


if __name__ == "__main__":
    main()  # 常见异常：除数为零、强制类型转换、下标越界、空指针等













