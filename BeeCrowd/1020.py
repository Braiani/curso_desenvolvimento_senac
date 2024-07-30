# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
idade = int(input())
anos = 0
meses = 0
dias = 0
while idade > 365:
    anos += 1
    idade -= 365
while idade >= 30:
    meses += 1
    idade -= 30
dias = idade
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")