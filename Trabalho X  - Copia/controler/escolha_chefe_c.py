from model.usuario_m import UsuarioModel
from view.escolha_chefe_v import EscolhaView
import tkinter as tk


class EscolhaController:
    def __init__(self, view:EscolhaView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_chefe)
        self.carregar_chefes()

    def adicionar_chefe(self):
        id = self.view.get_id()
        if  id:
            self.model.inserir_chefe(id)
            self.view.chefes_listbox.delete(0, tk.END)
            self.carregar_chefes()

    def carregar_chefes(self):
        chefe = self.model.selecionar_chefe()#retorna uma lista de tuplas
        for chefe in chefe:
            self.view.adicionar_chefe_lista(chefe)