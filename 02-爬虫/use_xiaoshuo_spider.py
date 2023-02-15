"""
爬取小说网站，使用lxml清洗数据，并将小说数据存入mysql数据库
author：LBL
date:2023-2-15

"""
import time
from test24_pymysql_use import DBUtil
import requests
from lxml import etree


class xiaoshuo_spider(object):
    def __init__(self):
        # 某小说章节列表
        self.url1 = "https://www.z1xs.com/book/9388/"
        self.header = {'User-Agent':'Mozilla/5.0'}

    def get_url(self):
        """ 获取一本小说的所有章节地址 """
        url_list = []
        # gb18030是比gbk编码方式大一些的编码
        response = requests.get(url=self.url1,headers=self.header).content.decode("gb18030")
        # print(response)
        parse_html = etree.HTML(response)

        # 定位每个章节的a标签元素的href属性，即链接地址
        xpath_bds = '//dd/a/@href'
        data_list = parse_html.xpath(xpath_bds)

        for data in data_list:
            url_list.append("https://www.z1xs.com/" + data)
        print(url_list)
        return url_list

    def save_data(self, url_list):
        """ 爬取网址章节内容并存到数据库 """
        for url in url_list:
            print(url)
            # errors="ignore"可以避免因为某个字符解码失败导致报错无法继续爬虫
            response = requests.get(url=url,headers=self.header).content.decode('gbk',errors="ignore")
            # 创建html解析对象
            parse_html = etree.HTML(response)
            # 定位获取章节名称
            xpath_name = "//h1//text()"
            name = parse_html.xpath(xpath_name)[0]
            # 获取原始小说文本段落列表
            xpath_text = "//div[@id='content']//text()"
            text = parse_html.xpath(xpath_text)
            # 处理小说文本,去除段落前后空格
            res = ""
            for t in text:
                # print(t.strip())
                res += t.strip()
            data = (name,res,url)
            # 将章节元组存入数据库
            self.save_to_mysql(data)
            print(name+"爬取完成")

    def save_to_mysql(self,data):
        """ 将章节元组存入数据库 """
        # 拼接sql语句
        # 本地需有db1数据库，xiaoshuo表，属性有：id主键自增长，name,text,url
        sql = 'insert into xiaoshuo(name,text,url) values("{}","{}","{}");'.format(data[0],data[1],data[2])
        # print(sql)
        # 调用之前编写的工具类执行失sql
        DBUtil.exec_sql(sql)

# 程序主入口
if __name__ == "__main__":
    # 创建爬虫对象
    spider = xiaoshuo_spider()
    # 获取章节url列表
    url_list = spider.get_url()
    time.sleep(0.01)
    # 保存每个章节内容
    spider.save_data(url_list)