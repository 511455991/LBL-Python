# encoding=utf-8

"""
使用requests抓取代理网站数据，并使用BeautifulSoup解析高匿ip代理地址
author：LBL
date:2023-2-8
"""
import requests
from bs4 import BeautifulSoup
import time


class IP_spider(object):
    def __init__(self,):
        self.url = "http://www.ip3366.net/?stype=1&page={}"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
        self.proxies_list = []

    def get_proxies_ip(self, page):
        """ 获取代理ip列表 """
        url = self.url.format(page)
        response = requests.get(url=url, headers=self.header)
        ip_list = []
        if response.status_code == 200:
            html = response.text
            # 使用bs4清洗数据获得ip信息
            soup = BeautifulSoup(html, 'lxml')
            tr_list = soup.select("table tbody tr")     # 列表一条tr是一个ip信息
            for tr in tr_list:
                td_info = tr.select('td')                   # 下面单元格是td，每个td是一部分信息
                ip_host = td_info[0].text.strip()           # td0:地址
                ip_port = td_info[1].text.strip()           # td1:端口
                ip_base = "//" + ip_host+":" + ip_port      # 手动拼接出除了协议的完整格式
                ip_list.append(ip_base)
            return ip_list


    def run(self):
        """ 执行程序 """
        # 爬取网站前十页可用的IP高匿代理地址
        for page in range(1,10):
            time.sleep(1)   # 访问太快会被拉黑名单
            ip_list = self.get_proxies_ip(page)
            print(ip_list)
            for ip_info in ip_list:
                proxies = {
                    'http': 'http:' + ip_info,
                    'https': 'https:' + ip_info
                }
                self.proxies_list.append(proxies)
        return self.proxies_list



# 程序主入口
if __name__ == "__main__":
    spider = IP_spider()
    proxies_list = spider.run()
    print(proxies_list)

    # 代理地址网站3366代理： http://www.ip3366.net/?stype=1&page=3
    # 89代理：   https://www.89ip.cn/index_2.html
    # jiangxianli代理：https://ip.jiangxianli.com/?page=1
    # 小幻国际代理： https://ip.ihuan.me/
    # 小幻国内代理： https://ip.ihuan.me/address/5Lit5Zu9.html
    # 小舒代理：     https://www.xsdaili.cn/


"""  html源码格式大概如下
...<table>...<tbody>...
            <tr>
                <td>111.225.153.240</td>
                <td>8089</td>
                <td>高匿代理IP</td>
                <td>HTTPS</td>
                <td>GET, POST</td>
                <td>河北省张家口市</td>
                <td>1秒</td>
                <td>2023/1/18 6:00:02</td>
            </tr>
           
            <tr>
                <td>111.225.152.29</td>
                <td>8089</td>
                <td>高匿代理IP</td>
                <td>HTTPS</td>
                <td>GET, POST</td>
                <td>河北省张家口市</td>
                <td>5秒</td>
                <td>2023/1/18 2:00:03</td>
            </tr>
"""

