# 1. Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих».
# 2.  Дан переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.


# Task 1.


import random
number_1 = random.randrange(100, 1000)
number_2 = random.randrange(100, 1000)
number_3 = random.randrange(100, 1000)
print('Случайные числа - ', number_1, number_2, number_3)
if number_2 == number_1:
    print('true')
else:
    print('false')
if number_1 == number_3:
    print('true')
else:
    print('false')
if number_2 == number_3:
    print('true')
else:
    print('false')


# Task 2.
# 2  Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значенияновые значения переменных A и B.

a = random.randrange(1, 99)
b = random.randrange(1, 99)
print(a, b)
if a != b:
    a = b = max(a, b)
else:
    a = b = 0

print('Число А - ', a)
print('Число B - ', b)

