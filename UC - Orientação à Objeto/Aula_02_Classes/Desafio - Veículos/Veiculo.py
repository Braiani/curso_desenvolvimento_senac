class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)
        print(self.cor)