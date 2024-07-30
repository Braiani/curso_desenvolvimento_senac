# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n = int(input())
segundo = 0
minuto = 0
hora = 0
while n>0:
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
    n -= 1
print(f"{hora}:{minuto}:{segundo}")