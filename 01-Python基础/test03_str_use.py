# encoding=utf-8

"""
字符串类型数据使用
author：LBL
date:2023-2-8
"""

if __name__ == "__main__":
    # 定义字符串,使用”“或‘’
    s1 = "    这是测试用的字符串：ab,cd,ef,gh    "

    # 字符串编码、解码
    s1_encode = s1.encode("utf-8")
    s1_decode = s1_encode.decode("utf-8")

    # 格式化字符串:方式一%  方式二.format  方式三+拼接  方式四*乘
    print("%s %d + %.2f的值" % ("计算", 10, 12.0))
    print("{}的{}成绩是{}".format("张三", "数学", 99))
    print("张三的数学成绩是" + str(99))
    print("a"*10)

    # 获取字符串长度
    s1_len = len(s1)
    # 根据下标取对应位置字符
    char_0 = s1[0]
    # 查找字符下标索引，返回首次出现位置，未找到返回-1
    a_index = s1.find("a")
    # 统计子字符串出现次数
    a_num = s1.count("ab")
    # 替换查找到的所有字符串
    s2 = s1.replace(","," ")
    # 拆分字符串,不指定字符时按空白字符拆分
    s1_list = s1.split(",")
    # 字符串切片[开始索引：结束索引：步长]  包含开始不包含结尾,步长省略则默认为1
    s2 = s1[::-1]       # 逆序
    s2 = s1[2:6]        # 截取子字符串
    s2 = s1[::2]        # 步长为2，隔一个字符取一个
    s2 = s1[4:]         # 取到最后
    print(s2)
    # 去除字符串左右空格
    s2 = s1.strip()
    s2 = s1.lstrip()
    s2 = s1.rstrip()
    # 字符串大小写转换
    s2 = s1.upper()
    s2 = s1.lower()
    s2 = s1.swapcase()      # 反转
    # 判断字符串内容
    s1.isalpha()            # 是否全是文字
    s1.isdigit()            # 是否全是数字
    s1.islower()            # 是否字母全是小写
    s1.isupper()            # 是否字母全是大写



