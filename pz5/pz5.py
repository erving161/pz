# Cоставить функцию решения задачи: из заданного числа вычли сумму его цифр. #1
# Из результата вновь вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?

def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s



c = int(input("Введите число: "))
k = 0
while c > 0:
    c -= f(c)
    k += 1


print("Через " + str(k) + " действий")
