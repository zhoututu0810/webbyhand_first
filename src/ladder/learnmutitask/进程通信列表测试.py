from multiprocessing import Process, Queue
import os, time, random

a = 1
test_list = []

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    print('测试写入中的的a', a)
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        # q.append(value)
        # print('写入q', q)
        test_list.append(value)
        print('写入test_list', test_list)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    print('测试读取中的的a', a)
    while True:
        print('test_list的长度', len(test_list))
        if len(test_list):      # 也不会共享，相当于变量test_list拷贝了一份，在哪个线程改了就改了，但是这个线程还是没改哦
            # value = q.pop(0) # ？？？
            # print('读取q', q)     # 根本读取不了，不会共享
            print('读取q', test_list)  # 根本读取不了，不会共享
            # print('Get %s from queue.' % value)



if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = []		# 问题，子进程不会拷贝变量吗？
# 这个q和队列有啥区别，我如果定义一个列表传递进去，会共享吗？
    pw = Process(target=write, args=(q,))   # 当做形参传递进去列表不会共享
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()