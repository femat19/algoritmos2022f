# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ie7YQK_6yjwYpv2DWuL-X3PMf5FT6RSn
"""

num = int(input("Insira um número"))

u = num // 1 % 10
print(u)
d = num // 10 % 10
print(d) 
c = num // 100 % 10
print(c)
m = num // 1000 % 10
print(m)

nar = (m**3) + (c**3) + (d**3) + (u**3)

if nar == num:
  print("Esse número é narcisista")
else:
  print("Esse número não é narcisista")