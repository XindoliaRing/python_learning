from __future__ import print_function
# -*- coding: utf-8 -*
import numpy as np 
a = np.array([2, 0, 1, 5])
print(a) # 打印数组
print(a[:3]) # 切片，输出前三个元素
print(a.max())
a.sort()
print(a)
b = np.array([[1,2,3], [4,5,6]])
print(b * b)

### 随机散点图 ###
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