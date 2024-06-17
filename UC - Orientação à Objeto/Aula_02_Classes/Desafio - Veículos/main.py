from Eletrico import Eletrico
from Automotor import Automotor

carros_disponiveis = {
    Eletrico(1500, 520, "Particular", 4, 10, 2000, "Tesla", "Model X", 2024, "Azul", 200000),
    Automotor("Gasolina", 200, "Aluguel", 4, 2, 1500, "Ferrari", "F250", 2023, "Vermelha", 1500000),
    Automotor("Diesel", 180, "Particular", 4, 5, 1800, "Ford", "Ranger", 2022, "Branca", 180000),
    Eletrico(1300, 480, "Particular", 4, 5, 1800, "Nissan", "Leaf", 2023, "Verde", 180000),
    Automotor("Gasolina", 250, "Aluguel", 4, 4, 1600, "Porsche", "Cayman", 2024, "Preto", 160000),
    Eletrico(1600, 550, "Particular", 4, 5, 1900, "Audi", "e-tron", 2022, "Prata", 190000),
    Automotor("Etanol", 190, "Oficial", 4, 5, 1700, "Chevrolet", "Camaro", 2023, "Amarelo", 170000),
    Eletrico(1400, 500, "Aluguel", 4, 4, 1700, "BMW", "i3", 2024, "Cinza", 170000),
    Automotor("Gasolina", 300, "Particular", 4, 5, 1800, "Lamborghini", "Huracan", 2023, "Laranja", 180000),
    Eletrico(1700, 600, "Particular", 4, 5, 2000, "Mercedes-Benz", "EQC", 2022, "Roxo", 200000),
    Automotor("Diesel", 220, "Aluguel", 4, 4, 1600, "Toyota", "Hilux", 2024, "Prata", 160000),
    Eletrico(1500, 550, "Oficial", 4, 5, 1800, "Volvo", "XC40 Recharge", 2023, "Azul", 180000),
    Automotor("Gasolina", 280, "Particular", 4, 5, 1700, "Maserati", "Ghibli", 2022, "Vermelho", 170000),
    Eletrico(1400, 480, "Aluguel", 4, 4, 1600, "Hyundai", "Kona Electric", 2024, "Branco", 160000),
    Automotor("Gasolina", 150, "Particular", 2, 1, 200, "Honda", "CBR1000RR", 2023, "Vermelha", 20000),
    Automotor("Gasolina", 100, "Particular", 2, 1, 180, "Harley-Davidson", "Sportster Iron 883", 2022, "Preto", 18000),
    Automotor("Gasolina", 80, "Particular", 2, 1, 160, "Yamaha", "MT-07", 2024, "Azul", 16000),
    Automotor("Gasolina", 180, "Particular", 2, 1, 220, "BMW", "R1250GS Adventure", 2023, "Prata", 22000),
    Automotor("Gasolina", 120, "Particular", 2, 1, 200, "Kawasaki", "Vulcan S", 2022, "Verde", 20000),
    Automotor("Etanol", 200, "Particular", 4, 5, 1800, "Jaguar", "F-Type", 2023, "Amarelo", 180000),
    Eletrico(1600, 600, "Particular", 4, 5, 1900, "Kia", "EV6", 2022, "Verde", 190000),
    Automotor("Gasolina", 320, "Aluguel", 4, 4, 1700, "McLaren", "570S", 2024, "Preto", 170000),
    Automotor("Diesel", 300, "Transporte Público", 6, 40, 12000, "Mercedes-Benz", "O500 RSD", 2023, "Branco", 1200000),
    Automotor("Diesel", 250, "Transporte Público", 6, 30, 10000, "Volvo", "B340M", 2022, "Azul", 1000000),
    Automotor("Diesel", 280, "Transporte Público", 6, 35, 11000, "Scania", "K360", 2024, "Vermelho", 1100000),
    Automotor("Diesel", 320, "Transporte Público", 6, 45, 13000, "MAN", "Lion's Coach", 2023, "Amarelo", 1300000),
    Automotor("Diesel", 270, "Transporte Público", 6, 38, 11500, "Iveco", "Crossway", 2022, "Prata", 1150000),
    Eletrico(1800, 650, "Particular", 4, 5, 2000, "Polestar", "2", 2023, "Cinza", 200000),
    Automotor("Gasolina", 350, "Particular", 4, 5, 1800, "Bugatti", "Chiron", 2022, "Azul", 1800000),
    Eletrico(1700, 620, "Aluguel", 4, 4, 1600, "Rivian", "R1T", 2024, "Laranja", 160000),
    Automotor("Gasolina", 400, "Particular", 4, 5, 1900, "Pagani", "Huayra", 2023, "Prata", 1900000),
    Automotor("Diesel", 400, "Carga Pesada", 8, 2, 15000, "Volvo", "FH16", 2023, "Branco", 1500000),
    Automotor("Diesel", 350, "Carga Pesada", 8, 2, 14000, "Scania", "R500", 2022, "Vermelho", 1400000),
    Automotor("Diesel", 380, "Carga Pesada", 8, 2, 14500, "Mercedes-Benz", "Actros", 2024, "Azul", 1450000),
    Automotor("Diesel", 420, "Carga Pesada", 8, 2, 15500, "MAN", "TGX", 2023, "Verde", 1550000),
    Automotor("Diesel", 360, "Carga Pesada", 8, 2, 13500, "DAF", "XF", 2022, "Amarelo", 1350000),
}


