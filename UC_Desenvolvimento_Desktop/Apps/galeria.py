from tkinter import *
from tkinter import PhotoImage

class Application:
    def __init__(self) -> None:
        self.janela = Tk()
        self.images = []
    
    def set_resizable(self, resizable=True):
        self.janela.resizable(resizable,resizable)

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

    def container(self, image: dict = {}):
        frame = Frame(self.janela, background=self.background)
        frame.grid(row=image['row'], column=image['col'], padx=50, pady=30)

        img = self.resize_image(image_path=image['src'], width=300, height=300)
        self.images.append(img)

        Label(frame, image=img).pack()
        Entry(frame).pack()

    def start(self):
        self.janela.mainloop()

if __name__ == '__main__':
    programa = Application()
    programa.set_resizable(False)
    programa.set_background('gray')
    programa.set_geometry(1000,650)
    programa.set_title('Galeria')

    images = [
        {
            'src': 'UC_Desenvolvimento_Desktop\\Apps\\images\\image1.png',
            'row': 0,
            'col': 0
        },
        {
            'src': 'UC_Desenvolvimento_Desktop\\Apps\\images\\image2.png',
            'row': 0,
            'col': 1
        },
        {
            'src': 'UC_Desenvolvimento_Desktop\\Apps\\images\\image3.png',
            'row': 1,
            'col': 0
        },
        {
            'src': 'UC_Desenvolvimento_Desktop\\Apps\\images\\image4.png',
            'row': 1,
            'col': 1
        },
    ]
    
    for image in images:
        programa.container(image)

    programa.start()