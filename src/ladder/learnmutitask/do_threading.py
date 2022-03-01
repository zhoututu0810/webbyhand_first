import time
import threading
import os

# 新线程执行的代码:
def loop():  # 子线程执行
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print(os.getpid())
print('thread %s is running' % threading.current_thread().name)  # 主线程执行
t = threading.Thread(target=loop, name='LoopThread')  # name表示定义的线程名
t.start()
# t.join()
print('thread %s ended.' % threading.current_thread().name)