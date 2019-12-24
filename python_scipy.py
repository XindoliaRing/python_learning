# -*- coding: utf-8 -*
# 1. 求解非线性方程组2x1-x2^2=1, x1^2-x2=2
from scipy.optimize import fsolve # 导入求解方程组的函数
# 定义要求解的方程组
def f(x):
  x1 = x[0]
  x2 = x[1]
  return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]

result = fsolve(f, [1, 1]) # 输入初值[1, 1]并进行求解
print(result) # 输出结果

# 2.数值积分
from scipy import integrate # 导入积分函数
# 定义被积函数
def g(x):
  return (1-x**2)**0.5

pi_2, err = integrate.quad(g, -1, 1) # 积分结果和误差
print(pi_2 * 2) # 由微积分知识知道积分结果为圆周率pi的一半

