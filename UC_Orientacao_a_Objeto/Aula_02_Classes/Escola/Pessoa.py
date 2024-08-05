class Pessoa:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def acordar(self):
        return True
    
    def caminhar(self):
        return 'passo'
    
    def comer(self):
        return False
