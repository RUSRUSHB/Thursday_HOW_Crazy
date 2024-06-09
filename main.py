import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family='Microsoft YaHei')

def read_data():
    # 读取数据，跳过前8行
    data = pd.read_csv("data/疯狂星期四-抖音关键词搜索指数.csv", skiprows=8)
    # 数据格式如下："2024/05/08","16186"
    # 第一列是日期，第二列是搜索指数
    return data

def extract_thursday_data(data):
    # 提取关键词搜索指数和日期数据
    thursday_keyword_data = data.iloc[:, 1]
    date_data = data.iloc[:, 0]
    datetime_data = pd.to_datetime(date_data)
    # 选择星期四的数据
    thursday_data = data[datetime_data.dt.dayofweek == 3]
    thursday_keyword_data = thursday_data.iloc[:, 1].values
    thursday_days = pd.to_datetime(thursday_data.iloc[:, 0])  # 将日期数据转换为时间戳
    return thursday_keyword_data, thursday_days


if __name__ == '__main__':
    data = read_data()
    thursday_keyword_data, thursday_days = extract_thursday_data(data)
    
    # 绘制直方图
    plt.figure(figsize=(12, 12))
    
    # 绘制原始数据
    plt.subplot(211)
    plt.plot(thursday_days, thursday_keyword_data, marker='o', linestyle='-')
    plt.title("疯狂星期四-抖音关键词搜索指数（星期四的数据）")
    plt.xlabel("日期")
    plt.ylabel("关键词搜索指数")
    plt.xticks(ticks=np.arange(0, len(thursday_days), 10), labels=thursday_days[::10], rotation=45)
    plt.grid(True)
    
    # 提取感兴趣的区域： 2022-06-16 到 2023-12-28
    start_date = pd.to_datetime("2022-06-16")
    end_date = pd.to_datetime("2023-12-28")
    interested_indices = np.where((thursday_days >= start_date) & (thursday_days <= end_date))[0]
    
    # 绘制感兴趣的区域
    plt.subplot(212)
    plt.plot(thursday_days.iloc[interested_indices], thursday_keyword_data[interested_indices], marker='o', linestyle='-')
    plt.title("感兴趣的时间区间")
    plt.xlabel("日期")
    plt.ylabel("关键词搜索指数")
    plt.xticks(rotation=45)
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

    interested_keyword_data = thursday_keyword_data[interested_indices]
    interested_days_data = thursday_days.iloc[interested_indices]

    # 对这一部分的数据进行拟合

    