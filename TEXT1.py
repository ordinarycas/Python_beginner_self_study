'''
Python練習文件
Python3 默認就是用 utf-8
'''

#-*- coding: utf-8 -*-
#while回圈

age_of_ironman = 35
count = 0

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
else:
    #當count不為真會執行下面這行
    print("You have tried too many, exit")