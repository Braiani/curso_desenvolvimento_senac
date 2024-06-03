print("""
Enunciado do exercício:
    12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual 
    numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: 
    a. Tabuada de 5: 
    b. 5 X 1 = 5 
    c. 5 X 2 = 10 
    d. ... 
    e. 5 X 10 = 50
""")

tabuada = int(input("Digite a tabuada que deseja ver: "))

print(f"Tabuada de {tabuada}:")
for i in range(1,11):
    print(f"{tabuada} X {i} = {tabuada * i}")