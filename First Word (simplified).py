# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:54:13 2021

@author: Ring

title: First Word

You are given a string and you have to find its first word.
"""

from string import punctuation, whitespace
def first_word(str):
    to_strip = punctuation + whitespace
    return str.lstrip(to_strip).split(' ', 1)[0].rstrip(to_strip)


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    print(first_word("a word"))
    print(first_word("hi"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    #print("Coding complete? Click 'Check' to earn cool rewards!")
