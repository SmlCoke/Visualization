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
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

x1 = np.linspace(start=-50,stop=50,num=1000)  # 傅里叶变换的频率范围

# 固定左边的符号函数
line1, = axes[0].plot([], [], lw=2,color = 'black')  # 创建空线条对象
axes[0].set_title(r"$G_{\tau}(t)$",fontproperties=S_14)
axes[0].set_xlim(-0.6,0.6)
axes[0].set_ylim(0,5)
axes[0].set_yticks([0,5])
axes[0].set_xlabel(r'$t$',fontproperties=T_12)
axes[0].set_ylabel(r'$f(t)$',fontproperties=T_12)

# 初始化右边的动态指数函数
line2, = axes[1].plot([], [], lw=2,color = 'black')  # 创建空线条对象
axes[1].set_xlim(-50,50)
axes[1].set_ylim(-0.5, 1.5)
axes[1].set_title(r"$F(j\omega)$",fontproperties=S_14)
axes[1].set_yticks([0,1])
axes[1].set_xlabel(r'$\omega$',fontproperties=T_12)
axes[1].set_ylabel(r'$F(j\omega)$',fontproperties=T_12)

# 参数 a 的变化范围（指数级递减）
tau = np.linspace(start=1, stop=0.0001, num=100)  # 从 1 到 0.001



# 添加可变的文本对象（初始空内容）
text_annotation1 = axes[0].text(
    x=0.05,  # 左侧5%位置
    y=0.95,  # 顶部95%位置
    s="",     # 初始无内容
    transform=axes[0].transAxes,  # 使用坐标轴比例坐标系
    fontproperties = T_12,
    color="red",
    weight="bold",
    verticalalignment="top"  # 顶部对齐
)

text_annotation2 = axes[1].text(
    x=0.05,  # 左侧5%位置
    y=0.95,  # 顶部95%位置
    s="",     # 初始无内容
    transform=axes[1].transAxes,  # 使用坐标轴比例坐标系
    fontproperties = T_12,
    color="red",
    weight="bold",
    verticalalignment="top"  # 顶部对齐
)


def init():
    """初始化函数（动画开始时调用）"""
    line1.set_data([], [])
    line2.set_data([], [])
    return line1,line2


def update(tau):
    """更新函数（每一帧调用）"""
    # 计算新的矩形脉冲信号
    x0 = np.linspace(start=-tau/2, stop=tau/2, num=100)  # 矩形脉冲波的时间范围
    y_G = np.full(shape=100,fill_value=1)
    x_l = np.linspace(-10,-tau/2,100)
    x_r = np.linspace(tau/2,10,100)
    y_l = np.full(100,0)
    y_r = np.full(100,0)
    # 更新线条数据
    line1.set_data(np.concatenate((x_l,x0,x_r)), np.concatenate((y_l,1/tau*y_G,y_r)))
    # 更新文本内容（保留3位小数）
    text_annotation1.set_text(rf"$\tau$={tau:.3f}")


    # 计算新的傅里叶变换
    y_S = np.sin(x1*tau/2)/(x1*tau/2)
    line2.set_data(x1,y_S)

    # 更新文本内容（保留3位小数）
    text_annotation2.set_text(rf"$\tau$={tau:.3f}")

    return line1, line2, text_annotation1, text_annotation2  # 返回所有需要更新的对象


# 创建动画对象
ani = FuncAnimation(fig,
                    update,
                    frames=tau,
                    init_func=init,
                    blit=True,  # 优化渲染
                    interval=70)  # 每帧间隔（毫秒）

# 保存为GIF（需要安装pillow库）
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "../../Figure/SS/Gtdelta.gif")
save_path = os.path.normpath(save_path)
ani.save(save_path, writer="pillow")

plt.show()