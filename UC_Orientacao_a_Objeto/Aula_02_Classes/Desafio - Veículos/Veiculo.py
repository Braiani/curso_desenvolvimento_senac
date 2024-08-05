class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}\n"
        
    def atende_requisito(self, requisito, resposta):
        pass