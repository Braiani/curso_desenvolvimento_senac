class Habilitacao:
    def __init__(self, idade, quantidade_rodas, quantidade_ocupantes, peso_veiculo):
        self.idade = idade
        self.quantidade_rodas = quantidade_rodas
        self.quantidade_ocupantes = quantidade_ocupantes
        self.peso_veiculo = peso_veiculo
        

    def pode_ter_habilitacao(self):
        return self.idade >= 18
    
    def tipo_habilitacao(self):
        if self.quantidade_rodas < 4:
            return "A"
        if self.quantidade_ocupantes <= 9:
            if self.peso_veiculo <= 3500:
                return "B"
            return "C"
        elif self.quantidade_ocupantes > 9:
            return "D"
        
        if self.idade >=21:
            return "E"
        
        return "Categoria não identificada"
    
class Carro(Habilitacao):
    def __init__(self, cor, marca, idade, quantidade_rodas, quantidade_ocupantes, peso_veiculo):
        super().__init__(idade, quantidade_rodas, quantidade_ocupantes, peso_veiculo)
        self.cor = cor
        self.marca = marca

    def qual_meu_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Cor: {self.cor}")