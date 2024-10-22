class Animais:
    def __init__(self, nome_cientifico, habitat) -> None:
        self.nome_cientifico = nome_cientifico
        self.habitat = habitat

    def alimentacao(self):
        return f'O {self.nome_cientifico} está se alimentando no seu {self.habitat}'
    
    def movimentacao(self):
        return f'O {self.nome_cientifico} está se movimentando até o seu {self.habitat}'
    
    def reproducao(self):
        return f'O {self.nome_cientifico} está se reproduzindo no seu {self.habitat}'