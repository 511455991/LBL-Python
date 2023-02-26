# encoding=utf-8

"""
多任务编程之多进程：threading子线程模块使用
author：LBL
date:2023-2-26
"""
import threading   # 1、导包
import time


data_list = []
def sign():
    """ 唱歌函数 """
    while True:
        print('唱歌中')
        time.sleep(1)


# 程序主入口
if __name__ == "__main__":
    print("w","W")
    """
    多任务编程分为多进程与多线程，为了被导包后防止递归创建子进程需要将子进程创建运行放在if __name__ == "__main__":下
    多线程：进程是操作系统分配资源的单位，而线程是cpu调度的基本单位，一个进程可以有多个线程，此案成之间共享全局变量。
            1、导包
                import threading
            2、创建子线程,选择目标函数
                sub_threading = threading.Thread(target=sing)
                sub_threading.Thread(target=sing, daemon=True)    # 一步创建子线程并设置为守护进程
            3、（可选）设置子线程为守护进程，即主进程运行结束就会退出，不设置的话是主线程等待子进程结束
                sub_threading.daemon = True
            4、开启子线程
                sub_threading.start()
            5、（可选）设置子进程运行结束主进程再往下运行
                sub_threading.join()

    # 给线程传递参数使用args与kwargs参数，用法与进程一致,如
        sub_threading = threading.Thread(target=sign,args=())
        
    # 互斥锁：
        因为线程间共享全局变量，当多个线程同时操作一个变量时可能会导致结果错误，解决方法：添加线程等待(join)、或者使用互斥锁
        
        g_num = 0
        
        def task():
            # 上锁
            lock.acquire()
            # 操作全局变量
            for  i in range(10000):
                global g_num
                g_num += 1
            print("task:",q_num)
            # 操作完后释放锁,不释放会造成死锁
            lock.release()
            
        if __name__ == "__main__":
            # 创建互斥锁
            lock = threading.Lock()
            sub_threading = threading.Thread(target=task)
            sub_threading.start()
    """
    # 2、创建子进程对象
    sub_threading = threading.Thread(target=sign)
    # 3、运行子进程
    sub_threading.start()
    # 设置主进程等待子进程运行结束再向下运行，不设置的话会直接向下运行
    sub_threading.join()














