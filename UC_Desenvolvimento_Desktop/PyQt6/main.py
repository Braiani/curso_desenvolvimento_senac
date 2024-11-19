import sys, os
from PyQt6.uic import load_ui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow, QWidget

class MainWindows(QMainWindow):
    contador = 1
    def __init__(self, ui_file) -> None:
        super().__init__()
        load_ui.loadUi(ui_file, self)
        self.btn_teste.clicked.connect(self.clicked)
        self.btn_teste.pressed.connect(lambda: self.btn_teste.setText('pressionado!'))

        
    
    def clicked(self):
        vezes = 'vez'
        if self.contador > 1:
            vezes = 'vezes'
        self.btn_teste.setText(f'Você clicou {self.contador} {vezes}!')
        self.contador += 1
    
    def hover(self):
        print('Vc passou sobre o botão!')

def get_base_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

if __name__ == "__main__":
    ui_file = get_base_path() + "/teste.ui"

    app = QApplication(sys.argv)
    window = MainWindows(ui_file)
    window.show()
    sys.exit(app.exec())