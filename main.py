import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rc("font",family='Microsoft YaHei')
from scipy.stats import norm, kstest, anderson

def _plot_data(data, date_data, title):
    plt.plot(date_data, data, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('日期')
    plt.ylabel('关键词搜索指数')
    plt.xticks(rotation=45)
    plt.gca().set_xticks(date_data.index[::100])
    plt.grid(True)
    plt.tight_layout()
    pass

# 读取数据
data = pd.read_csv("data/疯狂星期四-抖音关键词搜索指数.csv", skiprows=8) # 跳过前8行
print(data)

keyword_data = data.iloc[:, 2]
date_data = data.iloc[:, 0]
datetime_data = pd.to_datetime(date_data)

# plt.figure(figsize=(15, 6))
plt.figure()
# plt.subplot(121)
# _plot_data(keyword_data, date_data, '原始关键词搜索指数')

# 进行平滑化处理
import scipy.ndimage as nd
keyword_data_smooth = nd.gaussian_filter1d(keyword_data, sigma=4)
# plt.subplot(122)
_plot_data(keyword_data_smooth, date_data, '平滑化后的关键词搜索指数')
plt.show()