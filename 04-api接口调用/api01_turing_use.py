# encoding=utf-8

"""
图灵机器人聊天接口
author：LBL
date:2023-2-14
"""
from urllib.parse import urlencode
import requests


class TuringChatMode(object):
    def __init__(self):
        self.turing_url = 'http://www.tuling123.com/openapi/api?'
        self.key = '82622364a28142878dd8ad634eec401c'

    def run(self, text):
        """ 执行函数 """
        turing_dict = {
            'key': self.key,
            'info': text
        }
        url = self.turing_url + urlencode(turing_dict)
        print(url)
        # 发送数据，获取机器人响应
        response = requests.get(url=url).json()
        print("机器人说：" + response['text'])


# 程序主入口
if __name__ == "__main__":
    spider = TuringChatMode()
    text = input("你说：")
    spider.run(text)





