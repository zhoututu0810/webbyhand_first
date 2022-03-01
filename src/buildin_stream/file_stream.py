import os
# 参考菜鸟
# open(file, mode='r', buffering=None, encoding=none, errors=None, newline=None, closefd=True):
# open()的本质创建一个文件流
# encoding的本质，open默认读取的二进制0101，是字符串，如果指定了文本模式t，那么就会用指定的解码类型，解码成为字符串
# 组要注意的读取文本，本质是读取二进制的字节串


# fileObject.read([size]);
# 参数
# size -- 从文件中读取的字节数，默认为 -1，表示读取整个文件。
# 返回值
# 返回从字符串中读取的字节还是字符，要依赖open的类型！。


# fileObject.readlines( );
# readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
# 如果碰到结束符 EOF 则返回空字符串。
# 注意：读取的字符串包括换行符，所以必须手动去掉

# 参数
# 无。
# 返回值
# 返回列表，包含所有的行。
with open('test.txt', mode='r', encoding='utf-8') as fp:
    lines = fp.readlines()
    print(lines, end='')


# fileObject.readline(size)  # 读取探针(指针)所在的行，读取一行的内容，探针移动到下一行
# readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
# 参数
# size -- 从文件中读取的字节数。
# 返回值
# 返回从字符串中读取的字节。
print()
print('测试结尾换行符是否有')
with open('test.txt', mode='r', encoding='utf-8') as fp:
    while True:
        line = fp.readline()
        if line:
            print(line, end='')
        else:
            break

# fileObject.write( [ str ])
# write() 方法用于向文件中写入指定字符串。
# 在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
# 如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。


# fileObject.writelines( [ str ])
# ritelines() 方法用于向文件中写入一序列的字符串。
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 换行需要制定换行符 \n。
# 参数
# str -- 要写入文件的字符串序列。
# 返回值
# 该方法没有返回值。


# fileObject.flush();
# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。


# fileObject.close();
# close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
# 当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。

