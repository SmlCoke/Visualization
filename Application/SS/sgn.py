import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties
S_16 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 16)  # 宋体
S_14 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 14)  # 宋体
S_12 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 12)  # 宋体
T_12 = FontProperties(fname= r'C:\\Windows\\Fonts\\times.ttf', size = 12)

# 初始化画布和子图
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))
x = np.linspace(start=-100, stop=100, num=200)

# 固定左边的符号函数
y_sgn1 = np.full(shape=100, fill_value=-1)
y_sgn2 = np.full(shape=100, fill_value=1)
y_sgn = np.concatenate((y_sgn1, y_sgn2))
axes[0].plot(x, y_sgn,color = 'black')
axes[0].set_title("符号函数",fontproperties=S_14)
axes[0].set_xlim(-100,100)
axes[0].set_ylim(-1.5,1.5)
axes[0].set_yticks([-1,0,1])
axes[0].set_xlabel(r'$t$',fontproperties=T_12)
axes[0].set_ylabel(r'$f(t)$',fontproperties=T_12)

# 初始化右边的动态指数函数
line, = axes[1].plot([], [], lw=2,color = 'black')  # 创建空线条对象
axes[1].set_xlim(-100, 100)
axes[1].set_ylim(-1.5, 1.5)
axes[1].set_title("双边指数信号",fontproperties=S_14)
axes[1].set_yticks([-1,0,1])
axes[1].set_xlabel(r'$t$',fontproperties=T_12)
axes[1].set_ylabel(r'$f(t)$',fontproperties=T_12)

# 参数 a 的变化范围（指数级递减）
a_values = np.logspace(0, -5, num=100)  # 从 1 到 0.001



# 添加可变的文本对象（初始空内容）
text_annotation = axes[1].text(
    x=0.05,  # 左侧5%位置
    y=0.95,  # 顶部95%位置
    s="",     # 初始无内容
    transform=axes[1].transAxes,  # 使用坐标轴比例坐标系
    fontproperties = S_12,
    color="red",
    weight="bold",
    verticalalignment="top"  # 顶部对齐
)

def init():
    """初始化函数（动画开始时调用）"""
    line.set_data([], [])
    return line,


def update(a):
    """更新函数（每一帧调用）"""
    # 计算新的指数函数
    y_e1 = -np.exp(a * x[0:100])
    y_e2 = np.exp(-a * x[100:200])
    y_e = np.concatenate((y_e1, y_e2))

    # 更新线条数据
    line.set_data(x, y_e)
    # 更新文本内容（保留3位小数）
    text_annotation.set_text(f"当前α值: {a:.3f}")

    return line, text_annotation  # 返回所有需要更新的对象


# 创建动画对象
ani = FuncAnimation(fig,
                    update,
                    frames=a_values,
                    init_func=init,
                    blit=True,  # 优化渲染
                    interval=70)  # 每帧间隔（毫秒）

# 保存为GIF（需要安装pillow库）
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "../../Figure/SS/dynamic_plot.gif")
save_path = os.path.normpath(save_path)

ani.save(save_path, writer="pillow")

plt.show()