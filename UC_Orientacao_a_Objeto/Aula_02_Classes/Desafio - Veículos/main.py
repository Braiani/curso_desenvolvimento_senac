from Eletrico import Eletrico
from Automotor import Automotor
from PropulsaoHumana import PropulsaoHumana

perguntas = ['ocupacao','autonomia','combustivel','estilo_vida']

def exibe_carros_atendidos(carros_atendidos):
    print("--------//----------//----------------//-------------------//-----------")
    for carro in carros_atendidos:
        print(carro.exibir_informacoes())
        print("--------//----------//----------------//-------------------//-----------")

def atualiza_carros_disponiveis_baseado_resposta(pergunta, resposta, carros_disponiveis):
    novo_carros_disponiveis = []
    for carro in carros_disponiveis:
        if carro.atende_requisito(pergunta, resposta):
            novo_carros_disponiveis.append(carro)
    return novo_carros_disponiveis
    

carros_disponiveis = [
    Automotor("Gasolina", 200, "Aluguel", 4, 2, 1500, "Ferrari", "F250", 2020, "Vermelha", 1500000),
    Automotor("Diesel", 180, "Particular", 4, 5, 1800, "Ford", "Ranger", 2022, "Branca", 180000),
    Automotor("Gasolina", 250, "Aluguel", 4, 4, 1600, "Porsche", "Cayman", 2024, "Preto", 160000),
    Automotor("Etanol", 300, "Particular", 4, 5, 1800, "Lamborghini", "Huracan", 2023, "Laranja", 180000),
    Automotor("Diesel", 220, "Aluguel", 4, 4, 1600, "Toyota", "Hilux", 2024, "Prata", 160000),
    Automotor("Gasolina", 280, "Particular", 4, 5, 1700, "Maserati", "Ghibli", 2022, "Vermelho", 170000),
    Automotor("Gasolina", 150, "Particular", 2, 1, 200, "Honda", "CBR1000RR", 2023, "Vermelha", 20000),
    Automotor("Gasolina", 100, "Particular", 2, 1, 180, "Harley-Davidson", "Sportster Iron 883", 2022, "Preto", 18000),
    Automotor("Etanol", 80, "Particular", 2, 1, 160, "Yamaha", "MT-07", 2024, "Azul", 16000),
    Automotor("Gasolina", 180, "Particular", 2, 1, 220, "BMW", "R1250GS Adventure", 2023, "Prata", 22000),
    Automotor("Gasolina", 120, "Particular", 2, 1, 200, "Kawasaki", "Vulcan S", 2022, "Verde", 20000),
    Automotor("Etanol", 200, "Particular", 4, 5, 1800, "Jaguar", "F-Type", 2020, "Amarelo", 180000),
    Automotor("Gasolina", 320, "Aluguel", 4, 4, 1700, "McLaren", "570S", 2024, "Preto", 170000),
    Automotor("Diesel", 300, "Transporte Público", 6, 40, 12000, "Mercedes-Benz", "O500 RSD", 2023, "Branco", 1200000),
    Automotor("Diesel", 250, "Transporte Público", 6, 30, 10000, "Volvo", "B340M", 2022, "Azul", 1000000),
    Automotor("Diesel", 280, "Transporte Público", 6, 35, 11000, "Scania", "K360", 2024, "Vermelho", 1100000),
    Automotor("Diesel", 320, "Transporte Público", 6, 45, 13000, "MAN", "Lion's Coach", 2023, "Amarelo", 1300000),
    Automotor("Diesel", 270, "Transporte Público", 6, 38, 11500, "Iveco", "Crossway", 2022, "Prata", 1150000),
    Automotor("Gasolina", 350, "Particular", 4, 5, 1800, "Bugatti", "Chiron", 2022, "Azul", 1800000),
    Automotor("Gasolina", 400, "Particular", 4, 5, 1900, "Pagani", "Huayra", 2023, "Prata", 1900000),
    Automotor("Diesel", 400, "Carga Pesada", 8, 2, 15000, "Volvo", "FH16", 2023, "Branco", 1500000),
    Automotor("Diesel", 350, "Carga Pesada", 8, 2, 14000, "Scania", "R500", 2022, "Vermelho", 1400000),
    Automotor("Diesel", 380, "Carga Pesada", 8, 2, 14500, "Mercedes-Benz", "Actros", 2024, "Azul", 1450000),
    Automotor("Diesel", 420, "Carga Pesada", 8, 2, 15500, "MAN", "TGX", 2023, "Verde", 1550000),
    Automotor("Diesel", 360, "Carga Pesada", 8, 2, 13500, "DAF", "XF", 2022, "Amarelo", 1350000),
    Automotor("Gasolina", 250, "Particular", 4, 5, 1500, "Chevrolet", "Onix", 2023, "Prata", 80000),
    Automotor("Diesel", 180, "Transporte Público", 4, 20, 2500, "Mercedes-Benz", "Sprinter", 2022, "Branca", 180000),
    Automotor("Etanol", 200, "Particular", 4, 5, 1600, "Toyota", "Corolla", 2024, "Azul", 100000),
    Automotor("Gasolina", 300, "Particular", 4, 4, 1700, "Honda", "Civic", 2023, "Preto", 120000),
    Automotor("Etanol", 180, "Particular", 4, 5, 1600, "Ford", "Ka", 2023, "Vermelho", 60000),
    Automotor("Diesel", 220, "Particular", 4, 5, 2000, "Volvo", "XC60", 2022, "Cinza", 220000),
    Automotor("Gasolina", 280, "Particular", 4, 5, 1650, "Hyundai", "HB20", 2023, "Preto", 85000),
    Automotor("Gasolina", 320, "Particular", 4, 5, 1800, "Kia", "Sportage", 2024, "Azul", 110000),
    Automotor("Etanol", 190, "Particular", 4, 5, 1650, "Fiat", "Argo", 2023, "Vermelho", 70000),
    Automotor("Gasolina", 260, "Particular", 4, 5, 1550, "Jeep", "Compass", 2023, "Preto", 95000),
    Automotor("Etanol", 210, "Particular", 4, 5, 1700, "Peugeot", "208", 2024, "Branco", 80000),
    Automotor("Diesel", 240, "Particular", 4, 5, 1900, "Land Rover", "Discovery", 2022, "Cinza", 250000),
    Automotor("Gasolina", 300, "Particular", 4, 5, 1700, "Audi", "A3", 2023, "Preto", 125000),
    Automotor("Etanol", 190, "Particular", 4, 5, 1600, "Volkswagen", "Golf", 2024, "Prata", 90000),
    Automotor("Diesel", 230, "Particular", 4, 5, 1800, "BMW", "X1", 2022, "Azul", 180000),
    Eletrico(1500, 520, "Particular", 4, 10, 2000, "Tesla", "Model X", 2024, "Azul", 200000),
    Eletrico(1300, 480, "Particular", 4, 5, 1800, "Nissan", "Leaf", 2023, "Verde", 180000),
    Eletrico(1600, 550, "Particular", 4, 5, 1900, "Audi", "e-tron", 2022, "Prata", 190000),
    Eletrico(1400, 500, "Aluguel", 4, 4, 1700, "BMW", "i3", 2024, "Cinza", 170000),
    Eletrico(1700, 600, "Particular", 4, 5, 2000, "Mercedes-Benz", "EQC", 2022, "Roxo", 200000),
    Eletrico(1400, 480, "Aluguel", 4, 4, 1600, "Hyundai", "Kona Electric", 2024, "Branco", 160000),
    Eletrico(1600, 600, "Particular", 4, 5, 1900, "Kia", "EV6", 2022, "Verde", 190000),
    Eletrico(1800, 650, "Particular", 4, 5, 2000, "Polestar", "2", 2020, "Cinza", 200000),
    Eletrico(1700, 620, "Aluguel", 4, 4, 1600, "Rivian", "R1T", 2024, "Laranja", 160000),
    Eletrico(600, 300, "Particular", 4, 5, 1800, "Tesla", "Model 3", 2023, "Branco", 150000),
    Eletrico(500, 250, "Particular", 4, 5, 1700, "Nissan", "Leaf", 2023, "Prata", 90000),
    Eletrico(700, 350, "Particular", 4, 5, 1900, "BMW", "i3", 2024, "Azul", 120000),
    Eletrico(550, 280, "Particular", 4, 5, 1750, "Audi", "e-tron", 2023, "Branco", 140000),
    Eletrico(650, 320, "Particular", 4, 5, 1850, "Jaguar", "I-Pace", 2024, "Prata", 160000),
    Eletrico(600, 300, "Particular", 4, 5, 1800, "Porsche", "Taycan", 2023, "Vermelho", 170000),
    Eletrico(700, 350, "Particular", 4, 5, 1950, "Renault", "Zoe", 2023, "Branco", 130000),
    Eletrico(500, 250, "Particular", 4, 5, 1700, "Mitsubishi", "Outlander", 2023, "Prata", 95000),
    Eletrico(600, 300, "Particular", 4, 5, 1800, "Mini", "Cooper SE", 2024, "Vermelho", 125000),
    Eletrico(650, 330, "Particular", 4, 5, 1900, "Volvo", "XC40 Recharge", 2023, "Branco", 155000),
    Eletrico(550, 270, "Particular", 4, 5, 1650, "Citroën", "C4 elétrico", 2023, "Azul", 110000),
    Eletrico(600, 320, "Particular", 4, 5, 1850, "Ford", "Mustang Mach-E", 2024, "Vermelho", 160000),
    Eletrico(700, 360, "Particular", 4, 5, 2000, "Polestar", "2", 2023, "Branco", 170000),
    Eletrico(500, 260, "Particular", 4, 5, 1750, "Mazda", "MX-30", 2023, "Prata", 100000),
    PropulsaoHumana(26, 1200, "Bicicleta", 2, 1, 15, "Caloi", "Elite", 2023, "Vermelha", 1000),
    PropulsaoHumana(29, 1230, "Bicicleta", 2, 1, 14, "Specialized", "Rockhopper", 2022, "Preta", 1500),
    PropulsaoHumana(20, 450, "Patinete", 2, 1, 8, "Xiaomi", "Mi Electric Scooter", 2024, "Branco", 1200),
    PropulsaoHumana(24, 720, "Triciclo", 3, 2, 25, "Huffy", "Green Machine", 2021, "Verde", 800),
    PropulsaoHumana(26, 1220, "Bicicleta", 2, 1, 12, "Trek", "Marlin", 2023, "Azul", 1800),
    PropulsaoHumana(27, 2020, "Bicicleta", 2, 1, 11, "Scott", "Aspect", 2022, "Laranja", 1600),
    PropulsaoHumana(20, 1620, "Patinete", 2, 1, 7, "Segway", "Ninebot ES2", 2023, "Cinza", 1100),
    PropulsaoHumana(22, 1020, "Bicicleta", 2, 1, 10, "Giant", "TCR Advanced", 2022, "Preto", 2000),
    PropulsaoHumana(24, 1200, "Triciclo", 3, 2, 30, "Schwinn", "Meridian", 2021, "Vermelho", 1000),
    PropulsaoHumana(26, 1920, "Bicicleta", 2, 1, 13, "Cannondale", "Trail", 2024, "Amarela", 1700),
    PropulsaoHumana(26, 1200, "Bicicleta", 2, 2, 150, "Caloi", "Elite 30", 2023, "Preto", 2000),
    PropulsaoHumana(29, 800, "Triciclo", 2, 1, 120, "Specialized", "S-Works", 2022, "Vermelho", 8000),
    PropulsaoHumana(24, 1500, "Patinete", 3, 2, 180, "Trek", "Fuel EX", 2024, "Verde", 10000),
    PropulsaoHumana(27, 1000, "Bicicleta", 2, 1, 130, "Giant", "Trance", 2022, "Azul", 9500),
    PropulsaoHumana(25, 1300, "Triciclo", 3, 2, 170, "Cannondale", "Scalpel", 2024, "Preto", 12000),
    PropulsaoHumana(28, 900, "Patinete", 2, 1, 140, "Specialized", "Epic", 2023, "Verde", 8500),
    PropulsaoHumana(30, 1100, "Bicicleta", 3, 2, 160, "Scott", "Spark", 2023, "Preto", 13500),
    PropulsaoHumana(23, 1600, "Triciclo", 3, 2, 190, "Santa Cruz", "Blur", 2024, "Laranja", 15000),
    PropulsaoHumana(26, 1200, "Patinete", 2, 1, 140, "Yeti", "SB100", 2023, "Azul", 11000),
    PropulsaoHumana(29, 900, "Bicicleta", 3, 2, 175, "Orbea", "Occam", 2023, "Verde", 12500),
    PropulsaoHumana(27, 1100, "Triciclo", 3, 2, 170, "GT", "Sensor", 2024, "Preto", 11500),
    PropulsaoHumana(24, 1400, "Patinete", 2, 1, 150, "Canyon", "Lux", 2023, "Vermelho", 10500),
    PropulsaoHumana(28, 1000, "Bicicleta", 3, 2, 165, "BMC", "Fourstroke", 2023, "Preto", 14000),
    PropulsaoHumana(25, 1200, "Triciclo", 3, 2, 160, "Merida", "Big Nine", 2024, "Laranja", 13000),
    PropulsaoHumana(30, 800, "Patinete", 2, 1, 145, "Yeti", "SB115", 2023, "Azul", 11500)
]

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

