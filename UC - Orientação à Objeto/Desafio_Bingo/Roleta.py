import random as r

class Roleta:
    
    def __init__(self):
        self.historico = []

    def girar(self):
        numero = r.randint(1,5)
        self.historico.append(numero)
        return numero
    
    def exibir_historico(self):
        print(f"Os números gerados até o momento foram: {self.historico}")