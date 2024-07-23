from model.usuario_m import UsuarioModel
from view.atualiza_v import AtualizaView
import tkinter as tk


class AtualizaController:
    def __init__(self, view:AtualizaView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.atualizar_button.config(command=self.atualizar_chefe)
        self.carregar_chefes()

    def atualizar_chefe(self):
        id = self.view.get_id()

        if id.isdigit():
            self.model.atualizar_chefe(id)
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_chefes()
        else:
            self.view.show_info()

    def carregar_chefes(self):
        chefe = self.model.selecionar_chefe()#retorna uma lista de tuplas
        for chefe in chefe:
            self.view.adicionar_chefe_lista(chefe)



