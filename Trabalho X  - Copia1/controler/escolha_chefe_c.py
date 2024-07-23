from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
from view.escolha_chefe_v import EscolhaView
import tkinter as tk


class EscolhaController:
    def __init__(self, view:EscolhaView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_usuario)
        self.carregar_usuarios()

    def adicionar_usuario(self):
        id = self.view.get_id()
        if  id:
            self.model.inserir_usuario(id)
            self.view.nome_entry.delete(0, tk.END)
            self.view.idade_entry.delete(0, tk.END)
            self.view.usuarios_listbox.delete(0, tk.END)
            self.carregar_usuarios()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()#retorna uma lista de tuplas
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)