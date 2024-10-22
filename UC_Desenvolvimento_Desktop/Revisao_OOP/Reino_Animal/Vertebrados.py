from Animais import Animais
class Vertebrados(Animais):
    def __init__(self, nome_cientifico, habitat) -> None:
        super().__init__(nome_cientifico, habitat)
        self.coluna_vertebral = True
        self.cranio = True