resposta_valida = False

while not resposta_valida:
    ocupacao = int(input("""
    1. Qual é a sua ocupação principal?
    (1) Estudante
    (2) Profissional liberal
    (3) Empresário(a)
    (4) Trabalhador(a) CLT
    (5) Aposentado(a)
    Escolha a opção: """))
    
    if ocupacao in range(1,6):
        resposta_valida = True
    else:
        print("Opção inválida!")

carros_disponiveis = atualiza_carros_disponiveis_baseado_resposta('ocupacao', ocupacao, carros_disponiveis)
print()
print(f"Separamos {len(carros_disponiveis)} veículos com sua resposta")

if len(carros_disponiveis) <= 1:
    if len(carros_disponiveis) == 1:
        print("Veja abaixo o seu carro ideal: \n")
        exibe_carros_atendidos(carros_disponiveis)
    print("Obrigado por usar nossos seriços!\n")
    exit()

if input("Deseja ver os veículos separados (s para ver)? ").lower() == 's':
    exibe_carros_atendidos(carros_disponiveis)
    print()
    print("Gostou das recomendações? Deseja continuar a procura?")
    if input("Digite s para sair ou qualquer outra tecla para continuar... ").lower() == "s":
        print("\nObrigado por usar nosso sistema!\n")
        exit()

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


