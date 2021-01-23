##start() 方法创建子进程
# from multiprocessing  import Process                ##导入multiprocessing模块

# ##执行子程序代码
# def test(name):
#     print('我是子程序',name)

# ##执行主程序
# def main():
#     print("主程序开始")
#     p = Process(target = test,args =('lhuan',))      ##实例化Process类
#     p.start()                                        ##启动子进程
#     print("主进程结束")

# if __name__ == "__main__":
#     main()

##join() 方法 创建子进程
##p.join([timeout])   主线程等待p终止（ps：主线程处于等的状态，而p处于运行的状态）
# timeout时可选的超时时间。（ps：p.join只能join住start开启的进程，而不能join住run开启的进程。
# import time
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     time.sleep(1)
#     print('子进程')
# if __name__=='__main__':
#     p=Process(target=f,args=('lhuan',))
#     p.start()
#     # p.run()
#     p.join() #如果改为p.run（）则后面的不会执行 
#     print('主程序')



##创建两个子进程，并记录子进程的运行时间
# from multiprocessing import Process
# import time
# import os

# ##两个子进程会调用的方法
# def child_1(interval):
#     print("子进程(%s)开始执行,父进程为:(%s)"%(os.getpid(),os.getppid()))
#     t_start = time.time()                                               ##计时开始
#     time.sleep(interval)                                                ##程序将会被挂起interval秒
#     t_end = time.time()                                                 ##计时结束
#     print("子进程(%s)执行时间为'%0.2f'秒"%(os.getpid(),t_end-t_start))

# def child_2(interval):
#     print("子进程(%s)开始执行,父进程为:(%s)"%(os.getpid(),os.getppid()))
#     t_start = time.time()                                               ##计时开始
#     time.sleep(interval)                                                ##程序将会被挂起interval秒
#     t_end = time.time()                                                 ##计时结束
#     print("子进程(%s)执行时间为'%0.2f'秒"%(os.getpid(),t_end-t_start))

# if __name__ == "__main__":
#     print("----------------父程序执行----------------")
#     print("父程序PID :%s "%os.getpid())                                 ##输出当前程序的ID
#     P1 = Process(target=child_1,args=(1,))                              ##实例化进程p1
#     P2 = Process(target=child_2,args=(1,))                              ##实例化进程p2
#     P1.start()                                                          ##启动进程p1
#     P2.start()                                                          ##启动进程p2
#     ##同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
#     print("P1.is_alive=%s"%P1.is_alive())
#     print("P2.is_alive=%s"%P2.is_alive())
#     ##输出P1和P2进程的别名和PID
#     print("P1.NAME: %s"%P1.name)
#     print("P1.pid: %s"%P1.pid)
#     print("P2.NAME: %s"%P2.name)
#     print("P2.pid: %s"%P2.pid)
#     print("----------------等待子进程----------------")
#     P1.join()                                                           ##等待P1进程结束
#     P2.join()                                                           ##等待P2进程结束
#     print("----------------父进程执行结束----------------")


#多个进程
# import time,os
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     print("子进程的pid=%s"%os.getpid())
#     time.sleep(1)

# if __name__=='__main__':
#     print("----------------父程序执行----------------")
#     print("父程序PID :%s "%os.getpid())                                 ##输出当前程序的ID
#     p_lst=[]
#     for i in range(5):
#         p=Process(target=f,args=('lhuan',))
#         p.start()
#         p_lst.append(p)
#     print(p_lst)
#     print('----------------父程序结束----------------')


# import  time,os
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     print("子进程的pid=%s"%os.getpid())
#     time.sleep(1)
# if __name__=='__main__':
#     print("----------------父程序执行----------------")
#     print("父程序PID :%s "%os.getpid())                                 ##输出当前程序的ID
#     p_lst=[]
#     for i in range(5):
#         p=Process(target=f,args=('lhuan',))
#         p.start()
#         p_lst.append(p)
#         p.join()      ## [p.join() for p in p_lst]作用相同
#     print(p_lst)     
#     print('----------------父程序结束----------------')


# import os
# import  time
# from multiprocessing import  Process
# class Myprocess(Process):
#     def __init__(self,person):
#         super().__init__()
#         self.person=person
#     def run(self):
#         print(self.person)
#         print("子进程的pid=%s"%os.getpid())
# if __name__=='__main__':
#     print("----------------父程序执行----------------")
#     print("父程序PID :%s "%os.getpid()) ##输出当前程序的ID
#     p=Myprocess('lhuan')
#     p.daemon=True                       #一定要在p.start()前设置，设置p为守护进程，禁止p创建子进程，并且父进程代码执行结束，p即终止运行
#     p.start()
#     print("父程序PID :%s "%os.getpid()) ##输出当前程序的ID
#     time.sleep(10)                      #在sleep时查看进程id对应的进程
#     print('----------------父程序结束----------------')


import os
import  time
from multiprocessing import  Process
class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person=person
    def run(self):
        print(self.person)
        print("子进程的pid=%s"%os.getpid())
if __name__=='__main__':
    print("----------------父程序执行----------------")
    print("父程序PID :%s "%os.getpid()) ##输出当前程序的ID
    p=Myprocess('lhuan')
                          #一定要在p.start()前设置，设置p为守护进程，禁止p创建子进程，并且父进程代码执行结束，p即终止运行
    p.start()
    p.daemon=True 
    print("父程序PID :%s "%os.getpid()) ##输出当前程序的ID
    time.sleep(10)                      #在sleep时查看进程id对应的进程
    print('----------------父程序结束----------------')