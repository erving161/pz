# PZ - 2

# Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число.

try:
    number = int(input('Введите 3-х значное число: '))
    print("Вы ввеели число: ", number)
    sotni = int(number/100)  # Ищем сотни, единицы, десятки в введеном  числе.
    desyat = int((number-sotni*100)/10)
    edin = number%10
    new_number = str(edin) + str(desyat) + str(sotni)  # Так как мы зачеркиваем число справа и пишем его слева, у нас единицы превращаются в сотни, десятки в единицы и сотни в десятки. Применяю экранирование, перевожу числа в строчку(str) и складываю.
    print('Полученное число - ', new_number)
except ValueError:  # С помощью try, exсept - проверяю что введено действительно число, а не буквы.
    print('это не число')
