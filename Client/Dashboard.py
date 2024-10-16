import tkinter as tk
from tkinter import Menu
from FrmLogin import FormLogin
from FrmEle import ElektronikApp

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Menu Demo')
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None

        self.root.configure(background='#316879')
        self.root.option_add("*Font", "Helvetica 10")
        self.root.option_add("*Background", "#f0f0f0")
        self.root.option_add("*Foreground", "#000000")

        self.menubar = Menu(self.root, bg='#316879', fg='white', font=('Helvetica', 10))
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0, bg='#f0f0f0', fg='#000000', font=('Helvetica', 10))
        self.file_menu2 = Menu(self.menubar, tearoff=0, bg='#f0f0f0', fg='#000000', font=('Helvetica', 10))

        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu2.add_command(label='Exit', command=self.root.destroy)

        self.menubar.add_cascade(label="Sign In", menu=self.file_menu)
        self.menubar.add_cascade(label="Exit", menu=self.file_menu2)

        self.label_welcome = tk.Label(self.root, text="Selamat Datang di Dashboard,", font=("Helvetica", 24, "bold"), bg='#316879', fg='#f0f0f0')
        self.label_welcome.place(relx=0.5, rely=0.4, anchor='center')
        self.login_level_label = tk.Label(self.root, text="Silahkan Login Untuk Melanjutkan", font=("Helvetica", 24, "bold"), bg='#316879', fg='#f0f0f0')
        self.login_level_label.place(relx=0.5, rely=0.5, anchor='center')

    def new_window(self, title, _class):
        new = tk.Toplevel(self.root)
        new.transient(self.root)
        new.grab_set()
        if _class == FormLogin:
            _class(new, title, self.update_main_window)
        elif _class == ElektronikApp:
            _class(new, "Aplikasi Data Penjualan Elektronik")

    def update_main_window(self, data):
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if loginvalid:
            index = self.file_menu.index('Login')
            self.file_menu.delete(index)
            self.file_menu.entryconfig(index, state='disabled')
            self.file_menu2.entryconfig(index, state='normal')
            self.file_menu2.add_command(label='Logout', command=self.Logout)
            self.login_level_label.config(text=f"Selamat Datang, {level}")

            self.label_welcome.destroy()

            self.menu3 = Menu(self.menubar, tearoff=0, bg='#f0f0f0', fg='#000000', font=('Helvetica', 10))
            self.menu3.add_command(label='Elektronik', command=lambda: self.new_window("Aplikasi Data Elektronik", ElektronikApp))
            self.menubar.add_cascade(label="Aplikasi", menu=self.menu3)

    def Logout(self):
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        
        index_login = self.file_menu.index('Login')
        self.file_menu.entryconfig(index_login, state='normal')
        self.file_menu2.entryconfig(0, state='normal')
        self.file_menu2.delete('Logout')
        self.remove_all_menus()
        self.login_level_label.config(text="Silahkan Login Untuk Melanjutkan")


    def remove_all_menus(self):
        for i in range(len(self.menubar._tclCommands)):
            self.menubar.delete(0) 

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