print()
print("////--------------------- Seja Bem vindo!!!! ---------------------\\\\\\\\")
print(" ----- Nesse sistema você conseguirá achar o seu veículo ideal -----")

print("--- Nosso sistema possui carros das seguintes marcas: ")
marcas = []
print(f"++{'-'*30}++" )
for carro in carros_disponiveis:
    if carro.exibir_marca() not in marcas:
        tamanho_nome = len(carro.exibir_marca()) 
        inicio = (30 - tamanho_nome) // 2
        fim = 30 - inicio - tamanho_nome
        print(f"||{inicio * ' '}{carro.exibir_marca()}{fim * ' '}||")
        marcas.append(carro.exibir_marca())
print(f"++{'-'*30}++" )

print(f"{'-' * 5} Vamos começar a escolher o seu carro!!!! {'-' * 5}")

print("Faremos algumas perguntas para entender melhor a sua situação atual!")

respostas = []
resposta_valida = False

while not resposta_valida:
    ocupacao = int(input("""
    1. Qual é a sua ocupação principal?
    (1) Estudante
    (2) Profissional liberal
    (3) Empresário(a)
    (4) Trabalhador(a) de escritório
    (5) Trabalhador(a) manual (ex.: construção, indústria)
    (6) Aposentado(a)
    Escolha a opção: """))
    
    if ocupacao in range(1,7):
        resposta_valida = True
    else:
        print("Opção inválida!")

respostas.append(ocupacao)

resposta_valida = False

while not resposta_valida:
    estilo_vida = int(input("""
    2. Como você descreveria seu estilo de vida?
    (1) Muito ativo, sempre em movimento
    (2) Moderadamente ativo, com algumas atividades ao ar livre
    (3) Principalmente tranquilo e urbano
    (4) Focado em família e lazer
    Escolha a opção: """))

    if estilo_vida in range(1,5):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(estilo_vida)

resposta_valida = False

while not resposta_valida:
    viajante = int(input("""
    3. Com que frequência você viaja longas distâncias (mais de 100 km)?
    (1) Regularmente (pelo menos uma vez por semana)
    (2) Com frequência (duas a três vezes por mês)
    (3) Ocasionalmente (uma vez por mês)
    (4) Raramente (menos de uma vez por mês)
    (5) Nunca
    Escolha a opção: """))

    if viajante in range(1,6):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(viajante)

resposta_valida = False

while not resposta_valida:
    combustivel = int(input("""
    4. Qual é a importância de características como economia de combustível e manutenção para você ao escolher um veículo?
    (1) Muito importante
    (2) Importante
    (3) Neutro
    (4) Pouco importante
    (5) Não é importante
    Escolha a opção: """))

    if combustivel in range(1,6):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(combustivel)

resposta_valida = False

while not resposta_valida:
    tecnologia = int(input("""
    5. Você tem preferência por algum tipo de tecnologia de assistência ao motorista (ex.: piloto automático, assistência de estacionamento)?
    (1) Sim, prefiro veículos com essas tecnologias
    (2) Neutro, não é um fator decisivo
    (3) Não, não tenho interesse em tecnologias avançadas
    Escolha a opção: """))

    if tecnologia in range(1,4):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(tecnologia)

resposta_valida = False

while not resposta_valida:
    pavimentacao = int(input("""
    6. Como você lida com condições adversas de tráfego (ex.: trânsito intenso, estradas não pavimentadas)?
    (1) Estou acostumado(a) e lido bem com isso
    (2) É um desafio, mas adapto-me
    (3) Evito condições adversas sempre que possível
    (4) Não enfrento essas condições frequentemente
    Escolha a opção: """))

    if pavimentacao in range(1,5):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(pavimentacao)

resposta_valida = False

while not resposta_valida:
    prioridades = int(input("""
    7. Qual é a sua prioridade ao escolher um veículo novo?
    (1) Conforto e espaço interno
    (2) Segurança e tecnologia
    (3) Desempenho e dirigibilidade
    (4) Economia de combustível
    Escolha a opção: """))

    if prioridades in range(1,5):
        resposta_valida = True
    else:
        print("Opção inválida!")


respostas.append(prioridades)


for carro in carros_disponiveis:
    print(f"- {carro.exibir_marca()} - {carro.exibir_modelo()}:", end=" ")
    if carro.atende_requisitos(respostas):
        print("Sim")
    else:
        print("Não")

