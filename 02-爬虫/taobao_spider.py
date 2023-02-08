# encoding=utf-8

"""
使用selenium操作浏览器抓取淘宝商品信息：图片、价格、名称、店铺
author：LBL
date:2023-2-8
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Taobao_spider(object):
    def __init__(self,goods_name):
        self.goods_name = goods_name
        self.driver = webdriver.Edge()

    """ 打开浏览器，搜索商品 """
    def search_goods(self):
        # 浏览器全屏
        self.driver.maximize_window()
        # 访问淘宝首页
        self.driver.get("https://www.taobao.com")
        # 搜索商品,操作键盘输入回车
        self.driver.find_element(By.ID,"q").send_keys(self.goods_name)
        self.driver.find_element(By.ID, "q").send_keys(Keys.ENTER)
        # 有时会跳转到登录页面,需要手动登录淘宝
        while True:
            if "login" in self.driver.current_url:
                print("请扫码登录淘宝")
                time.sleep(2)
            else:
                print("登录成功")
                break
    """ 滚动页面到底部翻页处 """
    def scroll_to_end(self):
        # 拉动四次滚轮，每次滑动1200像素
        for i in range(0,4):
            height = 1200
            js_code = "window.scrollBy(0,%d)" % height
            # selenium执行js脚本
            self.driver.execute_script(js_code)
            time.sleep(2)

    """ 获取商品信息 """
    def get_goods_info(self):
        goods_list = self.driver.find_elements(By.CSS_SELECTOR,".J_MouserOnverReq")
        for goods in goods_list:
            goods_info = {}
            # 商品图片
            pic = goods.find_element(By.CLASS_NAME,"img").get_attribute("data-src")
            if "http" not in pic :
                pic = "https://"+ pic
            goods_info.update({"picture":pic})
            # 商品价格
            price = goods.find_element(By.CSS_SELECTOR,".g_price strong").text
            goods_info.update({"price":price})
            # 商品名称
            goods_name = goods.find_element(By.CSS_SELECTOR,".title").text
            goods_info.update({"goods_name":goods_name})
            # 商品店铺
            shop_name = goods.find_element(By.CSS_SELECTOR,".shopname").text
            goods_info.update({"shop_name":shop_name})
            # 商品链接
            goods_link = goods.find_element(By.CSS_SELECTOR,".J_ClickStat").get_attribute("href")
            goods_info.update({"goods_link":goods_link})

            print(goods_info)


    def run(self):
        # 打开淘宝，搜索商品
        self.search_goods()
        # 起始页1
        page_num = 1
        while True:
            print("正在抓取第" + str(page_num) + "页商品信息")
            # 滑动页面到底部，加载全部页面
            self.scroll_to_end()
            # 清洗数据,获取商品信息
            self.get_goods_info()
            # 翻页
            next_element = self.driver.find_element(By.CLASS_NAME,"next")
            next_page = next_element.find_element(By.TAG_NAME,"a")
            if next_page:
                next_page.click()
                time.sleep(2)
                page_num += 1
            else:
                print("到末页了，抓取结束")
                break
        # 退出浏览器
        self.driver.quit()




# 程序主入口
if __name__ == "__main__":
    # goods_name = input("请输入要抓取的商品名称")
    goods_name = "电风扇"
    taobao_spider = Taobao_spider(goods_name)
    taobao_spider.run()

