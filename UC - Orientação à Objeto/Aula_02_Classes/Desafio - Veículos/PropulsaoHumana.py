from TipoTracao import TipoTracao
from Categoria import Categoria
from Veiculo import Veiculo
from Habilitacao import Habilitacao

class PropulsaoHumana(TipoTracao, Categoria, Veiculo, Habilitacao):

    def __init__(self, aro, autonomia,
                 nome_categoria,
                 quantidade_rodas, quantidade_ocupantes, peso_veiculo,
                 marca, modelo, ano, cor, preco):
        TipoTracao.__init__(self, "Propulsao Humana", "Humana")
        Categoria.__init__(self, nome_categoria)
        Veiculo.__init__(self, marca, modelo, ano, cor)
        Habilitacao.__init__(self, quantidade_rodas, quantidade_ocupantes, peso_veiculo)
        self.aro = aro
        self.autonomia = autonomia
        self.preco = preco

    def exibir_informacoes(self):
        texto_pai = super().exibir_informacoes()
        return f"{texto_pai}{self.descricao_tracao()}\nNome categoria: {self.nome_categoria}, autonomia: {self.autonomia}, aro: {self.aro}"
        
    def exibir_marca(self):
        return self.marca
    
    def exibir_modelo(self):
        return self.modelo
    
    def atende_requisito(self, requisito, resposta):
        if requisito == 'ocupacao':
            return self.atende_requisito_ocupacao(resposta)
        elif requisito == 'autonomia':
            return self.atende_requisito_autonomia(resposta)
        elif requisito == 'combustivel':
            return self.atende_requisito_combustivel(resposta)
        elif requisito == 'estilo_vida':
            return self.atende_requisito_estilo_vida(resposta)
    
    def atende_requisito_ocupacao(self, ocupacao):
        if ocupacao == 1 and self.preco < 25000:
            return True
        elif ocupacao == 2 and self.preco < 30000:
            return True
        elif ocupacao == 3 and self.preco < 50000000:
            return True
        elif ocupacao == 4 and self.preco < 150000:
            return True
        elif ocupacao == 5 and self.preco < 2000000:
            return True
        else:
            return False
    
    def atende_requisito_autonomia(self, autonomia):
        if autonomia == 1 and (self.autonomia >= 1500):
            return True
        elif autonomia == 2 and (self.autonomia >= 1000):
            return True
        elif autonomia == 3 and (self.autonomia >= 800):
            return True
        elif autonomia == 4 and (self.autonomia < 800):
            return True
        else:
            return False
        
    def atende_requisito_combustivel(self, combustivel):
        if combustivel == 1 and (self.tipo_tracao() == "Propulsão Humana"):
            return True
        elif combustivel == 2 and (self.tipo_tracao() == "Elétrico"):
            return True
        elif combustivel == 3 and (self.tipo_tracao() == "Automotor"):
            return True
        else:
            return False
        
    def atende_requisito_estilo_vida(self, estilo_vida):
        if estilo_vida == 1 and (self.peso_veiculo < 22):
            return True
        elif estilo_vida == 2 and (self.quantidade_ocupantes == 2):
            return True
        elif estilo_vida == 3 and (self.cor == "Branca" or self.cor == "Preto"):
            return True
        elif estilo_vida == 4 and (self.aro <= 24):
            return True
        else:
            return False