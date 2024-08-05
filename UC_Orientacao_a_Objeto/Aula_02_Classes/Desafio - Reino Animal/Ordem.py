from Classe import Classe

class Ordem(Classe):
    
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas,
                 nome_filo, morfologia, sistema_digestivo,
                 nome_classe, habito_alimentar, locomocao,nome_ordem,interdependencia_ecologica):
          
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas, nome_filo, morfologia, sistema_digestivo, nome_classe, habito_alimentar, locomocao)
        self.nome_ordem = nome_ordem
        self.interdependencia_ecologica = interdependencia_ecologica

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome da ordem: {self.nome_ordem}")
        print(f"Interdependência ecológica: {self.interdependencia_ecologica}")