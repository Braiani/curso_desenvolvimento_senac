class Livro:
    def __init__(self, titulo,autor,genero, codigo, status = 'Disponível') -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.status = status
    
    def create(self):
        return f'insert into livro(titulo, autor, genero, status, codigo) values ("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.codigo});'