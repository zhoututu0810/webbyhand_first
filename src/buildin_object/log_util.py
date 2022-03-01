import logging
from logging import handlers
import os


# 准备日志文件路径

# 自定义一个logger对象
log = logging.getLogger('mylogger')
log.setLevel(logging.DEBUG)     # 第一个层记录哪些日志被记录

# 创建hander日志处理器(handle的作用 1.处理日志的输出流，2.格式化日志)
# 创建一个handle, 用于写入日志文件
fh = handlers.TimedRotatingFileHandler('log/debug.log', 'd', 1, 7)
fh.setLevel(logging.DEBUG)      #.往这个目的地过滤写哪些日志，不定义用全部写
fh2 = logging.FileHandler('log/error.log')
fh2.setLevel(logging.ERROR)
fh3 = logging.StreamHandler()
fh3.setLevel(logging.DEBUG)

# 创建输出的日志格式化
formatter = logging.Formatter(os.linesep +
                              '%(asctime)s-[%(levelname)s]-[%(filename)s]-[%(funcName)s]-[%(lineno)dno]:' +
                              os.linesep +'%(message)s')
fh.setFormatter(formatter)
fh2.setFormatter(formatter)
fh3.setFormatter(formatter)

# 过滤是怎么用的？

# 最重要的一步，给日志添加处理器
log.addHandler(fh)
log.addHandler(fh2)
log.addHandler(fh3)


if __name__ == '__main__':
    def tst():
        try:
            1/0
        except Exception as e:
            log.exception('必填参数')
    tst()
    log.debug('121')
    log.error('324234')