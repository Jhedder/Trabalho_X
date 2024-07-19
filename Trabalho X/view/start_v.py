import tkinter as tk
from controler.user_c import UsuarioController
from controler.delete_c import DeleteController
from controler.atualiza_c import AtualizaController
from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
from view.delete_v import DeleteView
from view.atualiza_v import AtualizaView
from PIL import Image, ImageTk
class StartView(tk.Frame):
  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.master.geometry('600x600')
        self.create_background()
        self.create_widgets()

    

    def load_image(self):
        image = Image.open("C:/Users/182400232/Documents/Trabalho/Trabalho X/Imagens/maxresdefault.jpg")
        image = image.resize((780, 600), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo

    def create_background(self):
        # Cria um Label para exibir a imagem como plano de fundo
        self.background_image = self.load_image()
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Posiciona o Label para ocupar toda a área do Frame


    def button_click(self):
        print("Botão clicado!")

    def create_widgets(self):
        # Cria um Frame para centralizar o botão na tela
        frame_center = tk.Frame(self)
        frame_center.place(relx=0.5, rely=0.9, anchor=tk.S)

        # Cria o botão dentro do Frame centralizado
        button = tk.Button(frame_center, text="Iniciar O Jogo", command=self.button_click)
        button.pack()
