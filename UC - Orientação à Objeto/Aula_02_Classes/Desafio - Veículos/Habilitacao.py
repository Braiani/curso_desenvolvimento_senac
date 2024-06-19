class Habilitacao:
    def __init__(self, quantidade_rodas, quantidade_ocupantes, peso_veiculo):
        self.quantidade_rodas = quantidade_rodas
        self.quantidade_ocupantes = quantidade_ocupantes
        self.peso_veiculo = peso_veiculo
        
    def tipo_habilitacao(self):
        if self.quantidade_rodas < 4:
            return "A"
        if self.quantidade_ocupantes <= 9:
            if self.peso_veiculo <= 3500:
                return "B"
            return "C"
        elif self.quantidade_ocupantes > 9:
            return "D"
        
        return "Categoria não identificada"
    