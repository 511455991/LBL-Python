# encoding=utf-8

"""
使用requests发起请求、获取响应
author：LBL
date:2023-2-10
"""

import requests                     # 安装 pip install requests


def get_html():
    """ 使用urllib.request发送请求保存图片到本地 """
    url = "https://images2018.cnblogs.com/blog/1007017/201806/1007017-20180608105004994-1976825557.png"
    header = {'User-Agent':'Mozilla/5.0'}
    proxy = {'http': '127.0.0.1:10809', 'https': '127.0.0.1:10809'}
    # proxies=proxy请求参数可设置代理
    # verify=False请求参数可关闭ca证书验证（关闭提示不安全网站）
    # timeout=10 请求参数可设置等待超时时间

    # 1、请求地址中带有汉字时需要进行url编码，
    response = requests.get(url=url,headers=header)
    return response


def save_png(response):
    """ 保存图片到本地 """
    with open("a.png", "wb") as f:
        f.write(response.content)


# 程序主入口
if __name__ == "__main__":
    # 电脑开启代理软件情况下requests会报错失败。urllib正常使用。代理会将整个系统的流量指向电脑某个端口，由代理软件在中间进行转发，
    # 想使用requests需要在请求中设置代理梯子的端口(通常为10809)，可以将python脚本请求转向该端口

    # 获取响应对象,解析响应内容
    response = get_html()
    # content为byte类型,指定解码方式,text是程序猜测的解码方式结果
    # print(response.content.decode("utf-8"))
    # print(response.text)
    # 保存图片到本地
    save_png(response)



