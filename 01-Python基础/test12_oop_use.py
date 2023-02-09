# encoding=utf-8

"""
面向对象编程(object oriented programming)的使用和练习
author：LBL
date:2023-2-9
"""

class Student(object):          # 所有类都继承object，super代表父类
    school = "清华大学"          # 类属性，属于类，不单独属于某个对象
    def __init__(self,name,age):
        """ 有参构造器，初始化属性 """
        self.__name = name      # __开头的属性或方法为私有，只能在类中访问
        self.age = age

    def set_name(self,name):
        """ 设置私有属性 """
        self.__name = name

    def get_name(self):
        """ 获取私有属性 """
        return self.__name

    @classmethod        # 类方法第一个参数必须是cls且类方法需要@classmethod修饰
    def study(cls):
        print(cls.school+"里的学生都在学习")

    def run(self):      # 实例方法第一个参数必须是self
        """ 执行程序 """
        self.set_name("马超")


# 程序主入口
if __name__ == "__main__":
    s1 = Student("黄忠",23)       # 实例化对象
    s1.run()
    print(s1.get_name())
    Student.study()



















