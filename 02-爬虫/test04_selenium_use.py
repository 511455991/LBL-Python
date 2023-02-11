# encoding=utf-8

"""
使用selenium发起请求、操作页面元素，获取元素信息。操作单个元素常用id，name,xpath。爬虫清洗一批类似元素常用xpath，css
author：LBL
date:2023-2-11
"""
from selenium import webdriver                      # 浏览器驱动
from selenium.webdriver.common.by import By         # 定位元素
from selenium.webdriver.common.keys import Keys     # 操作键盘
from selenium.webdriver import ActionChains         # 操作鼠标
import time


# 程序主入口
if __name__ == "__main__":
    # Selenuim 中文直译是硒，是用来做web网页自动化测试的。也可用来爬虫，所见即所得
    # 安装: pip install selenium==3.141.0

    # 选择浏览器驱动，还支持Firefox以及IE等 webdriver.Chrome()
    driver = webdriver.Edge()
    # 最大化浏览器
    driver.maximize_window()
    # 打开百度网址
    driver.get("http://www.baidu.com")
    # 打印标题
    print(driver.title)
    # 确认标题是否包含“百度一下”一词，通常用此来判断在哪个页面
    assert "百度一下" in driver.title

    # 查找搜索框的元素
    q_element = driver.find_element(By.ID,'kw')     # 注意大写BY.ID
    # 向找到的元素输入信息
    q_element.send_keys('hello world')
    # 输入键盘操作,功能键或组合键
    q_element.send_keys(Keys.ENTER)         # 回车
    time.sleep(1)
    q_element.send_keys(Keys.CONTROL, 'a')  # 全选，相当于CTRL+A
    q_element.send_keys(Keys.BACK_SPACE)    # 删除键
    q_element.send_keys("apple")
    # 使用元素点击方法
    driver.find_element(By.ID,"su").click()
    time.sleep(1)
    # 页面操作
    driver.back()         # 页面后退
    # driver.forward()    # 页面前进
    # driver.refresh()    # 刷新

    # 鼠标操作，移动鼠标进行设置。本质是执行js脚本
    # 1、实例化鼠标对象
    driver.get("http://www.baidu.com")  # 重新访问百度首页
    time.sleep(1)
    action = ActionChains(driver)
    # 2、用鼠标对象的方法操作元素，移动到元素上、点击、双击、右击、拖动
    action.move_to_element(driver.find_element(By.ID,"s-usersetting-top"))
    # 3、提交鼠标操作
    action.perform()

    # 打开注册百度新页面,再切回原页面
    time.sleep(1)
    action.click(driver.find_element(By.ID,"s-top-loginbtn"))
    action.perform()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__regLink"]').click()
    win_list = driver.window_handles        # 获取窗口句柄（返回列表）
    driver.switch_to.window(win_list[0])    # 通过窗口句柄下标切换标签页
    """ 滚动条 """
    # script = "window.scrollBy(0,1000)"    # js脚本，从当前位置向下滚动1000像素
    # script1 = "window.scrollTo(0,1000)"  # js脚本，向下滚动到0，1000位置
    # driver.execute_script(script)         # webdriver执行js脚本

    """ 弹窗操作 """
    # alert = driver.switch_to_alert切换到弹窗
    # alert.accept()
    # alert.dismiss()
    # print(alert.text)

    """ cookie操作 """
    # 添加cookie
    # cookie_dick = {
    # "name":"test_baidu",
    # "value":"test_value"
    # }
    # driver.add_cookie(cookie_dick)
    # 查看cookie
    # print(driver.get_cookies())
    # driver.get_cookie("name")



'''
    # 登录qq空间,子页面操作
    driver.get("https://qzone.qq.com/")  # 进入qq空间登录主页面
    # 定位到子页面iframe元素，然后切换窗口句柄到子页面。
    # 有些页面的frame子页面的id是随时变化的如时间戳，所以用xpath定位更好
    el_frame = driver.find_element(By.XPATH, '//*[@id="login_frame"]')
    driver.switch_to.frame(el_frame)
    # 操作子页面元素
    driver.find_element(By.ID, "switcher_plogin").click()  # 从扫码页面跳转到输入账户页面
    driver.find_element(By.ID, "u").send_keys("123456")
    driver.find_element(By.ID, "p").send_keys("123456")
    driver.find_element(By.ID, "login_button").click()  # 点击登录按钮（后面会有验证码）
    # 退出浏览器驱动，释放资源。driver.close()是关闭当前页面
    # driver.quit()
'''

"""  
    # 百度页面，使用cookie实现跳过登录
    driver.get("http://www.baidu.com")

    # 将手动获取到的cookie：BDUSS 添加到网页中，再刷新页面
    cookie = {
        "name":"BDUSS",
        "value":"kpQa32tqWkV-N0duUlI2Z3JaOUdVUm8wS2ZJWnpmc3YzdUlIWHR6eHpMVGVtR0poSVFBQUFBJCQAAAAAAAAAAAEAAACFFOZ80czLrs~QyMsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN4LO2HeCzthM"
    }
    driver.add_cookie(cookie)
    driver.refresh()
    # driver.close()

"""



