converter = input("Digite o que deseja converter: ")

try:
    print(f"{float(converter)}")
except ValueError:
    print("Conversão proibida!")