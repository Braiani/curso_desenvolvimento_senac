import random

class Cartela:
    def __init__(self):
        self.cartela = {"B": [], "I": [], "N": [], "G": [], "O": []}
        self.numeros_sorteados = []

    def gerar_cartela(self):
        while True:
            if len(self.cartela["B"]) <= 5:
                num_aleatorio = random.randint(1,15)
                if num_aleatorio not in self.cartela["B"]:
                    self.cartela["B"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["I"]) <= 5:
                num_aleatorio = random.randint(15,30)
                if num_aleatorio not in self.cartela["I"]:
                    self.cartela["I"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["N"]) <= 5:
                if len(self.cartela["N"]) == 2:
                    self.cartela["N"].append(0)
                    continue

                num_aleatorio = random.randint(30,45)
                if num_aleatorio not in self.cartela["N"]:
                    self.cartela["N"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["G"]) <= 5:
                num_aleatorio = random.randint(45,60)
                if num_aleatorio not in self.cartela["G"]:
                    self.cartela["G"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["O"]) <= 5:
                num_aleatorio = random.randint(60,75)
                if num_aleatorio not in self.cartela["O"]:
                    self.cartela["O"].append(num_aleatorio)
            else:
                break            
        
        return self.cartela
    
    def verificarCartelaBingada(self) -> bool:
        for i in range(len(self.numeros_sorteados)):
            print(i)

    def salvarNumeroSorteado(self, numero):
        self.numeros_sorteados.append(numero)