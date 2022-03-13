#Составить генератор (yield), который преобразует все буквенные символы в заглавные.





def str_to_upper(crs: str):
    for ch in crs:
        yield ch.upper()


user_str = input("Введите буквы нижнего регистра ")
print(''.join(str_to_upper(user_str)))
