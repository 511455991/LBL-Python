# encoding=utf-8

"""
使用urllib发起请求、获取响应，lxml清洗数据
author：LBL
date:2023-2-10
"""

from urllib import request,parse
from lxml import etree              # 需要安装pip install lxml


def get_html():
    """ 使用urllib.request发送请求获取响应 """
    # 1、请求地址中带有汉字时需要进行url编码，
    url1 = "http://www.baidu.com/S?wd=" + parse.quote("苹果")  # 字符串url编码
    url2 = "http://www.baidu.com/S?" + parse.urlencode({"wd": "苹果"})  # 字典url编码
    print(url1)
    print(url2)

    # 2、发送请求：构造请求头、发送请求、获取响应对象、指定解码方式提取响应内容
    header = {'User-Agent': 'Mozilla/5.0'}
    req = request.Request(url=url1, headers=header)
    response = request.urlopen(req)

    return response


def parse_html(html):
    """ 使用lxml.etree解析html获取百度搜索页面标题 """
    # 创建html解析对象
    parse = etree.HTML(html)
    # 编写xpathh表达式定位元素
    xpath_bds = "//h3/a[1]//text()"
    el_list = parse.xpath(xpath_bds)
    print(el_list)


# 程序主入口
if __name__ == "__main__":
    response = get_html()
    # 打印网页信息，read()获取结果为二进制数据
    html = response.read().decode("utf8")
    print(html)                 # 源码
    print(response.geturl())        # 网址
    print(response.getcode())       # 响应码

    # 4、清洗数据
    parse_html(html)


