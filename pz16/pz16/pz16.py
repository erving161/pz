import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#00BFFF', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="11.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить маршрут ', command=self.open_dialog, bg='#00BFFF',
                                         bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="14.png")
        btn_search = tk.Button(toolbar, text="Поиск маршрута", command=self.open_search_dialog, bg='#00BFFF',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.RIGHT)

        self.update_img = tk.PhotoImage(file="12.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать маршрут", command=self.open_update_dialog,
                                    bg='#00BFFF',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="15.png")
        btn_delete = tk.Button(toolbar, text="Убрать маршрут", command=self.delete_records, bg='#00BFFF',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.RIGHT)

        self.refresh_img = tk.PhotoImage(file="13.png")
        btn_refresh = tk.Button(toolbar, text="Обновить мартшруты", command=self.view_records, bg='#00BFFF',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=(
        'marsh', 'familia', 'data1', 'data2', 'massa'), height=15,
                                 show='headings')

        self.tree.column('marsh', width=120, anchor=tk.CENTER)
        self.tree.column('familia', width=180, anchor=tk.CENTER)
        self.tree.column('data1', width=140, anchor=tk.CENTER)
        self.tree.column('data2', width=140, anchor=tk.CENTER)
        self.tree.column('massa', width=140, anchor=tk.CENTER)

        self.tree.heading('marsh', text='Номер маршрута')
        self.tree.heading('familia', text='Фамилия водителя')
        self.tree.heading('data1', text='Дата отправки')
        self.tree.heading('data2', text='Дата доставки')
        self.tree.heading('massa', text='Масса груза')


        self.tree.pack()

    def records(self, marsh, familia, data1, data2, massa):
        self.db.insert_data(marsh, familia, data1, data2, massa)
        self.view_records()

    def update_record(self, marsh, familia, data1, data2, massa):
        self.db.cur.execute("""UPDATE perevozka SET marsh=?, familia=?, data1=?, data2=?, massa=? WHERE marsh=?""" ,
                            (marsh, familia, data1, data2, massa,
                             self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM perevozka""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM perevozka WHERE marsh=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, massa):
        massa = (massa + "%",)
        self.db.cur.execute("""SELECT * FROM perevozka WHERE massa LIKE ?""", massa)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить маршрут')
        self.geometry('400x270+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер маршрута')
        label_description.place(x=25, y=25)
        self.entry_score1 = ttk.Entry(self)
        self.entry_score1.place(x=170, y=25)

        label_name = tk.Label(self, text='Фамилия водителя')
        label_name.place(x=5, y=50)
        self.entry_name1 = ttk.Entry(self)
        self.entry_name1.place(x=170, y=50)

        label_spec = tk.Label(self, text='Дата отправки')
        label_spec.place(x=35, y=75)
        self.entry_name2 = ttk.Entry(self)
        self.entry_name2.place(x=170, y=75)

        label_lecs = tk.Label(self, text='Дата доставки')
        label_lecs.place(x=35, y=100)
        self.entry_score2 = ttk.Entry(self)
        self.entry_score2.place(x=170, y=100)

        label_score = tk.Label(self, text='Масса груза')
        label_score.place(x=35, y=125)
        self.entry_score3 = ttk.Entry(self)
        self.entry_score3.place(x=170, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=210)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=210)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_score1.get(), self.entry_name1.get(),
                                                                       self.entry_name2.get(), self.entry_score2.get(),
                                                                       self.entry_score3.get()))
        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать маршрут")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=210)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_score1.get(), self.entry_name1.get(),
                                                                       self.entry_name2.get(), self.entry_score2.get(),
                                                                       self.entry_score3.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск маршрута")
        self.geometry("400x140+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск дисциплин, по массе")
        label_search.place(x=5, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=220, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('PZ_16.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS perevozka (
                marsh INTEGER,
                familia TEXT NOT NULL,
                data1 INTEGER,
                data2 INTEGER,
                massa INTEGER
                )""")

    def insert_data(self, marsh, familia, data1, data2, massa):
        self.cur.execute(
            """INSERT INTO perevozka (marsh, familia, data1, data2, massa) VALUES (?, ?, ?, ?, ?)""",
            (marsh, familia, data1, data2, massa))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Грузовые перевозки")
    root.geometry("1000x500+300+200")
    root.resizable(False, False)
    root.mainloop()
