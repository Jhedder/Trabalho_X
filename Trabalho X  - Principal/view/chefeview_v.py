import tkinter as tk
from PIL import Image, ImageTk

class ChefeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        min_width, min_height = 600, 800
        parent.minsize(min_width, min_height)
        self.canvas = tk.Canvas(self, width=min_width, height=min_height,background="yellow")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Criar a janela principal
        self.parent.title("Burn Dinorex - Mega Man X5")
        self.parent.resizable(False, False)

        # Aumentar o tamanho mínimo da janela
        min_width, min_height = 600, 800
        self.parent.minsize(min_width, min_height)

        # Criar um canvas para o fundo com gradiente
        self.canvas = tk.Canvas(self, width=min_width, height=min_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Caminho inicial da imagem
        self.image_path = "Trabalho X  - Principal/midia/imagens/BurnDinorex.jpg"
        self.photo = None
        self.image_label = tk.Label(self, bg='#8B0000')
        self.image_label.place(x=100, y=100)

        self.update_image()

        # Texto com informações sobre o Magma Dragoon
        info_text = """
        Burn Dinorex (バーン・ディノレックスBān Dinorekkusu ) , também
        conhecido como Mattrex , [2] é um Reploid de Mega Man X5 baseado em
        um Tiranossauro . Ele possui um motor de propulsão de foguete
        necessário para o ônibus espacial . Ele era um membro da equipe de
        prevenção de desastres da Repliforce e está entre os sobreviventes do
        incidente da Repliforce em Mega Man X4 .
        """

        # Criar um label para exibir o texto
        self.text_label = tk.Label(self, text=info_text, justify=tk.LEFT, padx=10, pady=10, bg='#8B0000', fg='white',
                              font=('Helvetica', 12))
        self.text_label.place(x=25, y=520)

        # Criar um botão para atualizar a imagem
        self.escolher_button = tk.Button(self, text="Atualizar Chefe")
        self.escolher_button.place(x=250, y=700)

    def update_image(self):
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((400, 400))
        self.photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=self.photo)