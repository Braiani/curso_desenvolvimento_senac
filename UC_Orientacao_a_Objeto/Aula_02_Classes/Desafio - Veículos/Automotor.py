from TipoTracao import TipoTracao
from Categoria import Categoria
from Veiculo import Veiculo
from Habilitacao import Habilitacao

class Automotor(TipoTracao, Categoria, Veiculo, Habilitacao):

    def __init__(self, combustivel, potencia,
                 nome_categoria,
                 quantidade_rodas, quantidade_ocupantes, peso_veiculo,
                 marca, modelo, ano, cor, preco):
        TipoTracao.__init__(self, "Automotor", "Combustão")
        Categoria.__init__(self, nome_categoria)
        Veiculo.__init__(self, marca, modelo, ano, cor)
        Habilitacao.__init__(self, quantidade_rodas, quantidade_ocupantes, peso_veiculo)
        self.combustivel = combustivel
        self.potencia = potencia
        self.preco = preco

    def exibir_informacoes(self):
        texto_pai = super().exibir_informacoes()
        return f"""{texto_pai}{self.descricao_tracao()}
        Nome categoria: {self.nome_categoria}, 
        combustivel: {self.combustivel}, potencia: {self.potencia}
        Valor: R$ {self.preco:.2f} - {self.habilitacao_necessaria()}"""
        
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
        if ocupacao == 1 and (self.preco < 100000 and (self.nome_categoria == 'Particular' or self.nome_categoria == 'Aluguel')):
            return True
        elif ocupacao == 2 and (self.preco < 160000 and (self.nome_categoria == 'Particular' or self.nome_categoria == 'Aluguel')):
            return True
        elif ocupacao == 3:
            return True
        elif ocupacao == 4 and (self.preco < 250000 or self.nome_categoria == 'Transporte Público'):
            return True
        elif ocupacao == 5 and (self.preco < 1300000  and (self.nome_categoria != 'Transporte Público' or self.nome_categoria != 'Carga Pesada')):
            return True
        else:
            return False

    def atende_requisito_autonomia(self, autonomia):
        if autonomia == 1 and (self.potencia >= 300 or self.combustivel == "Gasolina"):
            return True
        elif autonomia == 2 and (self.potencia >= 200 or self.combustivel == "Diesel"):
            return True
        elif autonomia == 3 and (self.potencia >= 100 or self.combustivel == "Etanol"):
            return True
        elif autonomia == 4:
            return True
        else:
            return False
        
    def atende_requisito_combustivel(self, combustivel):
        if combustivel == 3 or self.combustivel == "Etanol":
            return True
        return False
        
    def atende_requisito_estilo_vida(self, estilo_vida):
        if estilo_vida == 1 and self.ano >= 2022:
            return True
        elif estilo_vida == 2 and self.nome_categoria == "Aluguel":
            return True
        elif estilo_vida == 3 and (self.potencia >= 100 and (self.cor == "Branca" or self.cor == "Preto")):
            return True
        elif estilo_vida == 4 and self.quantidade_ocupantes >= 3:
            return True
        else:
            return False