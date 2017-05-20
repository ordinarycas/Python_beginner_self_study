'''
Python練習文件
Python3 默認就是用 utf-8
'''

#-*- coding: utf-8 -*-

name = input("username:")
age = int(input("age:")) #型態轉換
job = input("job:")
salary = input("salary:")

#字串格式化

info = '''
-------- info of %s --------
Name: %s
Age: %d
Job: %s
Salary: %s
''' %(name,name,age,job,salary)

print(info)
