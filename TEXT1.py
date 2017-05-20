'''
Python練習文件
Python3 默認就是用 utf-8
'''

#-*- coding: utf-8 -*-
#while,for回圈

import os

cmd_rea = os.popen("dir d:\ /p /w /o:D").read()
print("----->",cmd_rea)

'''
age_of_ironman = 35
count = 0

for i in range(0,10,2):
    print("loop-: ",i)

while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_ironman:
        print("Bingo, You got it!!!")
        break
    elif guess_age > age_of_ironman:
        print("You may think smaller...")
    else:
        print("You may think bigger...")
    count +=1
    if count == 3:
        countine_confirm = input("Do you want to keep go in ? (y/n)")
        if countine_confirm != 'n':
            count = 0
'''
