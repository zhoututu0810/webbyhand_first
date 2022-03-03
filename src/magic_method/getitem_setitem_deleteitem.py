class DataTest(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        # 不定义该方法，[]会访问TypeError: 'DataTest' object is not subscriptable
        print('enter getitem', item)
        return item

d = DataTest('zhou')
print(d.name)
print(d['name'])
print()


import re
RE_WORD = re.compile(r'\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # re.findall函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配

    def __getitem__(self, index):
        return self.words[index]


# --
# 定义[]方式设置属性，是设置头部内容，所以如要要设置其他内容，需要内容setxxx，getxxx方法哦
class HttpResponseBase:
    def __setitem__(self, header, value):
        header = self._convert_to_charset(header, 'ascii')
        value = self._convert_to_charset(value, 'latin-1', mime_encode=True)
        self._headers[header.lower()] = (header, value)		# 注意这种存储格式！key的小写：元祖(key, value)

    def __delitem__(self, header):
        self._headers.pop(header.lower(), False)

    def __getitem__(self, header):		# 定义，当访问头部属性找不到的时候，默认取找头的key，很吊是不是！
        return self._headers[header.lower()][1]	# 请看上面的set方法，value是一个元祖，0是key, 1是value