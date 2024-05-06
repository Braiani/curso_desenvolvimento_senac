print("""
Enunciado do exercício:
    38. Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação:
""")

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        | X  | Abaixo do Peso                |
        |    | Saudável                      |
        |    | Peso em excesso               |
        |    | Obesidade Grau I              |
        |    | Obesidade Grau II (severa)    |
        |    | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")
elif imc > 18.5 and imc <= 24.9:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        |    | Abaixo do Peso                |
        | X  | Saudável                      |
        |    | Peso em excesso               |
        |    | Obesidade Grau I              |
        |    | Obesidade Grau II (severa)    |
        |    | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")
elif imc > 24.9 and imc <= 29.9:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        |    | Abaixo do Peso                |
        |    | Saudável                      |
        | X  | Peso em excesso               |
        |    | Obesidade Grau I              |
        |    | Obesidade Grau II (severa)    |
        |    | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")
elif imc > 29.9 and imc <= 34.9:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        |    | Abaixo do Peso                |
        |    | Saudável                      |
        |    | Peso em excesso               |
        | X  | Obesidade Grau I              |
        |    | Obesidade Grau II (severa)    |
        |    | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")
elif imc > 34.9 and imc <= 39.9:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        |    | Abaixo do Peso                |
        |    | Saudável                      |
        |    | Peso em excesso               |
        |    | Obesidade Grau I              |
        | X  | Obesidade Grau II (severa)    |
        |    | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")
    
elif imc > 39.9:
    print("""
        +------------------------------------+
        |    |  Classificação                |
        +----+-------------------------------+
        |    | Abaixo do Peso                |
        |    | Saudável                      |
        |    | Peso em excesso               |
        |    | Obesidade Grau I              |
        |    | Obesidade Grau II (severa)    |
        | X  | Obesidade Grau III (mórbida)  |
        +----+-------------------------------+
""")