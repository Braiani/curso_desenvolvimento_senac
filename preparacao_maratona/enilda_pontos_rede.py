"""
O engenheiro de uma empresa precisa calcular a quantidade de cabos de rede necessários para instalar um laboratório com "n" pontos de redes.
O engenheiro sabe que a distância entre cada ponto de rede será de "r" metros (razão) e que o comprimento total dos cabos é igual à soma das
distâncias entre todos os pontos de rede.
Para facilitar o cálculo, o engenheiro decidiu usar uma Progressão Aritmética (PA) para representar as distâncias entre os pontos de rede.
Você precisa escrever um programa Python que ajude o engenheiro a calcular a quantidade de cabos de rede necessários. Seu programa deve:
- Solicitar ao usuário os dados de entrada da PA que é dado por: a + (n-1)*r, onde "a" é o primeiro termo, "n" é o número de termos e "r" é a razão da progressão.
- Calcular total dos cabos de rede necessário, que é igual à soma dos termos de todos os pontos de rede. Exibir na tela a quantidade de cabos de rede
    necessários para instalar o laboratório.
- Exibir também quinto termo e o termo central da progressão aritmética.
- Para calcular o termo central o programa deve somar o 1º e ultimo termo da Progressão Aritmética e dividir por 2.
Por fim, o programa deve retornar uma lista com os termos da PA e ser testado com diferentes valores de "n" e "r" para garantir que ele esteja
funcionando corretamente e produzindo resultados precisos.
"""
try:
    pontos = []
    pa = int(input("Digite o primeiro termo da PA: "))
    r = float(input("Digite a razão: "))
    termos = int(input("Digite a quantidade de termos: "))

    i = 0
    pontos.append(pa)
    soma = pa
    while i < (termos - 1):
        atual = pa + (i + 1)*r
        soma += atual
        pontos.append(atual)
        i += 1
    
    print(pontos)
    if len(pontos) >= 5:
        print(f"O quinto termo é: {pontos[4]}")
    print(f"O termo central é: {(pontos[0] + pontos[termos-1])/2}")
    print(f"Soma dos termos: {soma}")
except:
    print("Um erro ocorreu!")