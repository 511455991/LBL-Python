# encoding=utf-8

"""
数学运算,基本数学运算、随机、math模块
author：LBL
date:2023-2-9
"""

import math


# 程序主入口
import random

if __name__ == "__main__":
    # 基本数学运算
    num1 = 5; num2 = 2
    res = num1 + num2
    res = num1 - num2
    res = num1 * num2
    res = num1 / num2
    res = num1 // num2      # 整除
    res = num1 % num2       # 取余
    res = num1 ** num2      # 幂（次方）
    res += 1                # res = res + 1
    print(res)

    print(abs(-10.2))         # 取绝对值
    print(max(1,2,3))         # 取最大值
    print(min(1,2,3))         # 取最小值

    # 转换进制
    print(bin(res))         # 0b11010   二进制
    print(oct(res))         # 0o32      八进制
    print(hex(res))         # 0x1a      十六进制
    print(format(res,"b"))  # 11010     使用format打印二进制去前缀字符
    print(format(res,"o"))  # 32        使用format打印八进制去前缀字符
    print(format(res,"x"))  # 1a        使用format打印十六进制去前缀字符

    # 生成随机数
    n0 = random.random()             # 在[0.0, 1.0)范围生成随机小数
    n1 = random.randint(10,12)       # 在[10，12]范围生成随机整数
    n3 = random.choice([0,1,2,"a"])  # 在指定序列中随机获取一个元素，参数可字符串、列表、元组
    random.choice(range(10))
    l1 = [0,1,2,"a"]                 # 打乱列表顺序，重新排列
    random.shuffle(l1)
    print(l1)

    # map函数可以接收一个函数作为第一个参数，后面参数为可迭代列表，传递给前面的函数，类似for循环
    # 使用map()函数计算1-9的平方结果
    square_list = map(a, range(1, 10))
    print(list(square_list))         # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    # math模块

















