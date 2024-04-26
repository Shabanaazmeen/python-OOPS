# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:32:43 2024

@author: shaik
"""
n=int(input('enter the numbers')) 
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print('reversed number:',rev)
#rev=0(5689)
#rev=0*10+9
#rev=9*10+8
#rev=98*10+6
#rev= 986*10+5
#9865*10=9865