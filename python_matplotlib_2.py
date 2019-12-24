### 1、创建三维坐标轴对象Axes3D ###

#方法一，利用关键字
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')
#ax = fig.add_subplot(111,projection='3d') #这种方法也可以画多个子图

#方法二，利用三维轴方法
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D#定义图像和三维格式坐标轴
fig=plt.figure()
ax2 = Axes3D(fig)

### 2、3D曲线和散点随后在定义的坐标轴上画图 ###

import numpy as np
z = np.linspace( 0, 13, 1000)
x = 5*np.sin(z)
y = 5*np.cos(z)
zd = 13*np.random.random( 100)
xd = 5*np.sin(zd)
yd = 5*np.cos(zd)
ax1.scatter3D(xd,yd,zd, cmap= 'Blues') #绘制散点图
ax1.plot3D(x,y,z, 'gray') #绘制空间曲线
plt.show()

### 3、3D曲面 ###

fig = plt.figure() #定义新的三维坐标轴
ax3 = plt.axes(projection= '3d')
#定义三维数据
xx = np.arange(- 10, 10, 100)
yy = np.arange(- 10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+np.cos(Y)
#作图
ax3.plot_surface(X,Y,Z,cmap= 'rainbow')
#ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow) #等高线图，要设置offset，为Z的最小值
plt.show()
ax3.plot_surface(X,Y,Z,rstride = 1, cstride = 1,cmap='rainbow')
# 其中的row和cloum_stride为横竖方向的步长

### 4、等高线 ###
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#定义坐标轴
fig4 = plt.figure()
ax4 = plt.axes(projection= '3d')
#生成三维数据
xx = np.arange(- 5, 5, 0.1)
yy = np.arange(- 5, 5, 0.1)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X** 2+Y** 2))
#作图
ax4.plot_surface(X,Y,Z,alpha= 0.3,cmap= 'winter') #生成表面， alpha 用于控制透明度
ax4.contour(X,Y,Z, zdir = 'z', offset=- 3, cmap= "rainbow") #生成z方向投影，投到x-y平面
ax4.contour(X,Y,Z, zdir = 'x', offset=- 6, cmap= "rainbow") #生成x方向投影，投到y-z平面
ax4.contour(X,Y,Z, zdir = 'y', offset= 6, cmap= "rainbow") #生成y方向投影，投到x-z平面
#ax4.contourf(X,Y,Z,zdir='y', offset=6,cmap="rainbow") #生成y方向投影填充，投到x-z平面，contourf()函数
#设定显示范围
ax4.set_xlabel( 'X')
ax4.set_xlim(- 6, 4) #拉开坐标轴范围显示投影
ax4.set_ylabel( 'Y')
ax4.set_ylim(- 4, 6)
ax4.set_zlabel( 'Z')
ax4.set_zlim(- 3, 3)
plt.show()

### 5、随机散点图 ###
#可以利用scatter()生成各种不同大小，颜色的散点图，其参数如下：
#函数定义
# matplotlib.pyplot.scatter(x, y,
# s= None, #散点的大小 array scalar
# c= None, #颜色序列 array、sequency
# marker= None, #点的样式
# cmap= None, #colormap 颜色样式
# norm= None, #归一化 归一化的颜色camp
# vmin= None, vmax= None, #对应上面的归一化范围
# alpha= None, #透明度
# linewidths= None, #线宽
# verts= None, #
# edgecolors= None, #边缘颜色
# data= None,
# **kwargs
# )

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#定义坐标轴
fig4 = plt.figure()
ax4 = plt.axes(projection= '3d')
#生成三维数据
xx = np.random.random( 20)* 10- 5#取100个随机数，范围在5~5之间
yy = np.random.random( 20)* 10- 5
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X** 2+Y** 2))
#作图
ax4.scatter(X,Y,Z,alpha= 0.3,c=np.random.random( 400),s=np.random.randint( 10, 20, size=( 20, 40))) #生成散点.利用c控制颜色序列,s控制大小
#设定显示范围
plt.show()

### 6、3D表面形状的绘制  ###

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot( 111, projection= '3d')
# Make data
u = np.linspace( 0, 2* np.pi, 100)
v = np.linspace( 0, np.pi, 100)
x = 10* np.outer(np.cos(u), np.sin(v))
y = 10* np.outer(np.sin(u), np.sin(v))
z = 10* np.outer(np.ones(np.size(u)), np.cos(v))
# Plot the surface
ax.plot_surface(x, y, z, color= 'b')
plt.show()