from TipoTracao import TipoTracao
from Categoria import Categoria
from Veiculo import Veiculo

class Automotor(TipoTracao, Categoria, Veiculo):

    def __init__(self, combustivel, potencia, nome_categoria, marca, modelo, ano, cor):
        TipoTracao.__init__(self, "Automotor", "Combustão")
        Categoria.__init__(self, nome_categoria)
        Veiculo.__init__(self, marca, modelo, ano, cor)
        self.combustivel = combustivel
        self.potencia = potencia

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(self.tipo_tracao())
        print(self.nome_categoria)
        print(self.combustivel)
        print(self.potencia)