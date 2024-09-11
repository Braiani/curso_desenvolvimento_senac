from App import App
import PIL.Image as Image
from Utils import Utils
from Usuarios import Usuarios

def logar(entradas: dict):
    usuario = entradas.get('usuario', '').get()
    senha = entradas.get('senha', '').get()
    if usuario == '' or senha == '':
        app.message_box(message='Dados inválidos', title='Verifique os dados', type='error')
        return

    global utils
    print(usuario, utils.generate_md5(senha))
    usuario = Usuarios(usuario, utils.generate_md5(senha), utils.get_connection())
    if not usuario.validar_login():
        app.message_box('Usuário inválido', 'Erro', 'warning')
        return
    
    app.message_box('Logado com sucesso!')

utils = Utils()

base_path = utils.get_base_path()

app = App(width=1200, height=800)

app.set_backgorund('black')
app.theme('mica')

entradas = {
    'usuario': '',
    'senha': ''
}

image = Image.open(f"{base_path}/mercado.jpg")

app.adicionar_imagem(image=image, position={
    'grid': {
        'row': 0,
        'column': 0,
        'rowspan': 6
    }
}, options={
    'size': ((app.width // 2) , app.height)
})

main_frame = app.adicionar_frame(position={
    'grid':{
        'row': 0,
        'column': 1,
        'padx': 50,
        'sticky': 'nsew'
    }
}, options={
    'config':{
        'fg_color': 'black'
    }
})

app.adicionar_label('Bem-vindo ao Sistema do Mercado!', position={
    'grid':{
        'row': 0,
        'column': 0,
        'pady': 80
    }
}, options={
    'config':{
        'font': ('Arial', 32),
        'bg_color': 'black'
    },
    'opacity': 'black',
    'master': main_frame
})

app.adicionar_label('Digite seu login:', position={
    'grid':{
        'row': 1,
        'column': 0
    }
}, options={
    'config':{
        'font': ('Arial', 24),
        'bg_color': 'black'
    },
    'opacity': 'black',
    'master': main_frame
})

usuario = app.adicionar_entry(position={
    'grid':{
        'row': 2,
        'column': 0,
        'pady': 20
    }
}, options={
    'config': {
        'width': (app.width // 2) - 100,
        'corner_radius': 32
    },
    'master': main_frame
})

entradas.update({'usuario': usuario})

app.adicionar_label('Digite sua senha:', position={
    'grid':{
        'row': 3,
        'column': 0
    }
}, options={
    'config':{
        'font': ('Arial', 24),
        'bg_color': 'black'
    },
    'opacity': 'black',
    'master': main_frame
})

senha = app.adicionar_entry(position={
    'grid':{
        'row': 4,
        'column': 0,
        'pady': 20
    }
}, options={
    'config': {
        'width': (app.width // 2) - 100,
        'corner_radius': 32,
        'show': '*'
    },
    'master': main_frame
})

entradas.update({'senha': senha})

app.adicionar_button(position={
    'grid':{
        'row': 5,
        'column': 0,
        'pady': 20,
        'sticky': 'w'
    }
}, options={
    'config': {
        'corner_radius': 32,
        'height': 50,
        'text': 'Logar',
        'command': lambda: logar(entradas)
    },
    'master': main_frame
})

app.adicionar_button(position={
    'grid':{
        'row': 5,
        'column': 0,
        'sticky': 'e',
        'pady': 20
    }
}, options={
    'config': {
        'corner_radius': 32,
        'height': 50,
        'text': 'Cadastrar'
    },
    'master': main_frame
})

app.start()