import tkinter as tk
from tkinter import messagebox
from Users import Users

class FormLogin:
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window 
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        self.parent.title("Login Page")
        self.parent.geometry("500x250")
        self.parent.config(bg="#d95d54")

        self.heading_label = tk.Label(self.parent, text="Login", font=("Helvetica", 24, "bold"), bg="#d95d54", fg="#ffffff")
        self.heading_label.place(x=220, y=20)

        tk.Label(self.parent, text="Email:", font=("Arial", 14), bg="#d95d54", fg="#f0f0f0").place(x=50, y=80)
        self.email_entry = tk.Entry(self.parent, font=("Arial", 12))
        self.email_entry.place(x=180, y=80, width=250)

        tk.Label(self.parent, text="Password:", font=("Arial", 14), bg="#d95d54", fg="#f0f0f0").place(x=50, y=120)
        self.password_entry = tk.Entry(self.parent, font=("Arial", 12), show="*")
        self.password_entry.place(x=180, y=120, width=250)

        login_button = tk.Button(self.parent, text="Login", command=self.onSubmit, font=("Arial", 14), bd=0, cursor="hand2", bg="#ff7e5f", fg="white")
        login_button.place(x=180, y=170, width=120)
      
    def onSubmit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
                
        obj = Users()
        val = obj.Validasi(email, password)
        C = val[1]
        if C:
            self.update_main_window(val)
            self.parent.destroy()
        else:
            messagebox.showwarning("showwarning", "Login Gagal ")

   
    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print()

    root = tk.Tk()
    aplikasi = FormLogin(root, "Aplikasi Data Login", update_main_window)
    root.mainloop()
