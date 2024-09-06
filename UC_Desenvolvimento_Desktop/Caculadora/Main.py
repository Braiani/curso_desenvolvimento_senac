import customtkinter as ctk
from PIL import Image
from tkinter import PhotoImage
import pywinstyles, os, sys


class App:
    def __init__(self) -> None:
        self.janela = ctk.CTk()
        self.set_title("Calculadora FASIO")
        self.set_geometry(600,700,True)
        self.janela.resizable(False, False)
        pywinstyles.apply_style(self.janela, 'aero')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme(f"{self.base_path()}/theme.json")

    def set_title(self, title=""):
        self.janela.title(title)

    @staticmethod
    def set_options_elements(element: ctk.CTkEntry | ctk.CTkLabel | ctk.CTkButton, options: dict):
        if 'opacity' in options:
            pywinstyles.set_opacity(element, color=options.get('opacity', 'white'))
        if 'config' in options:
            element.configure(**options['config'])

    @staticmethod
    def positional_element(element: ctk.CTkEntry | ctk.CTkLabel | ctk.CTkButton, options: dict):
        grid_options = {
            'padx': 10,
            'pady': 10
        }

        if options is not None and 'grid' in options:
            grid_options.update(options['grid'])

        if options.get('place', False):
            element.place(**options['place'])
            return

        if options.get('pack', False):
            element.pack(**options['pack'])
            return

        element.grid(**grid_options)

    def place_entry(self, options: dict=None):
        entrada = ctk.CTkEntry(master=options.get('master', self.janela))

        self.set_options_elements(element=entrada, options=options)
        self.positional_element(element=entrada, options=options)
        
        return entrada
    
    def place_frame(self, options: dict):
        frame = ctk.CTkFrame(master=options.get('master', self.janela))

        self.set_options_elements(element=frame, options=options)
        self.positional_element(element=frame, options=options)

        return frame
    
    def place_buttons(self, command, options: dict=None):
        btn = ctk.CTkButton(master=options.get('master', self.janela), command=command)

        self.set_options_elements(element=btn, options=options)
        self.positional_element(element=btn, options=options)
        
        return btn
    
    def place_labels(self, options: dict=None):
        btn = ctk.CTkLabel(master=options.get('master', self.janela))

        self.set_options_elements(element=btn, options=options)
        self.positional_element(element=btn, options=options)
        
        return btn
    
    @staticmethod
    def base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    def set_geometry(self, width, height, center = True, x=None, y=None):
        if center:
            screen_width = self.janela.winfo_screenwidth()
            screen_height = self.janela.winfo_screenheight()

            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            self.janela.geometry(f"{width}x{height}+{x}+{y}")
        else:
            if x is not None and y is not None:
                self.janela.geometry(f"{width}x{height}+{x}+{y}")
            else:
                self.janela.geometry(f"{width}x{height}")

    def start(self):
        self.janela.mainloop()


class Calculadora:
    def __init__(self) -> None:
        pass

    def atualizar_valor(self, new):
        pass


def botao_apertado(valor, calc: Calculadora, entry: ctk.CTkEntry):
    calc.atualizar_valor(valor)
    if valor == 'back':
        entrada.delete(ctk.END, ctk.END)
        return
    entry.insert(index=ctk.END,string=valor)


if __name__ == '__main__':
    app = App()
    calculadora = Calculadora()

    for col in range(5):
        app.janela.grid_columnconfigure(col, weight=1)
    
    app.place_labels({
        'config': {
            'text': 'FASIO',
            'font': ('Arial', 30),
            'height': 50,
            'corner_radius': 10,
            'bg_color': "#000001"
        },
        'grid': {
            'row': 0,
            'column': 0,
            'columnspan': 2,
            'padx': 20,
            'pady': 0,
            'sticky': 'nwes'
        }
    })

    app.place_frame({
        'config': {
            'height': 50,
            'corner_radius': 10,
            'bg_color': "#000001"
        },
        'grid': {
            'row': 0,
            'column': 3,
            'columnspan': 2,
            'padx': 30,
            'pady': 20,
            'sticky': 'nwes'
        }
    })

    entrada = app.place_entry(options={
        'config': {
            'height': 80,
            'font': ('Arial', 40),
            'corner_radius': 5,
            'bg_color': "#000001"
        },
        'opacity': "#000001",
        'grid': {
            'row': 1,
            'column': 0,
            'columnspan': 5,
            'padx': 30,
            'pady': 20,
            'sticky': 'nwes'
        }
    })


    botoes = {
        'invert': '+/-',
        'raiz' :'√',
        '%':'%',
        ' ':' ',
        '÷':'÷',
        'back':'back',
        '7':'7',
        '8':'8',
        '9':'9',
        'X':'X',
        'C':'C',
        '4':'4',
        '5':'5',
        '6':'6',
        '-':'-',
        'AC':'AC',
        '1':'1',
        '2':'2',
        '3':'3',
        '+':'plus',
        '0':'0',
        '00':'00',
        '.':'.',
        '=': '='
    }
    
    column = 0
    row = 2
    for key, botao in botoes.items():
        if column > 4:
            column = 0
            row += 1
        
        grid = {
            'row': row,
            'column': column,
            'padx': 5,
            'pady': 20,
            'sticky': 'n'
        }

        config = {
            'height': 60,
            'text': botao,
            'font': ('Arial', 20, 'bold'),
            'corner_radius': 10,
            'bg_color': "#000001"
        }

        
        if botao == 'back':
            config['text'] = ''
            img = Image.open(f"{app.base_path()}/backspace.png")
            config['image'] = ctk.CTkImage(img, size=(50,50))

        if botao == 'plus':
            config['text'] = "+"
            grid['rowspan'] = 2
            grid['sticky'] = 'nwes'


        app.place_buttons(
            command=lambda digitado=key: botao_apertado(valor=digitado, calc=calculadora, entry=entrada),
            options={
            'config': config,
            'grid': grid,
            'opacity': "#000001",
        })

        column += 1


    app.start()