dias_da_semana = [
    "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"
]

dia_digitado = int(input("Digite o número referente ao dia da semana: "))

if dia_digitado < 1 or dia_digitado > 7: 
    print("Durrrrrrrrrrrrrr... Não existe!")
else: 
    dia_digitado -= 1
    print(f"Você escolheu o dia {dias_da_semana[dia_digitado]}!")