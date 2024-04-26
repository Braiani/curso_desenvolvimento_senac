import tkinter as tk
from tkinter import ttk

def createFrame():
    frame = tk.Tk()
    frame.title("Tela de login")
    frame.geometry(f"{960}x{540}")
    return frame

def appendElements(frame):
    label = ttk.Label(frame, text="Digite seu usuário", borderwidth=20)
    button = ttk.Button(frame, text="Login")
    label.pack(padx=0)
    button.pack(pady=20)

if __name__ == '__main__':
    frame = createFrame()
    appendElements(frame)
    frame.mainloop()
