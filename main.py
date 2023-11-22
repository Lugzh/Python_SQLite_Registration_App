from customtkinter import *
import sqlite3

class Interface(CTk):
    def __init__(self):
        super().__init__()
        self.conne = DateBank()
        self.conne.create()
        set_appearance_mode("dark")
        self.title("Register")
        self.config(padx=10, pady=10)

        self.title_frame = CTkFrame(self)
        self.title_frame.grid(row=0,column = 0,sticky="we",padx=10,pady=10)

        sw_01 = CTkSwitch(self.title_frame, text="dark", onvalue="light", offvalue="dark",
                          command=lambda: [set_appearance_mode(sw_01.get()), sw_01.configure(text=sw_01.get())])
        sw_01.grid(row=0, column=1)

        self.entrance_frame = CTkFrame(self)
        self.entrance_frame.grid(row=1, column = 0,sticky="we",padx=10,pady=10)

        self.exit_frame = (CTkFrame(self))
        self.exit_frame.grid(row=2,column = 0, sticky="we",padx=10,pady=10)

        self.lb_title = CTkLabel(self.title_frame,text="Register",font=("Fira Code",35))
        self.lb_title.grid(row=0,column= 2)

        self.lb_name = CTkLabel(self.entrance_frame, text="Name: ", anchor="e")
        self.lb_name.grid(row=0,column = 0,sticky="we")

        self.lb_email = CTkLabel(self.entrance_frame, text="Email: ", anchor="e")
        self.lb_email.grid(row=1, column=0, sticky="we")

        self.in_name = CTkEntry(self.entrance_frame,placeholder_text="Name")
        self.in_name.grid(row=0, column=1, columnspan=2,pady=3)

        self.in_email = CTkEntry(self.entrance_frame,placeholder_text="Email")
        self.in_email.grid(row=1, column=1, columnspan=2)

        self.bt_save = CTkButton(self.entrance_frame, text="Save", command=lambda: [self.conne.save(self.in_name.get(),self.in_email.get()), self.event_read(),self.in_name.delete(0,END),self.in_email.delete(0,END)])
        self.bt_save.grid(row=1, column=3, sticky="we", padx=5)

        self.lb_search = CTkLabel(self.exit_frame, text="Name: ", anchor="e", )
        self.lb_search.grid(row=0, column=0, sticky="we")

        self.in_search = CTkEntry(self.exit_frame,placeholder_text="Name")
        self.in_search.grid(row=0, column=1)

        self.bt_search = CTkButton(self.exit_frame, text="Search", command=lambda : [self.event_search(self.in_search.get()),self.in_search.delete(0,END)])
        self.bt_search.grid(row=0, column=2, sticky="we", padx=5)

        self.lb_result = CTkLabel(self.exit_frame, text=f"Texting = ", anchor="w")
        self.lb_result.grid(row=2, column=1, sticky="we")
        self.event_read()

        self.bt_delete = CTkButton(self.exit_frame, text="Delete", command=lambda :[self.conne.delete(self.in_search.get()),self.event_read(),self.in_search.delete(0,END)])
        self.bt_delete.grid(row=2, column=2, sticky="we", padx=5, pady=4)

    def event_search(self, valor_buscar):
        self.var_text = ''

        for i in self.conne.search(valor_buscar):
            self.var_text += str(i) + '\n'

        self.lb_result.configure(text=self.var_text)

    def event_read(self):
        self.var_text = []
        self.var_text[:] = "D?"
        for i in self.conne.read():
            self.var_text.append(i)

        self.lb_result.configure(text=self.var_text[-1])


class DateBank():
    def __init__(self):
        self.connect = None
        self.cursor = None
        self.costumers_dates = None

    def create(self):
        self.connect = sqlite3.connect("people.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS costumers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL 
            )
        ''')
        self.connect.commit()
        self.connect.close()

    def save(self,in_name,in_email):
        connect = sqlite3.connect("people.db")
        cursor = connect.cursor()
        cursor.execute('INSERT INTO costumers (name,email) VALUES (?,?)', (in_name, in_email))
        connect.commit()
        connect.close()
        print(self.read())

    def search(self, in_search):
        self.connect = sqlite3.connect("people.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'SELECT * FROM costumers WHERE name="{in_search}"')
        self.costumers_dates = self.cursor.fetchall()
        self.connect.close()
        return self.costumers_dates

    def read(self):
        self.connect = sqlite3.connect('people.db')
        self.cursor = self.connect.execute('''
                   SELECT * FROM costumers
           ''')
        self.costumers_dates = self.cursor.fetchall()

        self.connect.close()

        return self.costumers_dates

    def delete(self,in_search):

        self.connect = sqlite3.connect("people.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute(f'DELETE FROM costumers WHERE name="{in_search}"')

        #lb_exit.configure(text="Data reading: ")
        #for cliente in clientes:
        #    lb_exit.configure(text=f" \n + {cliente} ", font=("Fira Code", 15))
        self.connect.commit()
        self.connect.close()

if __name__ == "__main__":
    App = Interface()
    App.mainloop()