from Mamiferos import Mamiferos

class Morcego(Mamiferos):
    def voar(self):
        return f'O {self.nome_comum} consegue voar!'
    
    def movimentacao(self):
        return self.voar()