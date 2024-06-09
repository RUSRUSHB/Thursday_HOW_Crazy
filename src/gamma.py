import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, kstest


plt.rc("font",family='Microsoft YaHei')
from scipy.stats import norm, kstest, anderson

# 生成符合伽马分布的随机数据
np.random.seed(0)
data = gamma.rvs(a=2, size=1000)

# 绘制数据的直方图
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# 拟合伽马分布到数据上
shape, loc, scale = gamma.fit(data)
x = np.linspace(0, 15, 100)
pdf = gamma.pdf(x, shape, loc, scale)
plt.plot(x, pdf, 'k-', linewidth=2)

# 进行 Kolmogorov-Smirnov 检验
stat, p = kstest(data, 'gamma', args=(shape, loc, scale))
print("K-S 统计量:", stat)
print("p 值:", p)

plt.title('数据与拟合的伽马分布比较')
plt.show()
