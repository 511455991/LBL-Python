# encoding=utf-8

"""
unittest单元测试模块的使用,HtmlTestRunner生成测试报告
author：LBL
date:2023-2-12
"""
import unittest                                 # 单元测试包

import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner       # 测试报告包

def my_sum(a,b):
    """被测试方法"""
    return a+b


class MyTest(unittest.TestCase):
    """ 测试类，必须继承自unittest.TestCase """
    # 测试用例执行顺序是以名称ascii排序执行顺序0-9，A-Z,a-z
    def test_001(self):
        print(my_sum(3,4))

    def test_002(self):
        re = my_sum(3,4)
        # 断言实际结果与预期结果相等
        self.assertEqual(re,7,msg="断言3+4=7")
    """ 常见断言
        【Equal NotEqual】相等、不等
        【In NotIn】在、不在范围内
        【None NotNone】空、非空
        【True False】真假
        msg参数可写可不写"""
# 执行方式一：直接执行
if __name__ == "__main__":
    # unittest.main()可以将一个单元测试的模块变为可以执行的脚本
    # unittest中testloader类来搜索以test开头的测试用例，并自动执行
    # 项目一但导入unittest，pycharm会自动将普通run运行模式换为 run unittest模式来执行用例，但有时不会加载出来，
    # 打开右上角文件配置，可以看到有python和python test两个路径选项，挂在哪个下面就是哪个运行的
    print("方式一：直接执行")
    unittest.main()


# 执行方式二
if __name__ == "__main__":
    print("方式二：创建测试套件，手动添加测试用例，按添加顺序执行")
    # 构造一个测试套件(suite容器)，来存放测试用例
    suite = unittest.TestSuite()
    # 添加类中的测试用例，分单个添加和多个添加
    suite.addTest(MyTest("test_001"))
    suite.addTest(MyTest("test_002"))
    suite.addTests([MyTest("test_001"),MyTest("test_002")])
    # 创建运行器
    run = unittest.TextTestRunner()
    # 调用运行器的run方法执行测试套件suite
    run.run(suite)


# 执行方式三
if __name__ == "__main__":
    print("方式三：创建测试套件，指定文件自动添加用例，执行用例")
    # 指定文件夹，指定文件名，可用通配符匹配多个测试用例文件
    suite = unittest.TestLoader().discover(".","test01_*.py")
    # 创建运行器执行测试套件
    run = unittest.TextTestRunner()
    run.run(suite)

# 执行方式四，HtmlTestRunner生成测试报告
if __name__ == "__main__":
    print("方式三：创建测试套件，指定文件自动添加用例，执行用例")
    # 指定文件夹，指定文件名，可用通配符匹配多个测试用例文件
    suite = unittest.TestLoader().discover(".", "test01_*.py")

    # 生成测试报告，测试报告使用TextTestRunner第三方模块，需要额外安装pip install html-testRunner
    # 测试报告中文乱码原因：生成报告时不是utf-8编码，html文件在浏览器默认utf-8解码。解决方法：进入HTMLTestRunner源码文件result.py中，将三处open文件后添加encoding="utf-8"参数
    with open("result.html","w",encoding="utf-8") as f:
        # 使用HTMLTestRunner创建运行器执行测试套件
        run = HTMLTestRunner(stream=f,report_title="测试报告")
        run.run(suite)




