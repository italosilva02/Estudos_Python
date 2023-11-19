# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 09:14:21 2023

@author: jzk767
"""

def soma(a,b):
    return a + b

def IsPalidromo(string):
    if string == string[::-1]:
        return "É um palidromo"
    else:
        return "Não é palidromo"
    
def divisao(a,b):
    return a / b
        