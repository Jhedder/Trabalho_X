from model.usuario_m import UsuarioModel
from view.show_bosses_v import ShowBossesView
import tkinter as tk


class Show_bosses_controller:
    def __init__(self, view:ShowBossesView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.atualizar_button.config()




