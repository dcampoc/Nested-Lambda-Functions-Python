# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:43:39 2019

@author: dcamp
"""

x = ['ROCK', 'PAPER']
def caps(li):
    """"Returns a list, with all elements capitalized"""
    def inner(w):
        """Returns a capitalized word"""
        return w.capitalize()
    return ([inner(li[0]), inner(li[1])])

print(caps(x))