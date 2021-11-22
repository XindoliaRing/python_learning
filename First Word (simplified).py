# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:54:13 2021

@author: Ring

title: First Word - timetest

You are given a string and you have to find its first word.
timetest
"""
from timeit import timeit as t

def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text


def first_word_1(text):
    return text.split(" ")[0]

print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~11.7 ms
print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~6.1 ms
print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~90928.2 ms
print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~5562.9 ms


def first_word_2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text
    
print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~6.3 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~4.7 ms
print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~7.0 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2108.4 ms


def first_word_3(text):
    try:
        index = text.index(" ")
        return text[:index]
    except ValueError:
        return text

print(t('first_word_3(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~5.8 ms
print(t('first_word_3(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~8.5 ms
print(t('first_word_3(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~5.8 ms
print(t('first_word_3(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2005.8 ms


def first_word_4(text):
    index = -1
    for pos, letter in enumerate(text):
        if letter == " ":
            index = pos
            break
    return text[:index] if index != -1 else text
    
print(t('first_word_4(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~13.1 ms
print(t('first_word_4(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~71.1 ms
print(t('first_word_4(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~13.1 ms
print(t('first_word_4(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~788793.7 ms