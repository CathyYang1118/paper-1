# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:06:16 2019

@author: Think
"""
def change(nu):
    if nu == 'A':
        re = 10
    elif nu == 'B':
        re = 11
    elif nu == 'C':
        re = 12
    elif nu == 'D':
        re = 13
    elif nu == 'E':
        re = 14
    elif nu == 'F':
        re = 15
    else:
        re = int(nu)
    return re

while True:
    m = change(input('input m:'))
    n = change(input('input n:'))
    if 1<m and m<=16 and 1<n and n<=16:
        break

while True:
    numm = input('input number:')
    for i in numm:
        cheak = False
        if change(i) >= m:
            print('change',change(i),m,'into',n)
            cheak = True
    if cheak == False:
        break
    
def ChangeIntoDecimal(numm):
    decimal = 0
    for n in range(0,len(numm)):
        used = change(str(numm[n]))
        decimal += used*(m**(len(numm)-n-1))
    print('changed in to deciaml:',decimal)
    return decimal

def ChangeIntoOther(decimal,n):
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=decimal//n
        y=decimal%n
        b.append(y)
        if s==0:
            break
        decimal = s
    b.reverse()
    for i in b:
        print(a[i],end='')
        
ChangeIntoOther(ChangeIntoDecimal(numm),n)