# encoding=utf-8

"""
使用socket模块开发基于TCP协议的网络通讯程序--服务端（多任务版，可同时服务多个客户端）
author：LBL
date:2023-2-26
"""
import socket       # 0、导包
import threading


def client_data(new_socket, client_ip):
    """ 子线程函数，接收新套接字，处理客户端发送过来的数据 """
    while True:
        # 死循环，使用新套接字循环接收客户端发送过来的信息，指定最大字节、解码方式
        recv_data = new_socket.recv(128).decode('gbk')
        if recv_data:
            print(recv_data)
            send_data = "服务器发送的数据".encode('gbk')
            new_socket.send(send_data)
        else:
            # 没接收到数据
            print("客户端已关闭",client_ip)
            break
    # 7.关闭套接字
    new_socket.close()

if __name__ == "__main__":
    # 1、创建服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、设置套接字属性。  socket.SOL_SOCKET表示当前套接字。 socket.SO_REUSEADDR是设置端口复用，退出程序后可立即释放端口。 True表示确定
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 3、绑定ip、端口（不写死ip则表示本地多个ip的话每个都可以）
    tcp_server_socket.bind(("",9000))

    # 死循环不停接收新客户端连接
    while True:
        # 开始监听
        tcp_server_socket.listen()
        # 接收到客户端连接后，会返回新套接字和客户端ip地址
        new_socket, client_ip = tcp_server_socket.accept()
        print("客户端已连接，地址是：", client_ip)
        # 创建子线程，目标函数为client_data处理客户端信息，传递参数为返回的新套接字和客户端的ip,设为守护进程
        sub_thread = threading.Thread(target=client_data, args=(new_socket, client_ip),daemon=True)
        sub_thread.start()
    # 关闭服务端套接字。一般不用关闭tcp_server_socket.close()




























