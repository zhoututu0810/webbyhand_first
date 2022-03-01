# 单向加密 最主要的就是摘要算法，摘要算法包括MD5 SHA SMAC

# 因为hashlib模块不仅仅是整合了md5和sha模块的功能，还提供了对更多中算法的函数实现，
# 如：MD5，SHA1，SHA224，SHA256，SHA384和SHA512。

# 提示： “安全哈希/安全散列” 与 “信息摘要” 这两个术语是可以等价互换的。
# 比较老的算法被称为消息摘要，而现代属于都是安全哈希/安全散列。

import hashlib
from hashlib import pbkdf2_hmac # 注意区分hmac和pbkdf2_hmac
import hmac


# 获取晒要算法对象
# hash = hashlib.new('md5')    # 不常用，建议用下面的快捷放肆
hash_md5 = hashlib.md5()
hash_sha256 = hashlib.sha256
messge = '123'
hash_md5.update(messge.encode('utf-8')) # 注意：这个返回的是None，要拿数据，还是从hash对象拿
# 从hash对象才能拿数据
ret = hash_md5.hexdigest()
print(ret)



print('开始测试hmac')
# HMAC算法也是一种一种单项加密算法，并且它是基于上面各种哈希算法/散列算法的，
# 只是它可以在运算过程中使用一个密钥来增增强安全性。
# hmac模块实现了HAMC算法，提供了相应的函数和方法，且与hashlib提供的api基本一致。

key = 'dfasdfadf'.encode('utf-8')
shash = hmac.new(key=key, digestmod=hashlib.sha256)
shash.update('hello'.encode('utf-8'))
shash.update('world'.encode('utf-8'))
ret = shash.hexdigest()
print(type(ret), ret)
# <class 'str'> 879b47311f4f6a919dcc7537ec719a96b336dfa7bcdf98389896378efb2109b0



