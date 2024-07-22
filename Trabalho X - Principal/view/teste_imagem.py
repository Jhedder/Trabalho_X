import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Abre a imagem usando PIL (Pillow)
image = Image.open("C:/Users/182400232/Documents/Projetos-Python1/Trabalho X/Imagens/maxresdefault.jpg")

# Converte a imagem PIL para um objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Cria um Label para exibir a imagem
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()