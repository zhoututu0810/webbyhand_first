# 流对象都有一个指针，当读取了一遍流，指针就移动了，如果不人工重置指针，指针移动到文件末尾
# 再次读取温酒就读取不出来内容了，证明如下

fp = open('test.txt', mode='rt', encoding='utf-8')
print(fp.readlines())   # ['fafdasdf\n', 'dfasdf\n', '211221\n', '33123\n', '\n']
print(fp.readlines())   # []
fp.close()
