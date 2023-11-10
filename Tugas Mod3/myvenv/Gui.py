
import tkinter as tk
import socket

def nslookup():
    domain = domain_entry.get()
    try:
        ipaddress = socket.gethostbyname(domain)
        result_label.config(text=f"Nama Domain: {domain}\nAlamat IP: {ipaddress}")
    except socket.gaierror:
        result_label.config(text="Domain tidak ditemukan")

#membuat jendela utama
root = tk.Tk()
root.title("App NSLookup")

#menambahkan perintah untuk mengatur jendela
root.geometry("400x200")#ukuran disesuaikan (lebarxtinggi)

#label dan input
domain_label = tk.Label(root, text="Masukan Domain: ")
domain_label.pack(pady=10)

domain_entry = tk.Entry(root)
domain_entry.pack()

#tombol untuk melakukan nslookup
lookup_button = tk.Button(root, text="NslookUp", command=nslookup)
lookup_button.pack(pady=10)

#hasil
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()