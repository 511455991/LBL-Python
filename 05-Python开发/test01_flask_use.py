# encoding=utf-8

"""
Flask开发框架基础使用,使用flask框架模拟返回数据，做mock测试
author：LBL
date:2023-2-19
"""

import json
from flask import Flask,jsonify,request     # 1、导包

# 2、创建一个应用对象
app = Flask(__name__)

# 3、定义视图函数，设置路由规则
@app.route("/index")
def index():
    """ 模拟主页，返回字符串 """
    print("访问index主页")
    return "hello mock"

@app.route("/api/sys/login",methods=['POST'])
def login():
    """ 模拟登录页面，接收post请求，判断请求数据，数据正确返回成功，不正确返回失败 """
    result = json.loads(request.get_data().decode("utf-8"))
    mobile = result.get("mobile")
    password = result.get("password")
    print(mobile,password)
    if mobile == "1380" and password == "123456":
        data = {
        "success":True,
        "code": 10000,
        "message":"操作成功！",
        "token": "ajsdfj-12312-szs-fd-dfs"
        }
    else:
        data = {
        "success": False,
        "code": 99999,
        "message": "抱歉，系统繁忙，请稍后重试",
        "token": None
        }
    return data

# 程序主入口
if __name__ == "__main__":
    """" Flask框架作为一个web框架，比django更小，只包含web服务核心功能。想要长期运行一个项目，使用flask框架可随意使用其他技术填充其不包含的功能。
        django框架比较大，功能都已经提供了，想要快速上线某个项目可使用django。
        1、安装：pip install Flask
        2、编写程序并运行
        3、浏览器或postman等工具按规定方式访问http://127.0.0.1:5000 加上路由地址
     """

    # 4、启动web服务器
    app.run()







