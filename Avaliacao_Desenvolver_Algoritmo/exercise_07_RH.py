print("Bem vindo ao Sistema automatizado de RH!")
print()

idade_minima = 18
nota_minima = 7

while True:
    cargo = input("Digite o cargo que deseja concorrer: ")
    nome_completo = input("Digite seu nome completo: ")
    email = input("Digite o seu melhor e-mail: ")
    idade = int(input("Digite sua idade: "))
    mensagem = "Parabéns " + nome_completo + "! Você passou para a próxima fase!"
    if idade < idade_minima:
        mensagem = "Prezado(a) " + nome_completo + "! Obrigado pela sua participação no processo seletivo para o cargo: " + cargo
        print(mensagem)
        break
    print(mensagem)

    curso = input("Digite o nome do curso que você tem: ")
    curso_qualificacao = input("Esse curso é de graduação? (s/n) ").lower()
    if curso_qualificacao != 's':
        mensagem = "Prezado(a) " + nome_completo + "! Obrigado pela sua participação no processo seletivo para o cargo: " + cargo
        print(mensagem)
        break
    print(mensagem)
    
    nota = float(input("Digite a sua nota na avaliação técnica: "))
    if nota < nota_minima:
        mensagem = "Prezado(a) " + nome_completo + "! Obrigado pela sua participação no processo seletivo para o cargo: " + cargo
        print(mensagem)
        break
    print(mensagem)

