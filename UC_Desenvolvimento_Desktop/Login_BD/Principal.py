from Utils import Utils
from Usuarios import Usuarios
from App import App

class Principal(Utils):
    def __init__(self, usuario: Usuarios, connector):
        super().__init__(connector)
        self.usuario = usuario
        self.app = App(width=1200, height=800)
        self.janela = self.app.janela
        self.app.set_title('Area Logada')
        self.app.set_backgorund('black')

    def desenhar_elementos(self):
        self.app.janela.bind('<Escape>', lambda e: self.sair())

        main_frame = self.app.adicionar_frame(position={
            'grid': {
                'row': 0,
                'column': 0,
                'padx': 50,
                'sticky': 'nsew'
            }
        }, options={
            'config': {
                'fg_color': 'black'
            }
        })

        self.app.adicionar_label(f'Bem-vindo {self.usuario.get_nome()}!', position={
            'grid': {
                'row': 0,
                'column': 0,
                'pady': 60
            }
        }, options={
            'config': {
                'font': ('Arial', 32),
                'bg_color': 'black'
            },
            'master': main_frame
        })


    def sair(self):
        self.app.janela.destroy()

if __name__ == "__main__":
    import Main

    Main