carros_disponiveis = atualiza_carros_disponiveis_baseado_resposta('estilo_vida', estilo_vida, carros_disponiveis)
print()
print(f"Separamos {len(carros_disponiveis)} veículos com sua resposta")

if len(carros_disponiveis) <= 1:
    if len(carros_disponiveis) == 1:
        print("Veja abaixo o seu carro ideal: \n")
        exibe_carros_atendidos(carros_disponiveis)
    print("Obrigado por usar nossos seriços!\n")
    exit()

if input("Deseja ver os carros separados (s para ver)? ").lower() == 's':
    exibe_carros_atendidos(carros_disponiveis)
    print()
    print("Gostou das recomendações? Deseja continuar a procura?")
    if input("Digite s para sair ou qualquer outra tecla para continuar... ").lower() == "s":
        print("\nObrigado por usar nosso sistema!\n")
        exit()

resposta_valida = False

while not resposta_valida:
    viajante = int(input("""
    3. Com que frequência você viaja longas distâncias (mais de 100 km)?
    (1) Regularmente (pelo menos uma vez por semana)
    (2) Com frequência (duas a três vezes por mês)
    (3) Ocasionalmente (uma vez por mês)
    (4) Raramente (menos de uma vez por mês)
    Escolha a opção: """))

    if viajante in range(1,5):
        resposta_valida = True
    else:
        print("Opção inválida!")


