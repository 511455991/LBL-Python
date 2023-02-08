# encoding=utf-8

"""
列表类型数据使用
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 定义列表
    test_list = []
    man_list = ["关羽","刘备","0曹操"]
    # 获取列表长度
    print(len(man_list))
    # 根据下标访问列表元素，-1代表倒数第一个
    print(man_list[0])
    # 增加元素
    man_list.append("吕布")       # 末尾追加
    man_list.insert(1,"张飞")     # 指定索引插入
    test_list.extend(man_list)   # 追加另一个列表所有数据
    # 删除元素
    test_list.pop()          # 删除末尾元素
    test_list.pop(0)         # 指定索引删除元素
    test_list.remove("张飞")  # 指定值删除元素，删除第一次出现的
    test_list.clear()        # 清空列表
    del(man_list[0])        # del方法也可指定索引删除
    # 修改元素
    man_list[2] = "董卓"
    # 查
    num = man_list.count("张飞")          # 统计出现次数
    index1 = man_list.index("张飞")       # 查找元素下标，不存在会报错
    index2 = man_list.index("张飞",0)     # 查找元素第几次出现的下标
    print(max(man_list))                 # 获取最大元素，排序方式是对象中的
    print(min(man_list))                 # 获取最大元素，排序方式是对象中的
    print("张飞" in man_list)             # in\not in判断是否在
    # 排序
    man_list.sort()             # 升序
    man_list.sort(reverse=True) # 降序
    man_list.reverse()          # 逆序，反转
    # 去重:转集合去重
    mans = set(man_list)

    # 遍历列表元素
    for man in man_list:
        print(man,end=" ")



