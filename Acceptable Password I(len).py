# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:05:54 2021

Title: Acceptable Password I
You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.
In this mission, you need to create a password verification function.
The verification condition is: the length should be bigger than 6.

@author: Ring
"""

def is_acceptable_password(password: str) -> bool:
    return bool(password[7::])
'''
# 1
def is_acceptable_password(password: str) -> bool:
    strlen = len(password)
    if strlen > 6: return True
    else return False
    
# 2(code better then 1, but still have some probloms)
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6
# This code accepts space for the password.
# print(is_acceptable_password('       ')) -> True

# 3
def is_acceptable_password(password: str) -> bool:
    return bool(password[7::])


'''

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('       '))
    print(is_acceptable_password('short'))
    print(is_acceptable_password('muchlonger'))
    print(is_acceptable_password('ashort'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    #print("Coding complete? Click 'Check' to earn cool rewards!")
    
