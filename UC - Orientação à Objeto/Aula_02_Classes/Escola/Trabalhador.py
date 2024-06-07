from Pessoa import Pessoa

class Trabalhador(Pessoa):

    def __init__(self, nome, idade, peso, empresa, matricula, salario):
        super().__init__(nome, idade, peso)
        self.empresa = empresa
        self.matricula = matricula
        self.salario = salario



    def feliz_no_trabalho():
        return True