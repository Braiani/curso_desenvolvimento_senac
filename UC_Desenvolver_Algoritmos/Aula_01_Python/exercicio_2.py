def sucessor(numero):
    return numero + 1

def antecessor(numero):
    return numero - 1

num = int(input("Digite um número mágico: "))

print(
   f"""
            +------------------------------------+
            | O sucessor do número mágico é: {sucessor(num)}   |
            | O antecessor do número mágico é: {antecessor(num)} |
            +------------------------------------+
    """
    )