import sys
import codecs
import encodings.utf_8


str1 = 'abc草'

coder = codecs.lookup('utf-8')
print(type(coder))  # <class 'codecs.CodecInfo'>
# [
#   <built-in function utf_8_encode>,
#   <function decode at 0x102833dd0>,
#   <class 'encodings.utf_8.StreamReader'>,
#   <class 'encodings.utf_8.StreamWriter'>
#  ]
print(list(coder))
print(coder.encode(str1))   # b'abc\xe8\x8d\x89', 4)  还返回了长度
print(coder.decode(coder.encode(str1)[0]))

# 内建函数
a = codecs.getreader('utf-8')
print(a)        # <class 'encodings.utf_8.StreamReader'>
print(dir(a))

