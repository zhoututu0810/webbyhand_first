import numpy as np
import pandas as pd
import math
print(math.pi)

# mu = 30
# sigma = 15
# num = 100
# random_data = np.random.normal(mu, sigma, num)
# print(random_data)
# print(np.round(random_data))

print(math.sin(2*math.pi))
# 自定义正选函数
def mysin(x):
    return 30 * math.sin(math.pi/24 * x)

print(mysin(12))

# 正态分布
# https://blog.csdn.net/C2681595858/article/details/88351791?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase


# 概率密度函数
# https://blog.csdn.net/with_still_water/article/details/102493308?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-3-102493308.nonecase
# https://blog.csdn.net/u012370185/article/details/90265670

# https://zuotu.91maths.com/eg/mi.html
std1 = 1 / (30 * math.pow(2 * math.pi, 0.5))    # 定义标准差, 并输入标准差 dealta
mean1 = 12  # 定义均值,并输入均值  junzhi

def fx1(x):
    return 1 / (std1 * pow(2 * math.pi, 0.5)) * np.exp(-((x - mean1) ** 2) / (2 * std1 ** 2))  # 概率密度函数公式
# u是平均值  = 12
print(fx1(12))