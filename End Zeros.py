# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:59:16 2021

Title: End Zeros
Try to find out how many zeros a given number has at the end.

@author: Ring
"""

def end_zeros(num: int) -> int:
    t = 0
    n = str(num)
    for x in n[::-1]:
        if x == '0':
            t += 1
        else:
            num = int(x)
            break
    return t


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    print(end_zeros(1))
    print(end_zeros(10))
    print(end_zeros(101))
    print(end_zeros(245))
    print(end_zeros(1900100))

'''
# 1
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))

# 2
def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if  x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))

# 3
def end_zeros(num: int) -> int:
    if num == 0:
        return 1
    
    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros

# 4
def end_zeros(b):
    if b==0:
        return 1
    for i in np.arange(1,len(str(b))+1):
        if float(b/(10**i)).is_integer()==False:
            break
    return i-1
'''