# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:40:59 2021

Title: Backward String
You should return a given string in reverse order.
逆序输出
@author: Ring
"""

def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    # output: lav