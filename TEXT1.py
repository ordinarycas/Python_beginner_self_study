'''
Python練習文件
Python3 默認就是用 utf-8
'''

#-*- coding: utf-8 -*-

import getpass

age_of_ironman = 35

guess_age = int(input("guess age:"))

if guess_age == age_of_ironman:
    print("Bingo, You got it!!!")
elif guess_age > age_of_ironman:
    print("You may think smaller...")
else:
    print("You may think bigger...") 
