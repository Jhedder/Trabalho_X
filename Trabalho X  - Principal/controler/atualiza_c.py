from model.usuario_m import UsuarioModel
from view.atualiza_v import AtualizaView
import tkinter as tk


class AtualizaController:
    def __init__(self, view:AtualizaView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.atualizar_button.config()




