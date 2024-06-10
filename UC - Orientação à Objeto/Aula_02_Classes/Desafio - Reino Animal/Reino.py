class Reino:
    
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas):
        self.nome_reino = nome_reino
        self.tipo_nutricao = tipo_nutricao
        self.tipo_celulas = tipo_celulas

    def exibir_informacoes(self):
        print(f"Nome do reino: {self.nome_reino}")
        print(f"Tipo de nutrição: {self.tipo_nutricao}")
        print(f"Tipo de células: {self.tipo_celulas}")