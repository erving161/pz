# На трех участках выращиваются следующие сельскохозяйственные культуры: картофель,
# Лук, морковь, горох, капуста, редис. Определить, какие из этих культур имеются на каждом
# Участке, имеются хотя бы на одном из участков и не имеются ни на одном участке.
import random
kultures = ['onion', 'potato', 'carrot', 'peas', 'cabbage', 'radish']

list_2 = set()
while len(list_2) != 3:
    list_2.add(kultures[random.randint(0, len(kultures) - 1)])
print(list_2)










