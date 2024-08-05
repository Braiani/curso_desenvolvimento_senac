from Filo import Filo

class Classe(Filo):

    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas, nome_filo, morfologia, sistema_digestivo,nome_classe,habito_alimentar,locomocao):
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas, nome_filo, morfologia, sistema_digestivo)
        self.nome_classe = nome_classe
        self.habito_alimentar = habito_alimentar
        self.locomocao = locomocao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome da classe: {self.nome_classe}")
        print(f"Hábito alimentar: {self.habito_alimentar}")
        print(f"Locomoção: {self.locomocao}")