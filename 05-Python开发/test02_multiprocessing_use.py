# encoding=utf-8

"""
多任务编程之多进程：multiprocessing子进程模块使用
author：LBL
date:2023-2-26
"""

import multiprocessing   # 1、导包
import time


data_list = []
def add_data():
    """ 向列表中添加数据 """
    for i in range(3):
        time.sleep(0.2)
        data_list.append(i)
        print(i)
    print(data_list)

def read_data():
    """ 读取列表中数据 """
    print(data_list)


# 程序主入口
if __name__ == "__main__":
    """
    多任务编程分为多进程与多线程，为了被导包后防止递归创建子进程需要将子进程创建运行放在if __name__ == "__main__":下
    多进程：主进程会等子进程运行结束再结束，多个子进程启动没有顺序限制，子进程会复制主进程的全部资源，子进程之间资源不互通，不共享全局变量
            1、导包
                import multiprocessing
            2、创建子进程,选择目标函数
                add_process = multiprocessing.Process(target=add_data)
            3、（可选）设置子进程为守护进程，即主进程退出的话子进程就会退出，不设置的话是主线程等待子线程结束
                add_process.daemon = True
            4、开启子线程
                add_process.start()
            5、（可选）设置子进程运行结束主进程再往下运行
                add_process.join()
            6、（可选）主动销毁子线程
                add_process.terminate()
                
    # 子进程间通信方式：函数带参数，创建子进程时传入参数，args参数值为元组，kwargs参数值为字典
    def show_info(name,age):
        print(name,age)

    subprocess = multiprocessing.Process(target=show_info, args=('小王',20))
    subprocess = multiprocessing.Process(target=show_info, kwargs={'name':'小王', age:20})
    
    # 获取当前进程编号
    os.getpid()
    # 获取当前进程的父进程编号
    os.getppid()
    # 杀死指定进程，9代表强制杀死
    os.kill(进程编号,9)
    
    """
    # 2、创建子进程对象
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)
    # 3、运行子进程
    add_process.start()
    # 设置主进程等待子进程运行结束再向下运行，不设置的话会直接向下运行
    add_process.join()
    # 运行读取子进程
    read_process.start()         # 因为子进程间数据不互通，所以读取的是空列表[]













