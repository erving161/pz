# Task 2.
# 2  Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значенияновые значения переменных A и B.
import random
a = random.randrange(1, 99)
b = random.randrange(1, 99)
print(a, b)
if a != b:
    a = b = max(a, b)
else:
    a = b = 0

print('Число А - ', a)
print('Число B - ', b)

