from Ordem import Ordem

class Familia(Ordem):
    def __init__(self, nome_reino, tipo_nutricao, tipo_celulas,
                 nome_filo, morfologia, sistema_digestivo,
                 nome_classe, habito_alimentar, locomocao,
                 nome_ordem, interdependencia_ecologica,
                 nome_familia, anatomia):
        
        super().__init__(nome_reino, tipo_nutricao, tipo_celulas,
                         nome_filo, morfologia, sistema_digestivo,
                         nome_classe, habito_alimentar, locomocao,
                         nome_ordem, interdependencia_ecologica)
        self.nome_familia = nome_familia
        self.anatomia = anatomia

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Nome da família: {self.nome_ordem}")
        print(f"Anatomia: {self.anatomia}")