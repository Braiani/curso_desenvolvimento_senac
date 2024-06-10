from Genero import Genero

class Especie(Genero):
    
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas,
                 nome_filo, morfologia, sistema_digestivo,
                 nome_classe, habito_alimentar, locomocao,
                 nome_ordem, interdependencia_ecologica,
                 nome_familia, anatomia,
                 nome_genero, adaptacoes,
                 nome_cientifico, dieta):
        
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas,
                         nome_filo, morfologia, sistema_digestivo,
                         nome_classe, habito_alimentar, locomocao,
                         nome_ordem, interdependencia_ecologica,
                         nome_familia, anatomia,
                         nome_genero, adaptacoes)
        self.nome_cietifico = nome_cientifico
        self.dieta = dieta

    def printar_nome_especie(self):
        print(f"Nome Científico da Espécie: {self.nome_cietifico}")
    
    def nome_especie(self):
        return self.nome_cietifico

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome Científico da Espécie: {self.nome_cietifico}")
        print(f"Dieta da espécie: {self.dieta}")