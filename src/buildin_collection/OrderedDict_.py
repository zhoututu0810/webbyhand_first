# OrderedDict 有序字典
# 使用OrderedDict会根据放入元素的先后顺序进行排序
# https://www.cnblogs.com/gide/p/6370082.html
# 这个命名元祖namedtuple里面相反的，orderddict里面保存的元祖，namedtuple里面保存的是字典，坑啊
# 方法和字典一样！

import collections

# 初始化
od = collections.OrderedDict()
od['A'] = 1
od['B'] = 2



dd = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
#按key排序
kd = collections.OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
#按照value排序
vd = collections.OrderedDict(sorted(dd.items(),key=lambda t:t[1]))

#输出
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])


import json
print('测试有序字段序列化')  # 还真可以！
print(json.dumps(kd))   # {"apple": 4, "banana": 3, "orange": 2, "pear": 1}
