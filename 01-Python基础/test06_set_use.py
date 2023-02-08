# encoding=utf-8

"""
集合类型数据使用,
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 定义一个集合。列表是有序的，set集合成员是无序不重复的。set使用场景不多，可用来去重
    my_set1 = set()              # 定义空集合需要用set()
    my_set = {"刘备","关羽","张飞"}
    # 增加元素
    my_set.add("吕布")
    # 删除元素，无序不能用索引
    my_set.remove("吕布")         # 指定删除元素
    my_set.pop()                 # 删除最后一个元素
    my_set.clear()               # 清空集合

    # 给列表、字符串等去重
    list1 = [1,1,2,3,4,4]
    max_num = max(set(list1))
    print(max_num)

    s1 = "abcdab12"
    print(set(s1))      # {'a', 'c', '1', '2', 'd', 'b'} 无序不重复
    s2 = "1234"
    print(set(s1) & set(s2))    # {'1', '2'}  &交集，|并集，-减去，^不重复







