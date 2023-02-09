# encoding=utf-8

"""
正则表达式的使用，查找数据、清洗数据
author：LBL
date:2023-2-9
"""
import re

def fun():
    pass

# 程序主入口
if __name__ == "__main__":
    # \d 匹配一个数字
    # \w 匹配数字一个数字或者字母
    # \s 表示一个空白字符，即空格与tab
    # * 星号可以表示任意字符（0个或者0个以上）
    # + 加号表示至少一个字符
    # ? 问号表示0个或者1个字符
    # {n} 前一个字符重复n次    {n,}前一个字符最少重复n次
    # {n,m} 前一个字符重复n到m次
    # [] 表示范围，例如[1,9]表示数字1至9
    # | 竖线表示或，例如 1|2 表示匹配到1或者2都成立
    # ^ 表示正则表达式匹配的开头，例如 ^python 表示这个字符串必须以python作为开始
    # $ 表示正则表达式的结束，例如 python$ 表示这个字符串必须以python作为结束
    # [^abc] 只能是a、b、c之外的任意字符。^托字符，在[]内代表取反
    # \ 特殊字符串，使用反斜线\进行转义
    # r 不考虑转义，需要使用r开始的前缀，例如 r'010-10010010'的-就不用转义了
    # 匹配模式：正则默认为贪婪模式，贪婪模式是匹配最多的符合要求的内容，爬虫清洗数据更适合非贪婪模式，量词后加？

    msg = "测试字符串111-123，第二个字符串222-123 第三个333-123"
    re_bds1 = r"\d{3}-123"            # 设置正则匹配规则

    """match()方法，只会从开头进行匹配，匹配到返回match对象，没匹配到返回None。匹配到结果需要group()才能查看"""
    result = re.match(re_bds1, msg)
    if result:
        print(result.group())
    else:
        print("match没有匹配到")

    """ search()方法,类似match，不同的是会全文匹配 """
    result = re.search(re_bds1, msg)
    print(result.group())

    """ findall()方法，会返回所有匹配到的内容列表"""
    result_list = re.findall(re_bds1, msg)
    print(result_list)

    """ sub()方法，替换匹配到的字符串 """
    new_str = "号码"
    result = re.sub(re_bds1, new_str, msg)      # 参数：正则规则、新字符串、旧字符串
    print(result)

    """ split()方法，按指定内容分割字符串，返回列表"""
    re_bds2 = r"\s|，"
    result = re.split(re_bds2, msg)  # 按空格或逗号分割字符串为列表
    print(result)

    """  爬虫清洗数据，由于爬虫内容前后html页面标签比较一致，可以直接加上前后内容再根据正则分组(.*?)获取其中需要部分 """
    html_response = "要筛选的字符串111-123，第二个字符串222-123， 第三个333-123"
    re_bds1 = '字符串(.*?)，'  # 量词后加?为非贪婪模式
    re_bds2 = '字符串(.*?)-(.*?)，'
    # re.S 是为了让.可以匹配任意字符包括换行等，html代码一般很长还包含换行
    # 当分组只有一个时，匹配到的结果为：元素为字符串的列表
    ip_list_1 = re.findall(re_bds1, html_response, re.S)    # ['111-123', '222-123']
    # 当分组有多个时，匹配到的结果为：元素为元组的列表
    pattern = re.compile(re_bds2, re.S)
    ip_list_2 = pattern.findall(html_response)              # [('111', '123'), ('222', '123')]
    print(ip_list_1)
    print(ip_list_2)
