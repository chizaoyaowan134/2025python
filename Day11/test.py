# 作者: 段鼎肯
# 2025年01月09日01时46分16秒
# xxx@qq.com

import numpy as np

t = np.arange(24).reshape(4, 6)
print(t)
print(id(t))
print('-' * 50)

# # 修改多个不相邻的点
t[[0, 1], [1, 3]] = 0
print(t)
print("-" * 50)
# # 修改多行多列，取第二行到第四行，第三列到第五列
t[1:3, 2:5] = 0
print(t)
