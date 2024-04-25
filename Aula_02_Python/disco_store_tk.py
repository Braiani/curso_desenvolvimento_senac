import tkinter as tk
from tkinter import messagebox

def precos_produtos():
    return [
        ("Azul", 20.0),
        ("Laranja", 30.0),
        ("Roxo", 40.0),
        ("Marrom", 50.0),
        ("Vermelho", 60.)
    ]

def mostrar_informacao():
    opcao_selecionada = escolha.get()
    if opcao_selecionada == "Opção 1":
        messagebox.showinfo("Informação", "Você selecionou a Opção 1!")
    else:
        messagebox.showinfo("Informação", "Por favor, selecione uma opção.")


# Cria a janela principal
janela = tk.Tk()
janela.title("Menu de Escolha")

# Define a largura e altura da janela
largura_janela = 960
altura_janela = 540

# Obtém a largura e altura da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula a posição x e y para centralizar a janela na tela
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2

# Define a posição e tamanho inicial da janela
janela.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, posicao_x, posicao_y))

valores = precos_produtos()

escolha = tk.StringVar(janela)
escolha.set(valores[0][0])

for produto, preco in valores:
    tk.OptionMenu(janela, escolha, produto, *valores)
    tk.Label(janela, text=f"{produto}: R${preco}").pack(pady=5)

# Cria o botão para mostrar a informação
botao_mostrar = tk.Button(janela, text="Finalizar", command=mostrar_informacao)
botao_mostrar.pack(pady=10)

# Inicia o loop principal da aplicação
janela.mainloop()
