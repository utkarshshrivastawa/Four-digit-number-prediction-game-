# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:18:38 2022

@author: utkar
"""

# game using whlie loop 
import random
nump = random.randint(1000,9999)
# print(nump)
n = int(input("enter the 4 digit number :"))
while n!=10:
    num = nump
    cor = 0
    while num%10:
        numc = num%10
        nc = n%10
        num = num//10
        n = n//10
        if numc==nc:
            cor= cor+1
    if cor == 4:
        print("congrates ! you have guessed correct digit")
        break
    else:
        print("%d digit you have correct" %cor)
        n = int(input("Enter the four digit number "))
else:
    print("you have quite the game ")