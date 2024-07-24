import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AtualizaView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        

    def create_widgets(self):
        self.id_label = ttk.Label(self, text="ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=5)

        self.id_entry = ttk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.atualizar_button = ttk.Button(self, text="Atualizar Chefe")
        self.atualizar_button.grid(row=1, column=0, pady=10, padx=10)

        self.chefes_listbox = tk.Listbox(self)
        self.chefes_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def get_id(self):
        id = self.id_entry.get()
        return id

    def adicionar_chefe_lista(self, chefe):
        self.chefes_listbox.insert(tk.END, f"id {chefe[0]} | nome  {chefe[1]} | fase  {chefe[2]} | poder  {chefe[3]} |")
    def show_info(self):
        messagebox.showinfo("Os campos não podem estar vazios e o id deve ser digito.")