class Usuarios:
    def __init__(self, usuario, senha, confirmar_senha) -> None:
        self.usuario = usuario
        self.senha = senha
        self.confirmar_senha = confirmar_senha
        self.usuarios = {
            'ederson': {
                'senha': '123456',
                'nome': 'Ederson',
            },
            'edini': {
                'senha': '123456',
                'nome': 'Edini',
            },
            'enilda': {
                'senha': '123456',
                'nome': 'Enilda',
            }
        }

    def validar_login(self):
        if self.usuario == self.senha:
            return {'code': 403, 'message' :'Usuário e senha não podem coincidir'}

        if self.senha != self.confirmar_senha:
            return {'code': 403, 'message' :'Senhas não coincidem!!'}

        if self.usuario in self.usuarios:
            if self.senha == self.usuarios[self.usuario]['senha']:
                return {'code': 200, 'message' :'Login Realizado com Sucesso!'}
            return {'code': 403, 'message' :'Credenciais inválidas!'}
        return {'code': 403, 'message' :'Usuário não cadastrado!'}