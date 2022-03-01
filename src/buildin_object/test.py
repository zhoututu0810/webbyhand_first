results = {}

# 子生成器
# 接收成绩，并计算处平均值，并返回给委托生成器
def average():
    print('enter average')
    total = 0.0
    count = 0
    average = 0
    while True:
        score = yield average
        if score is None:
            break
        total += score
        count += 1
        average = total/count

    return average

# 委托生成器
# 从子生成器获取一个学生的平均成绩，并赋值给结果字典
def count_one(name):
    while True:
        print('enter count_one')
        # yeild from 会接受子生成器的返回结果和异常结果，如果是yield结果，就会调用yield 结果，直接返回到调用者了
        # 如果返回的stop异常，那么会捕获该异常，然后类似调用send（异常值）一样，神奇！
        results[name] = yield from average()
        print('exit count_one')
        print(results)

if __name__ == '__main__':results = {}

# 子生成器
# 接收成绩，并计算处平均值，并返回给委托生成器
def average():
    print('enter average')
    total = 0.0
    count = 0
    average = None
    while True:
        score = yield average
        if score is None:
            break
        total += score
        count += 1
        average = total/count

    return average

# 委托生成器
# 从子生成器获取一个学生的平均成绩，并赋值给结果字典
def count_one(name):
    while True:
        print('inter')
        results[name] = yield from average()
        print('exit')
        print(results)

if __name__ == '__main__':
    # 主函数作为调用方
    # data中保存的是三个学生的成绩
    # 这里的目的是要分别计算处每个学生的平均成绩
    # 最终的结果保存在results字典中，同样以名字为键，平均成绩为值
    data = {
        'zhangsan':[80, 90, 60],
        'lisi': [50, 70, 90],
        'wangwu':[60, 30, 60],
    }

    # 针对每个学生都创建一个生成器，并传入name作为最终结果的键
    for name, score in data.items():
        co = count_one(name)
        # 发送None预激生成器，并将该学生的每门成绩发送给生成器
        print(co.send(None))
        for v in score:
            print(co.send(v))
        co.send(None)
    print(results)
