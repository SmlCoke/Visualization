import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties # 设置字体
from matplotlib.font_manager import FontProperties
S_14 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 14)  # 宋体
S_12 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 12)  # 宋体

# 生成原始数据：直线 y = 2x + 1 上加一些噪声
np.random.seed(0)
x = np.linspace(-3, 3, 10)
y = 2 * x + 1 + np.random.normal(0, 1, size=x.shape)

# 多项式拟合：使用高阶多项式（9阶）来过拟合数据
coeffs_high_order = np.polyfit(x, y, 9)
poly_high_order = np.poly1d(coeffs_high_order)

# 一次多项式拟合（直线拟合）
coeffs_linear = np.polyfit(x, y, 1)  # 1 表示一次多项式
poly_linear = np.poly1d(coeffs_linear)

# 用于绘图的细化x轴
x_fit = np.linspace(-3, 3, 400)
y_fit_high = poly_high_order(x_fit)
y_fit_linear = poly_linear(x_fit)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))

axes[1].scatter(x = x, y = y, color = "black")
axes[1].plot(x_fit, y_fit_high, color = 'red')
# 设置标题
axes[1].set_title('过拟合', fontproperties=S_14, color = "black")
xlim = axes[1].get_xlim()
ylim = axes[1].get_ylim()

# 绘制拟合直线
axes[0].scatter(x, y, color="black")
axes[0].plot(x_fit, y_fit_linear, color="green")
axes[0].set_title('最佳拟合', fontproperties=S_14, color="black")
axes[0].set_xlim(xlim)
axes[0].set_ylim(ylim)
plt.tight_layout()
plt.savefig("../../Figure/others/overfitting.svg")
plt.show()
