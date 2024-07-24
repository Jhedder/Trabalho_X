import tkinter as tk
from PIL import Image, ImageTk


from controler.delete_c import DeleteController
from controler.atualiza_c import AtualizaController
from model.usuario_m import UsuarioModel
from view.delete_v import DeleteView
from view.atualiza_v import AtualizaView
from view.menu_v import MenuView
from view.splash_v import SplashView
from view.escolha_chefe_v import EscolhaView
from controler.escolha_chefe_c import EscolhaController


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Megaman X5")
        self.escolha_chefe_v = EscolhaView
        self.atualiza_v = AtualizaView
        self.splash_v = SplashView
        self.menu_v = MenuView(self)
        self.switch_frame(SplashView)
        #self.switch_frame(UsuarioView)
   
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if frame_class ==  EscolhaView:
            model =  UsuarioModel()
            EscolhaController(new_frame,model)
        elif frame_class == DeleteView:
            model =  UsuarioModel()
            DeleteController(new_frame, model)
        elif frame_class == AtualizaView:
            model =  UsuarioModel()
            AtualizaController(new_frame, model)

        if hasattr(self, "current_frame"):
            self.current_frame.destroy()#fica aqui para apagar a visualização antiga....
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()