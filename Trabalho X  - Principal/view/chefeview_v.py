import tkinter as tk
from PIL import Image, ImageTk
class ChefeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.pack(fill=tk.BOTH, expand=True)
        min_width, min_height = 600, 800
        parent.minsize(min_width, min_height)
        canvas = tk.Canvas(parent, width=min_width, height=min_height)
        canvas.pack(fill=tk.BOTH, expand=True)
        #self.create_gradient_background(canvas,min_width,min_height)
        self.create_widgets()

    def create_widgets(self):
        # Criar a janela principal
        self.parent.title("Burn Dinorex - Mega Man X5")
        self.parent.resizable(False, False)

        # Aumentar o tamanho mínimo da janela
        min_width, min_height = 600, 800
        self.parent.minsize(min_width, min_height)

        # Criar um canvas para o fundo com gradiente
        canvas = tk.Canvas(self, width=min_width, height=min_height)
        canvas.pack(fill=tk.BOTH, expand=True)


        # Carregar e redimensionar a imagem do Magma Dragoon
        self.image_path = "Trabalho X  - Principal\midia\imagens\BurnDinorex.jpg" 
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)

        # Criar um label para exibir a imagem
        image_label = tk.Label(self, image=photo, bg='#8B0000')  # Fundo vermelho escuro para o label da imagem
        image_label.place(x=100, y=100)  # Posição relativa ao canvas

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
        text_label = tk.Label(self, text=info_text, justify=tk.LEFT, padx=10, pady=10, bg='#8B0000', fg='white',
        font=('Helvetica', 12))  # Fundo vermelho escuro e texto branco
        text_label.place(x=25, y=520)  # Posição relativa ao canvas

        # Criar um botão para atualizar a imagem
        self.escolher_button = tk.Button(self, text="Atualizar Chefe")
        self.escolher_button.place(x=250, y=700)  # Posição relativa ao canvas

        # Centralizar a janela na tela
        #self.center_window(self, min_width, min_height)

        # Rodar o loop principal
       
