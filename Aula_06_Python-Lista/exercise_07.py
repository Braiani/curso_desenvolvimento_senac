print("""
Enunciado do exercício:
    7 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
      para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
      O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
      Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo,
      do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
""")

academia = []
maior = {'cod_altura': '', 'cod_peso': ''}
maior_peso = 0
maior_altura = 0
soma_peso = 0
soma_altura = 0

while True:
    codigo = input("Digite o seu código (0 para sair): ")

    if codigo == "0":
      break
    
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    soma_altura += altura
    soma_peso += peso

    if altura > maior_altura:
      maior_altura = altura
      maior['cod_altura'] = codigo

    if peso > maior_peso:
      maior_peso = peso
      maior['cod_peso'] = codigo
    
    academia.append({
        'codigo': codigo,
        'altura': altura,
        'peso': peso
    })

print(f"""
  +=================+===============+
  |    Maior Altura   || {maior['cod_altura']} - {maior_altura}
  |     Maior Peso    || {maior['cod_peso']} - {maior_peso}
  | Média das Alturas || {soma_altura / len(academia)}
  |  Média de Pesos   || {soma_peso / len(academia)}
  +=================+===============+
""")