# encoding=utf-8

"""
字典dict类型数据使用
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 定义一个字典。字典存储键值对，key:value
    my_dict1 = {}
    my_dict = {"name":"刘备","age":23,"sex":"男"}

    # 获取指定key的值。
    print(my_dict["name"])
    print(my_dict.get("name"))  # get()方法是[]获取键对应值的升级版，键不存在时不会报错
    print(my_dict.keys())       # 获取所有键、值
    print(my_dict.values())

    # 增加、修改值。键存在为修改，不存在为增加
    my_dict["price"] = "8888"
    my_dict.update({"name":"张三","price":"9999"})

    # 删除某键值对，会返回value,可指定不存在时返回什么
    my_dict.pop("name")
    my_dict.pop("name","指定内容")
    # 清空字典
    my_dict1.clear()

    # 使用copy()复制一个字典
    copy_dict = my_dict.copy()

    """ 遍历字典的两种方法 """
    for k in dic1:  # 方式一： 普通for循环，取key
        print(k, dic1[k])

    for k in dic1.items():  # 方式二：items方法，获取每一个（key,value）组成的元组
        print(k)  # ('name', '刘备')。。。。
    for k, v in dic1.items():  # iteam()获取的元组可用拆包简化获取其内容
        print(k, v)

    # 使用dict()创建字典,dict()可以接收很多类型的对象
    # 可迭代对象作为参数
    tuple_math = ("math",99)
    tuple_english = ("english",89)
    dict_a = dict([tuple_math,tuple_english])
    print(dict_a)
    # 使用zip()合并两个列表分别作为字典的key和value
    list_key = ["math","chinese"]
    list_value = [78,89]
    dict_b = dict(zip(list_key,list_value))
    print(dict_b)









