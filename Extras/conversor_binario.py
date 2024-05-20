numero = int(input("Digite o número: "))

i = numero

while i < 10**12:
    print(i)
    valido = False
    if i % numero == 0:
        valido = True
        for j in str(i):
            if int(j) > 1:
                valido = False
                break

    if valido:
        print(i)
        break

    i +=1

if not valido:
    print("-1")