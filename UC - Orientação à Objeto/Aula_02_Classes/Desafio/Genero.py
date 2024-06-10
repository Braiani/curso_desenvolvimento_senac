from Familia import Familia

class Genero(Familia):
    
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas,
                 nome_filo, morfologia, sistema_digestivo,
                 nome_classe, habito_alimentar, locomocao,
                 nome_ordem, interdependencia_ecologica, 
                 nome_familia, anatomia,
                 nome_genero, adaptacoes):
        
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas,
                         nome_filo, morfologia, sistema_digestivo,
                         nome_classe, habito_alimentar, locomocao,
                         nome_ordem, interdependencia_ecologica,
                         nome_familia, anatomia)
        
        self.nome_genero = nome_genero
        self.adaptacoes = adaptacoes

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome do Gênero: {self.nome_genero}")
        print(f"Adaptações morfologicas: {self.adaptacoes}")