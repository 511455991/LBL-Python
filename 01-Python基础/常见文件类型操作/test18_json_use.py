# encoding=utf-8

"""
json格式文件操作:读取、写入、解析定位
author：LBL
date:2023-2-9
"""
import json         # python使用json工具类操作json文件
import jsonpath     # jsonpath类解析json字符串

def json_use():
    """ json类的使用，把字典与字符串、json文件互相转化"""
    dic_1 = {"name":"张三", "age":20, "addr":["北京", "朝阳区", 333]}
    # 字典默认是单引号存储，不能直接写入文件 {'name': '张三', 'age': 20, 'addr': ['北京', '朝阳区', 333]}
    print(dic_1)

    # 序列化:   将字典转为json字符串
    json_str = json.dumps(dic_1, ensure_ascii=False)    # ensure_ascii=False 代表中文不转义
    print(json_str)

    # 反序列化： 将json字符串转为字典
    dic_2 = json.loads(json_str)
    print(dic_2["addr"][0])         # 获取字典中具体信息

    # dump() 方法可直接将字典序列化为json文件,参数为文件对象
    with open("b.json", "w", encoding="utf-8") as f:
        json.dump(dic_1, f, ensure_ascii=False)

    # load() 方法可反序列json化文件为字典
    with open("b.json", "r", encoding="utf-8") as f:
        dic_3 = json.load(f)
        print(dic_3)


def jsonpath_use():
    """ jsonpath类可快速定位多级字典中的某个键对应的值。返回列表，因为可能定位到多个 """
    # 要安装 pip install jsonpath
    dic = {'dic1':{"1":"张三"},'dic2':{"2":"刘备"}}
    data = jsonpath.jsonpath(dic, "$..2")              # $ 根节点  . 子节点   .. 任意子孙节点
    print(data)

# 程序主入口
if __name__ == "__main__":
    # json概念：JavaScript Object Notation。JavaScript对象表示法。网络接口中传输数据的常见格式。
    # 注意：json文件中键必须用双引号,不能使用单引号。拿到数据后通常转换成字典来获取属性和属性值
    json_use()
    jsonpath_use()

