largura = 0
comprimento = 0

while largura <= 0 or comprimento <= 0:
    largura = int(input("Digite a largura do terreno: "))
    comprimento = int(input("Digite o comprimento do terreno: "))

    if largura < 0 or comprimento < 0:
        print("Não é possível um tamanho negativo de terreno!", end="\n\n")

    if largura == comprimento:
        print("O terreno não é um retângulo!")
        largura = 0
        comprimento = 0
    
area = largura * comprimento

print(f"A área do terreno é {area} m²")