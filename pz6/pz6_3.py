# Дан список размера N, все элементы которого, кроме последнего, упорядочены по
# Возрастанию. Сделать список упорядоченным, переместив последний элемент на
# Новую позицию.
import random
data_list = []
N = int(input("Ввести кол-во значений списка "))
for i in range(N):
    data_list.append(random.randrange(-100, 100))
data_list.sort()
print(data_list)