# encoding=utf-8

"""
编写自己的静态web服务器，（多线程面向对象版，启动者指定端口启动）
author：LBL
date:2023-2-26
"""
import socket
import threading
import sys


class HttpWebServer(object):
    def __init__(self,port):
        """ 构造器，初始化参数(准备服务端套接字) """
        # 创建服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字属性:端口复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 给套接字绑定(ip、端口)
        tcp_server_socket.bind(("", port))
        # 开启监听
        tcp_server_socket.listen(128)
        # 创建一个实例属性self.tcp_server_socket，上面那些都不是对象属性，是局部变量，为的就是得到这个对象的套接字
        self.tcp_server_socket = tcp_server_socket

    def handle_client_request(self,new_socket):
        """ 接收新套接字，处理客户端信息 """
        # 接收客户端请求的数据,解码。    client_data为HTTP请求数据，第一行格式为：GET / HTTP/1.1
        client_data = new_socket.recv(4096).decode('utf-8')
        # print(client_data)
        # 判断，如果客户端连接但是没发数据就主动断掉连接
        if len(client_data) == 0:
            new_socket.close()
            return

        # 获取用户访问的路径，
        file_name = client_data.split()[1]
        # 如果用户不指定文件，就给他返回主页
        if file_name == "/":
            file_name = "./index.html"
        try:
            # 读取用户访问的文件
            with open(file_name,'rb') as f:
                f_data = f.read()
        except Exception as e:
            print(e)
            # 如果没有找到文件，拼接404页面返回
            # 响应行
            response_line = 'HTTP/1.1 404 NOT FOUND1 \r\n'
            # 响应头
            response_header = 'Server:BWS/1.1 \r\n'
            # 响应体
            with open('./error.html', 'rb') as f:
                response_body = f.read()
            # 拼接响应，发送响应
            response = (response_line + response_header +'\r\n').encode('utf-8') + response_body
            new_socket.send(response)
        else:
            # 未出错情况，封装http格式返回数据
            response_line = 'HTTP/1.1 200 OK \r\n'
            response_header = 'Server:BWS/1.1 \r\n'
            response_body = f_data
            # 拼装响应，发送响应
            response = (response_line + response_header +'\r\n').encode('utf-8') + response_body
            new_socket.send(response)
        finally:
            # 关闭套接字
            new_socket.close()


    def run(self):
        """ 执行程序 """
        while True:
            # 接收客户端连接，得到新套接字和客户端地址
            new_socket,ip_port = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request,args=(new_socket,))
            # 启动子线程
            sub_thread.start()


def main():
    # 判断启动命令的参数个数
    if len(sys.argv) != 2:
        print("命令格式为：python test05_web_server.py 9001")
        return
    # 判断第二个参数是否是数字。能否能做启动端口
    if not sys.argv[1].isdigit():
        print("命令格式为：python test05_web_server.py 9001")
        return
    else:
        # 获取启动端口
        port = int(sys.argv[1])
        # 创建对象，执行对象的run方法
        http_server = HttpWebServer(port)
        http_server.run()


# 程序主入口
if __name__ == "__main__":
    main()

    # cmd启动：python test05_web_server.py 9001  ，浏览器访问地址1217.0.0.1:9000， 脚本所在位置需要有error.html和其他html文件





























