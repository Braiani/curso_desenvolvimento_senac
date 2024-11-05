
class ControllerLivro:
    def __init__(self) -> None:
        pass
    
    def pode_emprestar(self):
        return self.status == 'Disponível'

    def emprestar_livro(self, usuario):
        if not self.pode_emprestar():
            print("Livro indisponível para empréstimo")
            return
        
        self.status = "Emprestado"
        self.usuario = usuario

    def devolver_livro(self):
        if self.status != "Emprestado":
            return
        
        self.status = "Disponível"
        self.usuario = None