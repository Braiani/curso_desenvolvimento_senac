from Reino import Reino

class Filo(Reino):
    
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas, nome_filo, morfologia, sistema_digestivo):
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas)
        self.nome_filo = nome_filo
        self.morfologia = morfologia
        self.sistema_digestivo = sistema_digestivo
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome do Filo: {self.nome_filo}")
        print(f"Tipo de morfologia: {self.morfologia}")
        print(f"Tipo de sistema digestivo: {self.sistema_digestivo}")