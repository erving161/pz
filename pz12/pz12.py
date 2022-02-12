from tkinter import *
from tkinter import ttk



root = Tk()
root.geometry("1200x800")
root["bg"] = "white"          # Цвет фона окна
root.title("TEST")


Title = Label(text='Регистрация', background="#FFFFFF", foreground="#00BFFF", padx="0", pady="0", font=("Arial", 30))
Title.place(x=10, y=10)
Title2 = Label(text="Создание нового сайта", background="#00BFFF", foreground="white", padx="450", pady="15", font=("Arial", 25))
Title2.place(x=0, y=90)


email_1 = Label(text="Email ", bg='white', fg='#00BFFF', font=('Arial', 16))
email_1.place(x=250, y=205)
email_enter = Entry(bg='#00BFFF', fg='black', font=('Arial', 14))
email_enter.place(x=350, y=205, height=35, width=400)

password_1 = Label(text="Пароль", bg='white', fg='#00BFFF', font=('Arial', 16))
password_1.place(x=250, y=255)
password_1_enter = Entry(bg='#00BFFF', fg='black', font=('Arial', 14))
password_1_enter.place(x=350, y=255, height=35, width=400)


name_1 = Label(text="Имя    ", bg='white', fg='#00BFFF', font=('Arial', 16))
name_1.place(x=250, y=305)
name_1_enter = Entry(bg='#00BFFF', fg='black', font=('Arial', 14))
name_1_enter.place(x=350, y=305, height=35, width=400)


surname_1 = Label(text="Фамилия    ", bg='white', fg='#00BFFF', font=('Arial', 16))
surname_1.place(x=235, y=355)
surname_1_enter = Entry(bg='#00BFFF', fg='black', font=('Arial', 14))
surname_1_enter.place(x=350, y=355, height=35, width=400)


nickname_1 = Label(text="Никнейм", bg='white', fg='#00BFFF', font=('Arial', 16))
nickname_1.place(x=235, y=405)
nickname_1_enter = Entry(bg='#00BFFF', fg='black', font=('Arial', 14))
nickname_1_enter.place(x=350, y=405, height=35, width=400)


datebirth_1 = Label(text="Дата рождения", bg='white', fg='#00BFFF', font=('Arial', 16))
datebirth_1.place(x=165, y=465)

datebirth_2 = Listbox(root, height=3, width=6, bg='#00BFFF')
datebirth_2.place(x=350, y=465)

for i in ('1-10', '11-20', '21-31'):
    datebirth_2.insert(0, i)


datebirth_3 = Listbox(root, height=3, width=19, bg='#00BFFF')
datebirth_3.place(x=400, y=465)

for i in ('Январь-Апрель', 'Май-Август', 'Сентябрь-Декабрь'):
    datebirth_3.insert(0, i)

datebirth_4 = Listbox(root, height=3, width=19, bg='#00BFFF')
datebirth_4.place(x=530, y=465)

for i in ('1900-1940', '1941-1980', '1981-2022'):
    datebirth_4.insert(0, i)


pol = Label(text="Пол", bg='white', fg='#00BFFF', font=('Arial', 16))
pol.place(x=270, y=548)
pol_enter = Checkbutton(text="Мужчина", bg='#00BFFF', fg='black', font=('Arial', 10))
pol_enter.place(x=350, y=550, height=30, width=80)

pol_enter2 = Checkbutton(text="Женщина", bg='#00BFFF', fg='black', font=('Arial', 10))
pol_enter2.place(x=450, y=550, height=30, width=80)


projivanie = Label(text="Место проживания", bg='white', fg='#00BFFF', font=('Arial', 16))
projivanie.place(x=135, y=610)

projivanie_1 = Listbox(root, height=3, width=15, bg='#00BFFF', fg='black')
projivanie_1.place(x=350, y=600)

for i in ('Россия', 'Украина', 'Белорусь'):
    projivanie_1.insert(0, i)



uslovia = Checkbutton(text='Подтверждаю условия пользования uID сообщества', bg='white', fg='grey', font=('Arial', 12))
uslovia.place(x=350, y=700)

registration = Button(text='Регистрация', bg='#00BFFF', fg='white', font=('Arial', 16))
registration.place(x=350, y=750)








root.mainloop()


