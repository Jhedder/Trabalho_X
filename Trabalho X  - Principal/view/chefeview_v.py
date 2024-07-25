import tkinter as tk
from PIL import Image, ImageTk

class ChefeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.pack(fill=tk.BOTH, expand=True)
        min_width, min_height = 600, 800
        parent.minsize(min_width, min_height)
        # Criar um canvas para o fundo com gradiente
        canvas = tk.Canvas(parent, width=min_width, height=min_height)
        canvas.pack(fill=tk.BOTH, expand=True)
        self.create_gradient_background(canvas,min_width,min_height)
        #self.center_window(self.master,min_width,min_height)
        self.atualizar_imagem()
        self.create_widgets()
    def create_gradient_background(self,canvas, width, height):
        # Definir cores para o gradiente
        color1 = '#FF6347'  # Tomato
        color2 = '#8B0000'  # DarkRed

        # Criar gradiente vertical no canvas
        num_rectangles = 100
        for i in range(num_rectangles):
            # Interpolar entre color1 e color2
            color = '#{:02x}{:02x}{:02x}'.format(
                int((num_rectangles - i) * int(color1[1:3], 16) + i * int(color2[1:3], 16)) // num_rectangles,
                int((num_rectangles - i) * int(color1[3:5], 16) + i * int(color2[3:5], 16)) // num_rectangles,
                int((num_rectangles - i) * int(color1[5:], 16) + i * int(color2[5:], 16)) // num_rectangles
            )
            canvas.create_rectangle(0, i * (height // num_rectangles), width, (i + 1) * (height // num_rectangles), fill=color, outline="")

    # Função para centralizar a janela na tela
    # def center_window(self,window, width, height):
    #     screen_width = window.winfo_screenwidth()
    #     screen_height = window.winfo_screenheight()
    #     x = (screen_width // 2) - (width // 2)
    #     y = (screen_height // 2) - (height // 2)
    #     window.geometry(f'{width}x{height}+{x}+{y}')

    # Função para atualizar a imagem (substitua com sua lógica de atualização)
    def atualizar_imagem(self):
        # Aqui você pode implementar a lógica para atualizar a imagem
        # Por enquanto, vou manter a mesma imagem apenas para demonstração
        pass
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

        # Criar o fundo com gradiente
        self.create_gradient_background(canvas, min_width, min_height)

        # Carregar e redimensionar a imagem do Magma Dragoon
        self.image_path = "midia/imagens/BurnDinorex.jpg"  # Coloque o caminho da sua imagem aqui
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
        atualizar_button = tk.Button(self, text="Atualizar Chefe", command=self.atualizar_imagem)
        atualizar_button.place(x=250, y=700)  # Posição relativa ao canvas

        # Centralizar a janela na tela
        #self.center_window(self, min_width, min_height)

        # Rodar o loop principal
        self.mainloop()
