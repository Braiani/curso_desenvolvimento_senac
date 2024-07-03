import random as r

class Roleta:
    
    def __init__(self):
        self.historico = []

    def girar(self):
        numero = r.randint(1,75)
        self.historico.append(numero)
        return numero
    
    def girarNumeroUnico(self):
        while True:
            numero = r.randint(1,75)
            if numero not in self.historico:
                self.historico.append(numero)
                return numero
            self.historico.append(numero)
                


    def exibir_historico(self):
        print(f"Os números gerados até o momento foram: {self.historico}")