carros_disponiveis = atualiza_carros_disponiveis_baseado_resposta('autonomia', viajante, carros_disponiveis)
print()
print(f"Separamos {len(carros_disponiveis)} veículos com sua resposta")

if len(carros_disponiveis) <= 1:
    if len(carros_disponiveis) == 1:
        print("Veja abaixo o seu carro ideal: \n")
        exibe_carros_atendidos(carros_disponiveis)
    print("Obrigado por usar nossos seriços!\n")
    exit()

if input("Deseja ver os carros separados (s para ver)? ").lower() == 's':
    exibe_carros_atendidos(carros_disponiveis)
    print()
    print("Gostou das recomendações? Deseja continuar a procura?")
    if input("Digite s para sair ou qualquer outra tecla para continuar... ").lower() == "s":
        print("\nObrigado por usar nosso sistema!\n")
        exit()

resposta_valida = False

while not resposta_valida:
    combustivel = int(input("""
    4. Qual é a importância de características como economia de combustível e manutenção para você ao escolher um veículo?
    (1) Muito importante
    (2) Neutro
    (3) Pouco importante
    Escolha a opção: """))

    if combustivel in range(1,4):
        resposta_valida = True
    else:
        print("Opção inválida!")


carros_disponiveis = atualiza_carros_disponiveis_baseado_resposta('combustivel', combustivel, carros_disponiveis)
print()
print(f"Separamos {len(carros_disponiveis)} veículos com sua resposta")

if len(carros_disponiveis) <= 1:
    if len(carros_disponiveis) == 1:
        print("Veja abaixo o seu carro ideal: \n")
        exibe_carros_atendidos(carros_disponiveis)
    print("Obrigado por usar nossos seriços!\n")
    exit()

exibe_carros_atendidos(carros_disponiveis)
print()