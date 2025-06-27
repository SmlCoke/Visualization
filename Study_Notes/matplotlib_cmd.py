# 导入模块
'''
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D 绘制三维曲面时需导入

from matplotlib.font_manager import FontProperties # 设置字体
'''

# 图形正确显示(全局设置)
'''
plt.rc('font', family="SimHei")            # 正确显示中文  (不建议直接使用，推荐精细调控)
plt.rc('font', size=16)                    # 设置字号     (不建议直接使用，推荐精细调控)
plt.rc('axes',unicode_minus = False)       # 正确显示负号
plt.rcParams['text.usetex'] = True         # 调用LaTeX方法渲染文本 (无法兼容中文)
r 前缀表示原始字符串，它告诉Python忽略字符串中的转义字符，如反斜杠 \
'''

# 字体设置(用法需要个性化调整)
'''
from matplotlib.font_manager import FontProperties
S_16 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 16)  # 宋体
K_16 = FontProperties(fname = r'C:\\Windows\\Fonts\\STKAITI.TTF', size = 16) # 楷体
T_16 = FontProperties(fname= r'C:\\Windows\\Fonts\\times.ttf', size = 16)    # Times New Roman
S_14 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 14)  # 宋体
K_14 = FontProperties(fname = r'C:\\Windows\\Fonts\\STKAITI.TTF', size = 14) # 楷体
T_14 = FontProperties(fname= r'C:\\Windows\\Fonts\\times.ttf', size = 14)    # Times New Roman
S_12 = FontProperties(fname = r'C:\\Windows\\Fonts\\simsun.ttc', size = 12)  # 宋体
K_12 = FontProperties(fname = r'C:\\Windows\\Fonts\\STKAITI.TTF', size = 12) # 楷体
T_12 = FontProperties(fname= r'C:\\Windows\\Fonts\\times.ttf', size = 12)    # Times New Roman
'''


# 推荐绘图方法————精确操控子图法
'''
# 创建窗口以及子图集
fig, axes = plt.subplots(nrows=1, ncols=m, figsize=(11, 4))
axes[a]访问第a个子图

fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(11, 4))
axes[a,b]访问第a行第b列个子图

# 子图绘制
axes[a,b].plot(x = , y = , color = , label = , linestyle = , linewidth = , marker = , markersize= , alpha = ,)

# 设置标题
axes[a,b].set_title('标题', fontpreperties=S_16,color = )

# 设置图例
axes[a,b].legend(loc = 'upper left',prop = S_16)

# 调整坐标轴刻度
axes[a,b].set_xlim(-100,100)                 # x方向显示范围
axes[a,b].set_ylim(-1.5,1.5)                 # y方向显示范围
axes[a,b].set_yticks([-1,0,1])               # y轴显示的刻度
axes[a,b].set_xticks([num1, num2, num3,...,num_n], [str1, str2,... str_n]) # 将刻度数值替换为字符串,同时x轴范围变为[num1,num_n]
axes[a,b].set_xlabel(r'$t$',fontproperties=T_12)  # x轴标签
axes[a,b].set_ylabel(r'$f(t)$',fontproperties=T_12)  # y轴标签


# 将刻度转化为百分数
def to_percentage(x, pos):
    return f'{100 * x:.2f}%'
axes[a,b].xaxis.set_major_formatter(FuncFormatter(to_percentage))

'''

# 其他绘图方法：单图绘制——直接使用plt
''' 
# 打开一个新的图形窗口
plt.figure(figsize = (10,8))
或fig = plt.figure()获取窗口名

# 调整布局
plt.tight_layout()

# 子图绘制
plt.plot(x = , y = , color = , label = , linestyle = , linewidth = , marker = , markersize= , alpha = ,)

# 设置标题
plt.title('标题', fontpreperties=S_16,color = )

# 设置图例
plt.legend(loc = 'upper left',prop = S_16)


# 调整坐标轴刻度

plt.xlim(-100,100)                 # x方向显示范围
plt.ylim(-1.5,1.5)                 # y方向显示范围
plt.xticks([num1, num2, num3,...,num_n])  将x轴的刻度显示为数值num1, num2,...同时x轴范围（或者说整个子图x方向的范围）变为num1~num_n
plt.xticks([num1, num2, num3,...,num_n], [str1, str2,... str_n])
显示为刻度大小对应于数值num1, num2,...的刻度
同时x轴范围（或者说整个子图x方向的范围）变为num1~num_n
并且将刻度的符号从num1, num2, ... 修改为字符串str1, str2,...str_n
想要显示的字符串同样支持r'$...$'方法

## y轴刻度旋转45°
ax = plt.gca()
ax.tick_params(axis='y', rotation=45, labelsize=size)  # 单独控制y轴刻度

## 将刻度转化为百分数
def to_percentage(x, pos):
    return f'{100 * x:.2f}%'
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percentage))

# 调整坐标轴标签
plt.xlabel(r'$t$',fontproperties=T_12)  # x轴标签
plt.ylabel(r'$f(t)$',fontproperties=T_12)  # y轴标签
如果需要使用LaTeX渲染文本，那么fontproperties字体设置自动失效，为了控制字体大小，更改命令为：
plt.xlabel(r'$t$',fontsize = size)  # x轴标签
plt.ylabel(r'$f(t)$',fontsize = size)  # y轴标签

## 移动坐标轴标签至y轴上侧，x轴右侧

### x轴标签设置到正右方
ax.xaxis.set_label_coords(1.05, -0.02)  # (x,y) in axes coordinates
ax.set_xlabel(r'$q$', fontsize=18,
             horizontalalignment='left',  # 对齐到定位点的左侧
             verticalalignment='center')

### y轴标签设置到正上方
ax.yaxis.set_label_coords(-0.08, 1.02)  # 微调坐标
ax.set_ylabel(r'$\omega(q)$', fontsize=18,
             rotation=0,                 # 取消自动旋转
             horizontalalignment='right',
             verticalalignment='bottom')


'''


# 保存图片
'''
plt.tight_layout()  # 布局紧凑
plt.savefig('figname.svg')
plt.savefig('figname.pdf')
plt.savefig('figname.png',dpi = 1200)
'''
# 子图的绘制
'''
方式一:
plt.figure()
plt.subplot(abc) : a行b列第c个(c是索引，从1开始)
使用此命令之后，plt自动移至当前子图窗口
获取轴：ax = plt.gca()

方式二:
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(222)
'''




# ax与plt
'''
ax = plt.gca() 用于获取当前的 Axes 对象。
Axes 对象是 matplotlib 中用于绘制图形的核心对象，
它包含了图形的所有元素，如线条、标记、标签、标题等。
ax = plt.gca()
'''


# 三维曲面
'''
除了基础模块matplotlib.pyplot外还需导入：
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (10,8))
x = list
x,y = np.meshgrid(x,x)
ax = fig.add_subplot(111,projection = '3d')
z = func(x,y)
ax.plot_surface(x,y,z,cmap = "viridis" , color = "green",label = "z = func(x,y)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('目标函数')
plt.legend(loc = "upper left" )
'''

# 三维曲线
'''
除了matplotlib.pyplot外不需要额外导入库
plt.subplot(111,projection= '3d')
给出x,y,z的参数方程及参数样本点集(np.linspace(a,b,num))
plt.plot(x,y,z,color = 'green', label = "test")
plt.legend(loc = "upper left" , title = "Test")
'''

