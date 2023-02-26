# encoding=utf-8

"""
使用socket模块开发基于TCP协议的网络通讯程序--客户端
author：LBL
date:2023-2-26
"""
import socket       # 0、导包


# 1、创建客户端套接字。               参数socket.AF_INET代表IPV4,  socket.SOCK_STREAM代表tcp协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、建立链接,设置服务端IP、端口。     用本地本地局域网模拟服务端 192.168.0.1
tcp_client_socket.connect(("192.168.21.1",9000))
while True:
    data = input("输入发送的内容：")
    if 'q' == data:
        # 5、断开链接
        tcp_client_socket.close()
        break
    # 3、发送数据（需要编码成二进制）
    tcp_client_socket.send(data.encode('gbk'))
    # 4、接收数据，需要指定最大字节，然后解码
    recv_data = tcp_client_socket.recv(128).decode('gbk')
    print(recv_data)

""" 默认情况下一个py文件不能同时多开，想同时运行多个客户端可编辑pycharm中该py文件设置：allow parallel run  """























