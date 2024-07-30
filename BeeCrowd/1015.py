# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
x1, y1 = input().split(" ")
x2, y2 = input().split(" ")
resultado = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5
print(f"{resultado:.4f}")