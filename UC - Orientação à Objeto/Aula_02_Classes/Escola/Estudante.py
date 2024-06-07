from Pessoa import Pessoa

class Estudante(Pessoa):

    def __init__(self, nome, idade, peso, serie, ra, curso, notas = []):
        super().__init__(nome, idade, peso)
        self.serie = serie
        self.ra = ra
        self.curso = curso
        self.notas = notas

    def toString(self):
        return f"""
            nome: {self.nome}
            idade: {self.idade}
            peso: {self.peso}
            serie: {self.serie}
            ra: {self.ra}
            curso: {self.curso}
            notas: {self.notas}
        """

    def media(self):
        media = sum(self.notas)/len(self.notas)
        return media
    
    def foi_aprovado(self):
        return self.media >= 7
    
    def estudar(self):
        return False
    
rafael = Estudante('Rafael', 20, 152, 2, '123', 'Desenvolvimento', [5,6,8,10])

print(rafael.toString())
print("\n"*3)
print(f"O estudante {rafael.nome} pesa {rafael.peso} Kg e tem {rafael.media()} de média no curso {rafael.curso}")
print("\n"*3)