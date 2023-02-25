# encoding=utf-8

"""
TKinter做带界面的爬取网易云音乐程序，并使用pyinstaller打包为exe
author：LBL
date:2023-2-12
"""
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def get_music():
    """ 按用户输入的名称下载音乐 """
    # 获取输入框文本
    name = entry.get()
    print(name)

    # 访问网易音乐进行爬虫
    url = 'https://music.163.com/#/search/m/?s={}'.format(name)
    # 调试用，有界面访问方式 driver = webdriver.Chrome(executable_path=r"D:\\Python\Python310\Scripts\chromedriver.exe")
    # 设置谷歌浏览器启动参数:--headless代表无界面访问。驱动定位不到，直接指定驱动位置
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"D:\\Python\Python310\Scripts\chromedriver.exe", chrome_options=option)

    driver.get(url)
    # print(driver.page_source)

    # 网易云音乐真坏，所有内容都放在子页面里，定位元素找半天才看到
    # 按名称搜索获取第一个歌曲的链接，
    driver.switch_to.frame("g_iframe")
    href = driver.find_element(By.XPATH,'.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    song_id = href.split("=")[-1]
    print(href)
    print("歌曲id："+song_id)
    song_name = driver.find_element(By.XPATH,'.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    print("歌曲名称："+song_name)

    # 根据id下载音乐
    song_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)
    # 终端显示
    print("正在下载{}".format(song_name))
    with open("{}.mp3".format(song_name), "wb") as f:
        f.write(requests.get(song_url).content)
    print("{}下载完成".format(song_name))

    # 文本框,最后插入消息，
    text.insert(END, "{}下载完成".format(song_name))
    # 文本框滚动到末尾
    text.see(END)
    # 更新文本框内容
    text.update()



# 程序主入口
if __name__ == "__main__":
    # TKinter是python自带的实现GUI模块
    # 主窗口
    root = Tk()
    # 设置窗口大小500x400，位置0，0
    root.geometry('700x500+0+0')
    # 窗口标题
    root.title('music_download')

    # 添加lable标签,row行号，column列号，columnspan占几列，
    label = Label(root, text="请输入歌曲名称：", font=('微软雅黑', 15))
    label.grid(row=0, column=0)

    # 添加entry输入框
    entry = Entry(root, font=('微软雅黑', 15))
    entry.grid(row=0, column=1)

    # 添加listbox列表显示框,一列占40px,这个占两列，总共长80px
    text = Listbox(root, font=('微软雅黑', 15), width=40, height=4)
    text.grid(row=1,columnspan=2,sticky=W)

    # 添加button按钮,命令直接操作元素或是一个函数,sticky可以设置控件对齐方式：W左E右
    button_s = Button(root, text='开始搜索', width="10", command=get_music)
    button_s.grid(row=2, column=0,sticky=W)
    button_q = Button(root, text="退出程序", width="10", command=root.quit)
    button_q.grid(row=2, column=1, sticky=E)

    #主窗口不断循环，这样才能显示
    root.mainloop()
    input("please input any key to exit")



# 程序打包成exe:
# 1、安装第三方模块 pip install pyinstaller
# 2、执行cmd命令：pyinstaller -F  test23_tkinter_use.py -w
# -F打包成一个可执行文件，-w不显示控制台窗口，-i指定ico图标
# 打包的exe运行可能出现闪退情况，解决方法，在主函数程序最后以行加额外代码让程序处于等待状态： input("please input any key to exit")
# 调试闪退问题：由于闪退看不到报错，可以cmd运行打包的程序如test.exe就可以看到报错了。
# 本地python环境问题也会导致打包出的程序有问题，可能换台电脑打包的就能执行，检查环境
# 可能引起错误原因：
# 程序中使用到的外部文件的路径与.exe的相对位置与程序中的不同，使得引用的资源文件丢失。
# 本地存在多个版本的python，打包成.exe程序的时候使用了与被打包程序不匹配的python对应的pyinstaller，导致打包之后的程序缺少了依赖的包。

