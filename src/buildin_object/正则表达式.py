import re
# 枚举特殊字符 https://www.cnblogs.com/yyyg/p/5498803.html
# \ 转义字符  \d匹配任意十进制数，相当于 [0-9]  \w 匹配任意数字和字母，相当于 [a-zA-Z0-9_]注意不包括所有的符号哦！ \s 匹配任意空白字符，相当于 [ \t\n\r\f\v]
# 锚定符 ^ $
# 个数修饰符 * + ？{m,[n]}  非贪婪匹配 *? +? ??
# 通配符 .
# [] 范围枚举
# ( | ) 分组提取和选择匹配  (?P<name>...)  ?P=name 分组别名定义和引用

# pattern_str格式是要求的哦
# 单行
pattern_str = r''
# 多行
pattern_str = r'''
line1
line2
'''

# 方法分类 - 匹配一个
# re.match默认从字符串的起点开始匹配(参数可以指定位置)，匹配成功返回Match对象，不成功返回None
# re.search可以看做是循环match。re.search第一次从第一个位置开始匹配，如果没有匹配到，再从第二个位置开始匹配，返回第一词匹配成功的就返回
# match和search方法的Match对象groups是空的，因为只返回一个，所以group()=group(1)匹配的字符串哦！，所以只用group就可以
# re模块的方法本质都是Pattern对象方法，举例说明
test_str = 'abc123cdf456'
pattern_str = r'\d'
pattern = re.compile(pattern_str, re.I)
match1 = pattern.match(string=test_str, pos=0, endpos=len(test_str)-1)  # 从字符串开头匹配，匹配到返回match的对象，匹配不到返回None
match1 = re.match(pattern_str, test_str, re.I)  # 区别就是不能指定起始位置和结束位置
match2 = pattern.search(string=test_str, pos=0, endpos=len(test_str)-1) # 扫描整个字符串返回"第一个"匹配到的元素并结束，匹配不到返回None

# print('match1.group()', match1.group())   # 返回match是一个None对象，因为第一个字符不是数字，匹配不上
# print('match1.groups()', match1.groups())
print('match2.group(0)', match2.group(0))
print('match2.groups()', match2.groups())


# 方法分类 - 匹配多个
# re.findall(pattern, string[, flags])
# re.finditer(pattern, string[, flags])
# findall返回类似search，区别是search匹配第一个成功后就返回了，但是findall会去掉应匹配的字符串，在剩余的字符串继续匹配，直到砍掉所有字符串
# findall返回的不是match对象，返回的是一个匹配结果的元素
# finditer和findall一样,区别是返回一个迭代器，可以用for循环go through
test_str = 'abc123cdf456'
pattern_str = r'\d'
pattern_str = r'\d'
pattern = re.compile(pattern_str)
ret_tuple = pattern.findall(string=test_str)    # 注意返回的不是Match对象，返回的是元素
print('ret_tuple', ret_tuple)


# -----------------------------------
# 提取子串
# 提取子串的作用的前提是先有匹配的了的串，首先是匹配到了字符串，我想要在匹配到的整个串中再提取部分。如果是findall有多个匹配的串，那么就会返回二元元祖哦！
# 常见的例子，匹配将电话号码的中间四位掩码
phone = '13113639422'
pattern_str = r'(\d{3})(\d{4})(\d{4})'
match_phone = re.sub(pattern_str, r'\1****\3', phone)
print('match_phone', match_phone)

# group([index1, …]): 	index1表示索引
# 获得一个或多个分组截获的字符串；group方法指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配到的字符串，注意不是原来的字符串哦！
# ；不填写参数时，返回group(0)；千万注意："没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。"
# groups([default]):
# 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
# groupdict([default]):
# 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
# start([group]):  参数是某个组的索引或者别名
# 返回"指定的组"截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
# end([group]):
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
# span([group]):
# 返回(start(group), end(group))。
# expand(template): 很强大强大的方法，引用子串拼接成新的字符串，太牛逼了！
# 将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。
match4 = re.match(r'(\d{3})-(\d{3,8})', '010-12345efg')
print('match4.group()', match4.group())     # 返回匹配的字符串，010-12345，
print('match4.group(0)', match4.group(0))
print('match4.group(1)', match4.group(1))
print('match4.group(2)', match4.group(2))
print('match4.groups()', match4.groups())   # 相当于调用group(1,2,…last)
print('match4.start()', match4.start())
print('match4.start(1)', match4.start(1))
print('match4.start(2)', match4.start(2))
print("match4.expand(r'\g2 - - \g1')", match4.expand(r'\g<2> - - \g<1>'))


m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group(1,2):", m.group(1, 2, 3))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
# 重要，没有讲到这个的就是傻逼文章
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

### output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2,3): ('hello', 'world', '!')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!

# -------------------------------------------------
# re.sub和re.subn方法用于替换字符串
# sub(pattern, repl, string, count=0, flags=0):  repl表示替换的字符串，string表示待匹配的字符串
# subn(pattern, repl, string, count=0, flags=0):
# 注意：repl可以引用匹配后的分组
ret = re.sub(r'\d{4}$', '0000', '13113639422')  # 类似findall，然后替换all,返回替换后的字符串
print(ret)
ret = re.sub(r'\d','ok', 'ab1cd22ef333')
print(ret)
ret = re.subn(r'\d{4}$', '0000', '13113639422') # 返回元祖，第一个位置表示替换后的字符串，第二个位置表示替换的次数
print(ret)
ret = re.subn(r'\d','ok', 'ab1cd22ef333')
print(ret)

# -------------------------------------------------
# re.split()切割字符串，类似字符串的split()方法，不同的是更自由，可以定制哦
re.split(r'\s+', 'a b   c')      # ['a', 'b', 'c']
re.split(r'[\s\,]+', 'a,b, c  d')   # ['a', 'b', 'c', 'd']
re.split(r'[\s\,\;]+', 'a,b;; c  d')    # ['a', 'b', 'c', 'd']


if __name__ == '__main__':
    pass