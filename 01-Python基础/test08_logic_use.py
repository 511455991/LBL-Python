# encoding=utf-8

"""
逻辑运算，if判断；for、while循环
author：LBL
date:2023-2-8
"""
import random


if __name__ == "__main__":
    # 简单if、if-else、if-elif-else
    n1 = random.randint(0, 100)     # 取随机整数
    if n1 > 10:
        print("%d大于10" % n1)
    elif n1 == 10:
        print(str(n1) + "等于10")
    else:
        print("{}小于10".format(n1))

    # while循环
    i = 0
    while i < 100:          # while True人造死循环
        if i % 2 == 0 and i > 50:
            print(i,end=" ")
        i += 1
    # if条件结合break可以退出循环，注意break只能退出单层循环。if结合continue跳过本次循环
    # 在函数中的话return也能退出循环终止函数，返回函数结果

    # for循环
    for num in range(0,10,2):   # range(start,stop,step)范围函数可生成一个指定范围、步长的数据,负数代表降序
        print(num,end=" ")










