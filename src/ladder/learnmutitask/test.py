# 单核CPU是怎么执行多任务的呢？
# 答案就是操作系统轮流让各个任务交替执行（问题是如何保存各个任务的对象和上下文）
# 对于操作系统来说，一个任务就是一个进程（Process）
# 在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
#
# 如果我们要同时执行多个任务怎么办？
# 有两种解决方案：
# 一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
# 还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
# 当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。

# fork创建子进程process
# fork方法比较原始，python用multiprocessing模块的Process类封装了对进程的调用！
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# fork()调用一次，返回两次(这是fork函数最最最特殊的地方)
# os.getpid()  返回当前进程process的ID
# os.getppid() 返回父进程的ID
pid = os.fork()
if pid == 0:    # 子进程永远返回0，调用getppid()就可以拿到父进程的ID
    # 这一块代码是子进程在执行 神奇吧
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:           # 父进程返回子进程的ID
    # 这一块代码是父进程在执行  神奇吧
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))




from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print('Current parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()   # 启动子进程，这个时候子进程已经执行了。子进程执行的同时，父进程也同时进行
    print(os.getpid) # 这一样是父进程执行的
    p.join() # join表示等待等待子进程的返回，父进程表示你做完了没，老子要你的数据!
    print('Child process end.')


