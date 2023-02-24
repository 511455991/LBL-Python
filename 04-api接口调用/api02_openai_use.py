# encoding=utf-8

"""
openai的chatgpt接口调用
author：LBL
date:2023-2-24
"""
import os
import openai

class chatgpt(object):
    def __init__(self):
        OPENAI_API_KEY = "sk-Q90kG9AoqzRyYf9j5YRRT3BlbkFJuNNICmZHHse1xhXJ9Mz81"
        openai.api_key = os.getenv("OPENAI_API_KEY",OPENAI_API_KEY)


    def text(self):
        """ 使用chatgpt处理文本信息 """
        # 设置要提的问题
        # prompt = "编写一段恐怖故事"
        prompt = "`openai.Completion.create()`函数能接受哪些参数的输入，分别有什么作用"
        # 设置参数，发送请求，获取响应
        response = openai.Completion.create(
            model = "text-davinci-003",     # 设置模型model = "text-davinci-003"是 chatGPT 文本处理模型。
            prompt = prompt,                # 设置提问内容
            temperature = 0.5,              # 设置生成文本的多样性和创意度在0-1
            max_tokens = 2048,              # 设置生成文本的最大长度，最大为2048
            n = 1,                          # 设置要生成的文本数量
            stop = None                     # 设置文本停止条件，当生成文本中包含这些条件之一停止生成。为一个字符串或列表
        )
        # 提取响应内容中文本答案
        print(response.choices[0].text)


# 程序主入口
if __name__ == "__main__":
    """ 
    openai的key需要自己有chatgpt账户然后生成：https://platform.openai.com/account/api-keys
    处理文本模型：
        model = "text-davinci-003"是 chatGPT 最常用的模型之一。
        prompt = "问题"
    处理代码错误信息：
        model="code-davinci-002",处理代码错误信息
        prompt="##### Fix bugs in the below function\n \n### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")\n    \n### Fixed Python",
    chatgpt的其他参数可以通过询问chatgpt获取：`openai.Completion.create()`函数能接受哪些参数的输入，分别有什么作用
     """
    chat = chatgpt()
    chat.text()





