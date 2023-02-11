# encoding=utf-8

"""
使用requests.session发起请求、获取响应,使用bs4解析数据
author：LBL
date:2023-2-11
"""
import re

import requests
from bs4 import BeautifulSoup


def get_html():
    """ 使用session访问起点，搜索小说，然后进入小说页面 """

    # 构造请求头
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    proxy = {'http':'127.0.0.1:10809','https':'127.0.0.1:10809'}    # 设置代理参数
    # 实例化session对象，使用session对象发请求
    session = requests.session()
    response = session.get("https://github.com/login",headers=header,proxies=proxy)

    # 使用正则获取登录请求所需参数
    authenticity_tokon = re.search('name="authenticity_token" value="(.*?)" />', response.text).group(1)
    print(authenticity_tokon)

    # 构造登录请求参数字典,这些参数是通过手动登录第二个网址抓包知道的提交的表单数据(必须项，有一些无关项不用填)
    data = {
        'commit': 'Sign in',                        # 固定值
        'authenticity_token': authenticity_tokon,   # 此参数在登陆页面的响应中
        'utf8':'%E2%9C%93',
        'login': input("输入github账户"),
        'password': input("密码")
    }

    # 发送登录请求,post方式数据通过data传递（发送成功就行，不用关注响应，登录成功后cookie会自动存入session）
    session.post('https://github.com/session', headers=header, proxies=proxy, data=data)
    # 访问登录后才能访问的页面
    response = session.get("https://github.com/511455991", headers=header)
    print(response.text)
    print("*"*80)
    # 3、使用session继续发送下一个请求,会自动携带前面的cookie
    session.close()
    return html


def parse_html(html):
    """ BeautifulSoup是python用来解析html源码的库，对结构清晰的网页元素定位比正则更便捷，演示如下，还需修改 """
    # 安装pip install beautifulsoup4

    test_html = '<html><body><div><p class="test p">Hello bs4<span id="test">666</span></p></div>'
    # 指定以lxml解析方式创建解析对象
    soup = BeautifulSoup(test_html,"lxml")
    # 获取p节点下的全部文本，string和text都可以，string是根节点，text是下级任意子节点的文本
    print(soup.p.text)
    # name属性可以获取节点的名称
    print(soup_lxml.p.name)     # p
    # attrs属性可以获取节点的所有属性名和属性值
    print(soup_lxml.p.attrs)    # {'class': ['test', 'p']}
    data['authenticity_token'] = soup.find('input', attrs={'name':'authenticity_token'})['value']
    # bs4也可以通过css选择器按层级来选择到元素
    e_list = soup.select(". . h3 a")
    for e in e_list:
        print(e.string)

# 程序主入口
if __name__ == "__main__":
    """ 多次请求前后有依赖关系的页面时需要手动带上cookie参数，使用session发请求就不用手动添加cookie了 """
    html = get_html()
    # bs4清洗数据
    parse_html(html)


