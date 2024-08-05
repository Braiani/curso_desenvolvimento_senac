import random

class Cartela:
    def __init__(self):
        self.cartela = {"B": [], "I": [], "N": [], "G": [], "O": []}
        self.numeros_sorteados = []
        self.gerar_cartela()

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
                num_aleatorio = random.randint(16,30)
                if num_aleatorio not in self.cartela["I"]:
                    self.cartela["I"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["N"]) <= 5:
                if len(self.cartela["N"]) == 2:
                    self.cartela["N"].append(0)
                    continue

                num_aleatorio = random.randint(31,45)
                if num_aleatorio not in self.cartela["N"]:
                    self.cartela["N"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["G"]) <= 5:
                num_aleatorio = random.randint(46,60)
                if num_aleatorio not in self.cartela["G"]:
                    self.cartela["G"].append(num_aleatorio)
            else:
                break
        
        while True:
            if len(self.cartela["O"]) <= 5:
                num_aleatorio = random.randint(61,75)
                if num_aleatorio not in self.cartela["O"]:
                    self.cartela["O"].append(num_aleatorio)
            else:
                break

    def formatar_numero(self, num):
        if num == "XX":
            return num
        
        if num < 10:
            return f"0{num}"
        return num
    
    def mostrarCartela(self):
        print("Veja abaixo sua cartela: ")
        print()
        print(f"+{'-'*78}+")
        print("|\t B\t||\t I\t||\t N\t||\t G\t||\t O\t|")
        print(f"+{'-'*78}+")
        
        for i in range(5):
            print(f"|\t{self.formatar_numero(self.cartela["B"][i])}\t|", end="")
            print(f"|\t{self.formatar_numero(self.cartela["I"][i])}\t|", end="")
            if i != 2:
                print(f"|\t{self.formatar_numero(self.cartela["N"][i])}\t|", end="")
            else:
                print(f"|     Free     |", end="")
            print(f"|\t{self.formatar_numero(self.cartela["G"][i])}\t|", end="")
            print(f"|\t{self.formatar_numero(self.cartela["O"][i])}\t|")
            print(f"|{"-"*15}||{"-"*14}||{"-"*14}||{"-"*14}||{"-"*13}|")
        print(f"+{'-'*78}+")


    def verificarCartelaBingada(self) -> bool:
        if self.verificaQuantidadeSorteadosColuna("B") == 5 or \
            self.verificaQuantidadeSorteadosColuna("I") == 5 or \
            self.verificaQuantidadeSorteadosColuna("N") == 5 or \
            self.verificaQuantidadeSorteadosColuna("G") == 5 or \
            self.verificaQuantidadeSorteadosColuna("O") == 5:
            return True
        if self.verificaQuantidadeSorteadosLinha(0) == 5 or \
            self.verificaQuantidadeSorteadosLinha(1) == 5 or \
            self.verificaQuantidadeSorteadosLinha(2) == 4 or \
            self.verificaQuantidadeSorteadosLinha(3) == 5 or \
            self.verificaQuantidadeSorteadosLinha(4) == 5:
            return True
        return False

    def atualizarCartelaComNumerosSorteados(self):
        for i in self.numeros_sorteados:
            for j in range(5):
                if self.cartela["B"][j] == i:
                    self.cartela["B"][j] = "XX"
                if self.cartela["I"][j] == i:
                    self.cartela["I"][j] = "XX"
                if self.cartela["N"][j] == i:
                    self.cartela["N"][j] = "XX"
                if self.cartela["G"][j] == i:
                    self.cartela["G"][j] = "XX"
                if self.cartela["O"][j] == i:
                    self.cartela["O"][j] = "XX"

    def salvarNumeroSorteado(self, numero):
        self.numeros_sorteados.append(numero)
        self.atualizarCartelaComNumerosSorteados()

    def verificaQuantidadeSorteadosColuna(self, coluna):
        ja_sorteado = 0
        for numero in self.cartela[coluna]:
            if numero == "XX":
                ja_sorteado += 1
        return ja_sorteado
    
    def verificaQuantidadeSorteadosLinha(self, linha):
        ja_sorteado = 0
        if self.cartela["B"][linha] == "XX":
            ja_sorteado += 1

        if self.cartela["I"][linha] == "XX":
            ja_sorteado += 1

        if self.cartela["N"][linha] == "XX":
            ja_sorteado += 1

        if self.cartela["G"][linha] == "XX":
            ja_sorteado += 1

        if self.cartela["O"][linha] == "XX":
            ja_sorteado += 1
        return ja_sorteado
    
    def gerarNovaCartela(self):
        self.cartela = {"B": [], "I": [], "N": [], "G": [], "O": []}
        self.numeros_sorteados = []
        self.gerar_cartela()