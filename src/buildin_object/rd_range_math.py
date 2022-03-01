# 字符串表达式变整数
rs = eval("1+2")
print(rs)

#Python数学函数 https://www.runoob.com/python/python-numbers.html
# https://www.py.cn/faq/python/12084.html

# math.ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# math.floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# round(x [,n])	不是math的，是内置函数，返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
import math
math.ceil(-0.5)
math.floor(-0.5)
round(3.4884)



# 比较函数
# cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
# operator.lt(a, b)
# operator.le(a, b)
# operator.eq(a, b)
# operator.ne(a, b)
# operator.ge(a, b)
# operator.gt(a, b)
# operator.__lt__(a, b) # 等于operator.lt(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)
import operator
operator.eq('hello', 'name');
operator.eq('hello', 'hello');



# range范围
print(range(10))    # 返回的是range对象,[0...10）,包头不包尾
print(list(range(10)))
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print()


# 随机数
import random

print("随机整数")
# 随机一个整数（包括负数）
print(random.randint(-9, 9))

print("随机浮点数")
# 随机一个 [0 - 1.0) 之间的浮点数,包括0但是不包括1, 小数点有很多位，需要自己处理
print(random.random())
# 产生一个 1.1 到 5.4 之间的随机浮点数:
print(random.uniform(1, 5))


# 从序列中随机选取一个字符
import string
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.whitespace)

print("随机选择1个字符")
print(random.choice(string.ascii_lowercase))

print("随机字符串")
print("".join([random.choice(string.ascii_letters) for _ in range(10)]))
# 随机的选取n个字符, 随机采样
print(random.sample(string.ascii_letters, 3))   # 返回的是列表，需要字符串的join函数
# 随机姓名
xing='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
ming='豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
X=random.choice(xing)
M="".join(random.choice(ming) for i in range(2))
print(X+M)

print("随机选择多个字符")
# random.sample(population, k)
# 从指定序列中随机获取k个不重复的元素，并以列表形式返回，用于不进行内容替换的随机抽样。
# andom.sample(population, k)只有在population中没有重复元素的情况下获取到的随机抽样结果才会有相同的元素；
print("random.sample('abcd1234', 3): ", random.sample('abcd1234', 3))


# # https://blog.csdn.net/zq476668643/article/details/95219453
# import numpy as np
#
# # 产生n维的均匀分布的随机数
# print(np.random.rand(5, 5, 5))
#
# # 产生n维的正态分布的随机数
# print(np.random.randn(5, 5, 5))
#
# # 产生n--m之间的k个整数
# print(np.random.randint(1, 50, 5))
#
# # 产生n个0--1之间的随机数
# print(np.random.random(10))
#
# # 从序列中选择数据
# print(np.random.choice([2, 5, 7, 8, 9, 11, 3]))
#
# # 把序列中的数据打乱
# # np.random.shuffle(item) 不会参数返回值，改变的话是在原列表中修改的
# item = [2, 5, 7, 8, 9, 11, 3]
# np.random.shuffle(item)
# print(item)
