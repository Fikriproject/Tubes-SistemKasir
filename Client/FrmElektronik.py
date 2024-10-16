import tkinter as tk
from tkinter import Frame, Label, Entry, Button, ttk, END, StringVar, messagebox
from tkinter.constants import NO, CENTER
from ttkthemes import ThemedTk
import json
from elektronik import elektronik

class ElektronikApp:
    def __init__(self, root, title):
        self.root = root
        self.root.geometry("990x600")
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ob = elektronik()
        self.ditemukan = False
        column_widths = {
            'ID': 50,
            'KD Pelanggan': 100,
            'Nama Pelanggan': 150,
            'KD Barang': 100,
            'Barang': 150,
            'Harga': 100,
            'Banyaknya': 100,
            'Pembayaran': 100,
            'Status': 100,
        }
        self.column_widths = column_widths
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.root, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)

        Label(mainFrame, text='Kode Pelanggan:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtkdpelanggan = Entry(mainFrame)
        self.txtkdpelanggan.grid(row=0, column=1, padx=5, pady=5)
        self.txtkdpelanggan.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama Pelanggan:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtnama_pelanggan = Entry(mainFrame)
        self.txtnama_pelanggan.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Kode Barang:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtkdbarang = Entry(mainFrame)
        self.txtkdbarang.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Nama Barang:').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtbarang = Entry(mainFrame)
        self.txtbarang.grid(row=3, column=1, padx=5, pady=5)

        Label(mainFrame, text='Harga:').grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtharga = Entry(mainFrame)
        self.txtharga.grid(row=4, column=1, padx=5, pady=5)

        Label(mainFrame, text='Banyaknya:').grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtbanyaknya = Entry(mainFrame)
        self.txtbanyaknya.grid(row=5, column=1, padx=5, pady=5)

        Label(mainFrame, text='Pembayaran:').grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtpembayaran = StringVar()
        CboPembayaran = ttk.Combobox(mainFrame, width=27, textvariable=self.txtpembayaran)
        CboPembayaran.grid(row=6, column=1, padx=5, pady=5)
        CboPembayaran['values'] = ('Cash', 'Credit')
        CboPembayaran.set('')

        Label(mainFrame, text='Status:').grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtstatus = StringVar()
        CboStatus = ttk.Combobox(mainFrame, width=27, textvariable=self.txtstatus)
        CboStatus.grid(row=7, column=1, padx=5, pady=5)
        CboStatus['values'] = ('Lunas', 'Cicilan')
        CboStatus.set('')

        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='green', fg='white')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='blue', fg='white')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='red', fg='white')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, bg='orange', fg='white')
        self.btnCari.grid(row=3, column=3, padx=5, pady=5)

        columns = ('ID', 'KD Pelanggan', 'Nama Pelanggan', 'KD Barang', 'Barang', 'Harga', 'Banyaknya', 'Pembayaran', 'Status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=NO, width=self.column_widths.get(col, 100), anchor=CENTER)
        self.tree.grid(row=9, column=0, columnspan=4, padx=10, pady=10)


    def onClear(self, event=None):
        self.txtkdpelanggan.delete(0, END)
        self.txtnama_pelanggan.delete(0, END)
        self.txtkdbarang.delete(0, END)
        self.txtbarang.delete(0, END)
        self.txtharga.delete(0, END)
        self.txtbanyaknya.delete(0, END)
        self.txtpembayaran.set("")
        self.txtstatus.set("")
        self.btnSimpan.config(text="Simpan")
        self.ditemukan = False
        self.onReload()

    def onReload(self, event=None):
        result = self.ob.getAllData()
        if result:
            try:
                parsed_data = json.loads(result)
                self.tree.delete(*self.tree.get_children())
                for i, d in enumerate(parsed_data):
                    self.tree.insert("", 'end', values=(d["id"], d["kdpelanggan"], d["nama_pelanggan"], d["kdbarang"], d["barang"], d["harga"], d["banyaknya"], d["pembayaran"], d["status"]))
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Failed to parse JSON response: {e}")
        else:
            messagebox.showerror("Error", "Empty response from server")


    def onCari(self, event=None):
        kdpelanggan = self.txtkdpelanggan.get()
        obt = self.ob.getBykdpelanggan(kdpelanggan)
        if obt and isinstance(obt, list) and len(obt) > 0:
            self.TampilkanData(obt[0])  # Access the first element of the list
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("Info", "Data Tidak Ditemukan")

    def TampilkanData(self, obt):
        self.txtkdpelanggan.delete(0, END)
        self.txtkdpelanggan.insert(END, obt['kdpelanggan'])
        self.txtnama_pelanggan.delete(0, END)
        self.txtnama_pelanggan.insert(END, obt['nama_pelanggan'])
        self.txtkdbarang.delete(0, END)
        self.txtkdbarang.insert(END, obt['kdbarang'])
        self.txtbarang.delete(0, END)
        self.txtbarang.insert(END, obt['barang'])
        self.txtharga.delete(0, END)
        self.txtharga.insert(END, obt['harga'])
        self.txtbanyaknya.delete(0, END)
        self.txtbanyaknya.insert(END, obt['banyaknya'])
        self.txtpembayaran.set(obt['pembayaran'])
        self.txtstatus.set(obt['status'])
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kdpelanggan = self.txtkdpelanggan.get()
        nama_pelanggan = self.txtnama_pelanggan.get()
        kdbarang = self.txtkdbarang.get()
        barang = self.txtbarang.get()
        harga = self.txtharga.get()
        banyaknya = self.txtbanyaknya.get()
        pembayaran = self.txtpembayaran.get()
        status = self.txtstatus.get()

        obt = elektronik()
        obt.kdpelanggan = kdpelanggan
        obt.nama_pelanggan = nama_pelanggan
        obt.kdbarang = kdbarang
        obt.barang = barang
        obt.harga = harga
        obt.banyaknya = banyaknya
        obt.pembayaran = pembayaran
        obt.status = status

        if not self.ditemukan:
            res = obt.simpan()
        else:
            res = obt.updateBykdpelanggan(kdpelanggan)

        if res:
            try:
                data = json.loads(res)
                status = data["status"]
                msg = data["message"]
                messagebox.showinfo("Info", f"{status}, {msg}")
                self.onClear()
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Failed to parse JSON response: {e}")
        else:
            messagebox.showerror("Error", "No response from server")


    def onDelete(self, event=None):
        kdpelanggan = self.txtkdpelanggan.get()
        obt = elektronik()
        obt.kdpelanggan = kdpelanggan

        if self.ditemukan:
            res = obt.deleteBykdpelanggan(kdpelanggan)
            try:
                data = json.loads(res)
                status = data["status"]
                msg = data["message"]
                messagebox.showinfo("Info", f"{status}, {msg}")
                self.onClear()
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to parse JSON response")
        else:
            messagebox.showinfo("Info", "Data harus ditemukan dulu sebelum dihapus")

    def onKeluar(self, event=None):
        self.root.destroy()

if __name__ == '__main__':
    root = ThemedTk(theme="plastik")
    aplikasi = ElektronikApp(root, "Aplikasi Data Elektronik")
    root.mainloop()
