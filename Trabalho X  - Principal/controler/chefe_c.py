from model.usuario_m import UsuarioModel
import tkinter as tk


class ChefeController:
    def __init__(self,parent, view,model):
        self.parent= parent
        self.view = view
        self.model = model
        self.id_chefe = ""
        self.view.escolher_button.config(command=self.selecionar_chefe)
        self.retornar_url_img_chefe

    def selecionar_chefe(self):
        self.parent.switch_frame(self.parent.escolha_chefe_v)

    def retornar_url_img_chefe(self):
        chefe = self.model.carregar_chefe(self.id_chefe) 
        self.view.image_path = chefe[4]