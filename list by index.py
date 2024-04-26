# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:29:37 2024

@author: shaik
"""

l =input ('enter the list').split()
l=[int(x) for x in l ]
key = int(input('Enter the key: ')) 
found = False

for i in range(len(l)):  # Using len(l) to get the length of the list
    if l[i] == key:
        print(f"key{key}found at index{i}")
        found = True
        break

if found:
    print('It is found')
else:
    print('It is not found')
