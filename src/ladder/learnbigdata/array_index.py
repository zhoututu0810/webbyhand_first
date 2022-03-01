# 要了解布尔索引，首先要了解数组索引
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
print(df1)
print(df1>3)