# encoding=utf-8

"""
常用模块：logging日志、time格式化输出时间、hashlib哈希校验文件、keyword查看关键词
author：LBL
date:2023-2-9
"""
import logging  # python自带的日志模块
import time
import hashlib
import keyword


if __name__ == "__main__":
    # 日志
    logging.basicConfig(level=logging.DEBUG)        # 设置日志级别，默认为warning
    logging.debug("debug级别的日志")                  # 打印日志
    logging.info("info级别的日志")
    logging.warning("warning级别的日志")
    logging.error("error级别的日志")
    logging.critical("critical级别的日志")
    """ 其他日志设置：format指定格式。当前时间、程序文件名、行号、日志级别、日志信息
        filename 输出到文件，默认输出到控制台
        filemode 模式 w覆盖 a追加"""
    # logging.basicConfig(level=logging.ERROR,
    #                     format="%(asctime)s-%(filename)s[lineno:%(lineon)d]-%(levelname)s-%(message)s",
    #                     filename="log.txt",
    #                     filemode="w")

    # 时间
    time.sleep(2)           # 暂停运行
    # 打印系统时间
    print(time.asctime())   # Thu Feb  9 15:04:31 2023
    print(time.time())      # 1675926271.3368564
    # 格式化输出时间Y年、m月、d日、H时、M分、S秒、z时区   2023-02-09 15-06
    print(time.strftime('%Y-%m-%d %H-%M'))

    # 哈希值常用来校验文件，哈希值变了代表文件被改变过
    data = 'python哈哈哈'
    # 创建哈希对象，选择加密方式
    md5 = hashlib.md5()
    # 向hash对象中添加数据，数据需要是二进制，字符串encode后为二进制
    md5.update(data.encode())
    # 获取hash值
    result = md5.hexdigest()
    print(result)

    # keyword可以列出python所有关键词
    print(keyword.kwlist)
    # 判断某个词是否是关键词
    print(keyword.iskeyword('False'))