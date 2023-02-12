# encoding=utf-8

"""
unittest集成requests实现接口测试，并通过parameterized实现参数化
author：LBL
date:2023-2-12
"""
import requests
import unittest
from HtmlTestRunner import HTMLTestRunner
from parameterized import parameterized     # 参数化包安装 pip install parameterized

class TPshop(unittest.TestCase):
    def setUp(self) -> None:
        """ 前置方法,用来定义变量 """
        self.session = requests.session()
        # 登录本地项目tpshoup需要两个接口，url_1负载发请求获取验证码图片，url_2负责登录
        self.url_1 = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_2 = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self) -> None:
        """ 后置方法,释放资源 """
        self.session.close()

    def test001_success(self):
        """ 用例1，账户密码验证码都正确访问成功。"""
        response = self.session.get(url=self.url_1)
        # 响应结果为200
        self.assertEqual(200, response.status_code)
        # 响应头中Content-Type属性值包含image
        self.assertIn('image', response.headers.get('Content-Type'))
        data = {
            'username': '13800000000',
            'password': '123456',
            'verify_code': '8888'
        }
        response = None
        response = self.session.post(url=self.url_2, data=data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertEqual('登陆成功', response.json().get("msg"))

    """  a.json文件如下
    [
  {"desc": "登陆成功", "username":"13800000000", "password":"123456","verify_code": "123456","status_code": "1","msg": "登陆成功"
  },
  {"desc": "账户不存在", "username":"13800000001", "password":"123456","verify_code": "123456","status_code": "1","msg": "登陆失败"
  },
  {"desc": "密码错误", "username":"13800000000", "password":"1234567","verify_code": "123456","status_code": "1","msg": "登陆失败"
  }
]
    """
    def build_data(self):
        """ 参数化获取数据列表方法，将a.json文件读取并返回为列表，列表作为参数化修饰符的入参 """
        list1 = []
        with open("a.json", 'r', encoding="utf8") as f:
            json_data = json.load(f)
            for data in json_data:
                desc = data["desc"]
                username = data["username"]
                password = data["password"]
                verify_code = data["verify_code"]
                status_code = data["status_code"]
                msg = data["msg"]
                list1.append((desc, username, password, verify_code, status_code, msg))
        return list1

    @parameterized.expand(build_data())         # 必须用@parameterized.expand()修饰，参数是元组构成的列表
    def test002_success(self, username, password, verify_code, status_code, msg):
        """ 参数化测试用例，导入外部文件作为参数，将变量值都换成参数名 """
        response = self.session.get(url=self.url_1)
        # 响应结果为200
        self.assertEqual(200, response.status_code)
        # 响应头中Content-Type属性值包含image
        self.assertIn('image', response.headers.get('Content-Type'))

        # 访问第二个链接，构造数据
        data = {
            'username': username,
            'password': password,
            'verify_code': verify_code
        }
        # 重置变量
        response = None
        response = self.session.post(url=self.url_2, data=data)
        print(response.json())
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(msg, response.json().get("msg"))



# 程序主入口
if __name__ == "__main__":
    # 指定文件夹，指定文件名，生成测试套件
    suite = unittest.TestLoader().discover(".", "test02_*.py")
    # 执行测试套件，生成测试报告
    with open("result.html","w",encoding="utf-8") as f:
        # 使用HTMLTestRunner创建运行器执行测试套件
        run = HTMLTestRunner(stream=f,report_title="测试报告")
        run.run(suite)




