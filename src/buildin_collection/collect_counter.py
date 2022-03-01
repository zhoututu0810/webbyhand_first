import collections

# 计算器
counter = collections.Counter('aabbccc')
print(type(counter.most_common()))      # 返回的居然是列表
print(counter.most_common())


