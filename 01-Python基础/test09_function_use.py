# encoding=utf-8

"""
函数的使用 ,自定义函数、函数递归、匿名函数、函数装饰器
author：LBL
date:2023-2-9
"""
import time

g_num = 10


def fun1(num1,num2=100):
    """ 自定义函数，参数可以设置默认值。函数中变量为局部变量"""
    print(num1,num2)
    global g_num            # 只有先声明全局变量，才能对全局变量进行修改
    g_num =11
    return num1+num2+g_num  # 函数返回值


def re_fu(number):
    """ 递归函数，函数调用自己，必须要有一个明确的结束信号"""
    if number == 1:
        return 1
    else:
        return number * re_fun(number -1)





if __name__ == "__main__":
    # 调用函数,传入参数
    res1 = fun1(22)
    print(res1)

    # lambda匿名函数。能创建一条语句的小型函数
    fun2 = lambda a,b:a+b
    res2 = fun2(2,3)
    print(res2)
    # 简化版lambda表达式
    num = (lambda a, b: a if a > b else b)(3, 6)
    print(num)

    print("-" * 40)
    """ 函数装饰器，也叫语法糖，用来扩充函数功能"""
    def my_decorator(func):
        def inner():
            start_time = time.time()
            func()
            end_time = time.time()
            print("函数执行一共花费了{}的时间".format(end_time - start_time))
        return inner        # 注意返回内容为内部函数，不是执行函数，没()

    @my_decorator
    def sleep_5s():
        time.sleep(5)

    sleep_5s()

















