from TipoTracao import TipoTracao
from Categoria import Categoria
from Veiculo import Veiculo

class Eletrico(TipoTracao, Categoria, Veiculo):

    def __init__(self, autonomia, potencia, nome_categoria, marca, modelo, ano, cor):
        TipoTracao.__init__(self, "Elétrico", "Energia Elétrica")
        Categoria.__init__(self, nome_categoria)
        Veiculo.__init__(self, marca, modelo, ano, cor)
        self.autonomia = autonomia
        self.potencia = potencia
        self.nome_categoria = nome_categoria

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(self.tipo_tracao())
        print(self.nome_categoria)
        print(self.autonomia)
        print(self.potencia)