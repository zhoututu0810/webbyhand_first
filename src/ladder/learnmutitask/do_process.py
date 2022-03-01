import os
import multiprocessing
from multiprocessing import Process
print('当前操作系统的核心数', multiprocessing.cpu_count())  # 查看当前系统是核心

a= 1
def abc():
    print('wabc')

# 子进程要执行的代码
def run_proc(name):	# 这个是事先定义的，说明在fork的时候，变量也会同样复制一份！！
    print('子线程执行 %s (%s)...' % (name, os.getpid()))
    print('测试变量共享不', a)     # 共享
    abc()       # 可以执行


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # start意思是fork了一个子进程，并且讲任务放在 pid ==0 的代码处进行
    p.start()   # 启动子进程，这个时候子进程已经执行了。子进程执行的同时，父进程也同时进行
    # 是不是可以理解为，process封装，就封装了部分代码进去子进程，当前报货全部的变量！！！
    print(os.getpid()) # 这一句是父进程执行的， 为什么这一句子进程不会执行？？？

    p.join() # join表示等待等待子进程的返回，父进程表示你做完了没，老子要你的数据! 应该也可以不join吧，表示你去玩吧
    print('Child process end.')