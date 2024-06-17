from TipoTracao import TipoTracao
from Categoria import Categoria
from Veiculo import Veiculo
from Habilitacao import Habilitacao

class Eletrico(TipoTracao, Categoria, Veiculo, Habilitacao):

    def __init__(self, autonomia, potencia, 
                 nome_categoria, 
                 quantidade_rodas, quantidade_ocupantes, peso_veiculo,
                 marca, modelo, ano, cor, preco):
        TipoTracao.__init__(self, "Elétrico", "Energia Elétrica")
        Categoria.__init__(self, nome_categoria)
        Veiculo.__init__(self, marca, modelo, ano, cor)
        Habilitacao.__init__(self, quantidade_rodas, quantidade_ocupantes, peso_veiculo)
        self.autonomia = autonomia
        self.potencia = potencia
        self.preco = preco
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(self.tipo_tracao())
        print(self.nome_categoria)
        print(self.autonomia)
        print(self.potencia)

    def exibir_marca(self):
        return self.marca
    
    def exibir_modelo(self):
        return self.modelo
    
    def atende_requisitos(self, requisitos):
        atende = False
        if requisitos[0] == 1 and self.preco < 25000:
            atende = True

        return atende
        