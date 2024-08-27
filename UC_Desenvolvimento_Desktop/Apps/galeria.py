from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox


class Application:
    def __init__(self) -> None:
        self.janela = Tk()
        self.images = []
        self.background = 'gray'

    def set_resizable(self, resizable=True):
        self.janela.resizable(resizable, resizable)

    def set_geometry(self, width, height):
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.janela.geometry(f"{width}x{height}+{x}+{y}")

    def set_title(self, title=""):
        self.janela.title(title)

    def set_background(self, color):
        self.background = color
        self.janela.config(background=color)

    def resize_image(self, image_path: str, width: int, height: int):
        img = PhotoImage(file=image_path)
        if img.width() <= width:
            factor_x = 1
        else:
            factor_x = img.width() / width

        if img.height() <= height:
            factor_y = 1
        else:
            factor_y = img.height() / height

        img = img.subsample(int(factor_x), int(factor_y))
        return img

    def container(self, image: dict):
        frame = Frame(self.janela, background=self.background)
        frame.grid(row=image['row'], column=image['col'], padx=50, pady=30)

        img = self.resize_image(image_path=image['src'], width=300, height=300)
        self.images.append(img)

        Label(frame, image=img).pack()
        entry = Entry(frame)
        entry.pack()
        return entry

    def change_entry_to_label(self, entry: Entry):
        text = entry.get()
        Label(entry.master, text=text, background=self.background, foreground='white').pack()
        entry.destroy()

    def set_button(self, options: dict):
        btn = Button(self.janela, text=options['text'], command=lambda: options['command']['function'](options['command']['args'], btn))

        btn.grid(row=options['row'], column=options['col'])

    def start(self):
        self.janela.mainloop()


def save_comments(args: list, button: Button):
    for entry in args[0]:
        args[1].change_entry_to_label(entry)
    button.destroy()
    messagebox.showinfo('Sucesso', 'Comentários salvos com sucesso!')

if __name__ == '__main__':
    try:
        programa = Application()
        programa.set_resizable(False)
        programa.set_background('gray')
        programa.set_geometry(1000, 650)
        programa.set_title('Galeria')

        images = [
            {
                'src': 'images/image1.png',
                'row': 0,
                'col': 0
            },
            {
                'src': 'images/image2.png',
                'row': 0,
                'col': 1
            },
            {
                'src': 'images/image3.png',
                'row': 1,
                'col': 0
            },
            {
                'src': 'images/image4.png',
                'row': 1,
                'col': 1
            },
        ]

        entries = []

        for image in images:
            entries.append(programa.container(image))

        programa.set_button({
            'text':'Salvar Comentários',
            'row': 2,
            'col': 1,
            'command': {
                'function': save_comments,
                'args': [entries, programa]
            }
        })

        programa.start()
    except Exception as e:
        print(e)