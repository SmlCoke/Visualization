import matplotlib.pyplot as plt

# 设置参数
tau = 2
E = 1

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(6, 4))

# 移动坐标轴到原点
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# 隐藏上、右边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置刻度位置和标签
ax.set_xticks([-tau/2, 0, tau/2])
ax.set_xticklabels([r'$-\tau/2$', '0', r'$\tau/2$'], fontsize=12)
ax.set_yticks([E])
ax.set_yticklabels([r'$E$'], fontsize=12)

# 设置坐标范围
ax.set_xlim(-tau*0.7, tau*0.7)
ax.set_ylim(0, E*1.2)

# 获取当前坐标范围
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()

# 添加箭头（修正位置）
ax.plot(x_min, 0, "<k",    # 左箭头，方向向左
        transform=ax.transData,
        clip_on=False,
        markersize=10)
ax.plot(0, y_max, "^k",    # 上箭头，方向向上
        transform=ax.transData,
        clip_on=False,
        markersize=10)

# 绘制矩形脉冲
ax.plot([-tau/2, tau/2], [E, E], 'k-', lw=2)
ax.vlines([-tau/2, tau/2], 0, E, colors='k', lw=2)

# 显示图形
plt.show()