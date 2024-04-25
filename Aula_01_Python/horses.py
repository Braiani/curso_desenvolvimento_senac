haras = int(input("Quantos cavalos foram comprados? "))

if haras < 0:
    print("Não é possível número negativo!")
    exit()

print(f"Você precisará de {haras * 4} ferraduras!")