from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
import tkinter as tk


class UsuarioController:
    def __init__(self, view:UsuarioView, model:UsuarioModel):
        self.view = view
        self.model = model
        