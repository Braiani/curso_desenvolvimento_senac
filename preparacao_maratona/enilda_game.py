'''
Crie um jogo de quiz com perguntas e respostas, onde o jogador acumula pontos ao acertar as respostas.
Exemplo de Saída:
Qual é a capital do Brasil?
Sua resposta: Br
Resposta incorreta.
Quem escreveu 'Dom Quixote'?
Sua resposta: n sei
Resposta incorreta.
Quanto é 2 + 2?
Sua resposta: 4
Resposta correta!
Você fez 1 pontos.
'''
score = 0
questionario = {
    'Qual a capital do Brasil?': 'Brasília',
    'Quanto é 2 + 2?': '4',
    'Quem descobriu o Brasil?': 'Pedro Alvares Cabral',
    'São Paulo é a cidade mais limpa do Mundo?': 'Não'
}

print("""
+========================================================================================================+
|                                     Game Full - Um Quiz diferente!                                     |
+========================================================================================================+""")
print(f"Seu score atual: {score}")

for pergunta, resposta in questionario.items():
    resposta_usuario = input(pergunta + " ")
    if resposta_usuario == resposta:
        print("Resposta correta!")
        score += 1
    else:
        print("Resposta incorreta.")

print(f"Sua pontuação final: {score}")