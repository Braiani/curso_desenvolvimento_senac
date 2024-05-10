print("""
Enunciado do exercício:
    9 - Em uma eleição presidencial existem quatro candidatos. 
        Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: 
        1,2,3,4 = voto para os respectivos candidatos; 
        5 = voto nulo; 
        6 = voto em branco; 

    Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de dados, considere o código zero. 
        Ao final, calcule e escreva: 
        total de votos para cada candidato; 
        - total de votos nulos; 
        - total de votos em branco;
""")

votos = [0,0,0,0]
votos_nulos = 0
votos_brancos = 0

while True:
    voto = int(input("Digite o seu voto: "))

    if voto == 0:
        break

    if voto < 0 or voto > 6:
        print("Voto não computado!")
        continue

    if voto == 5:
        votos_nulos += 1
        continue
    
    if voto == 6:
        votos_brancos += 1
        continue
    
    votos[voto - 1] += 1

print(f"""
+===============+==================
| Candidato 1   |  {votos[0]}
| Candidato 2   |  {votos[1]}
| Candidato 3   |  {votos[2]}
| Candidato 4   |  {votos[3]}
+---------------+------------------
|  Votos nulos  |  {votos_nulos}
| Votos brancos |  {votos_brancos}
+===============+==================
""")