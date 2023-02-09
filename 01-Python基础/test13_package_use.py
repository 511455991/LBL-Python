# encoding=utf-8

"""
包、模块的概念
author：LBL
date:2023-2-9
"""

"""python通过pip管理第三方依赖类库，查看版本pip -V
安装卸载包 pip/pip3 install/uninstall 【module_name】
查看已安装的模块 pip list|findstr 【module_name】

模块(module)：一个.py文件就是一个模块.
包(package):是一个特殊的目录，这个目录下必须有__init__.py文件。导包可以将此目录下所有模块一次性导入。原理：__init__.py文件中导入了本包中的模块，
__init__.py内容举例：
from . import a	# 是相对路径，包下的a.py文件
from . import ab
"""

import requests             # 导入第三方模块
import test12_oop_use       # 导入自定义模块


# 程序主入口
if __name__ == "__main__":
    s1 = test12_oop_use.Student("黄忠",23)                # 使用自定义模块中的类
    s1.run()
    print(s1.get_name())

    response = requests.get("http://www.baidu.com")       # 使用第三方模块中的功能



















