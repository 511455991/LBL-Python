# encoding=utf-8

"""
使用urllib发起请求、获取响应
author：LBL
date:2023-2-10
"""

from urllib import request,parse


# 程序主入口
if __name__ == "__main__":
    # 1、请求地址中带有汉字时需要进行url编码，
    url1 = "http://www.baidu.com/S?wd=" + parse.quote("苹果")             # 字符串url编码
    url2 = "http://www.baidu.com/S?"+parse.urlencode({"wd": "苹果"})      # 字典url编码
    print(url1)
    print(url2)

    # 2、发送请求：构造请求头、发送请求、获取响应对象、指定解码方式提取响应内容
    header = {'User-Agent': 'Mozilla/5.0'}
    req = request.Request(url=url1, headers=header)
    response = request.urlopen(req)
    # 打印网页源码，read()获取结果为二进制数据
    html = response.read().decode("utf8")
    print(html)
    # 打印网页网址
    print(response.geturl())
    # 打印网页响应码
    print(response.getcode())

    # 4、清洗数据


