from Vertebrados import Vertebrados

class Mamiferos(Vertebrados):
    def __init__(self, nome_cientifico, habitat, nome_comum) -> None:
        super().__init__(nome_cientifico, habitat)
        self.nome_comum = nome_comum

    def amamentar(self):
        return f'O animal {self.nome_comum} está amamentando, pois é mamifero'