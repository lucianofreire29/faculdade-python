"""Problema 02: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato”.
"""

produto1 = float(input("digite o preço do produto 1: "))
produto2 = float(input("digite o preço do produto 2: "))
produto3 = float(input("digite o preço do produto 3: "))


if produto1<produto2 and produto1<produto3:
    print(f"o produto 1 e o mais barato, custando:{produto1}")
elif produto2<produto1 and produto2<produto3:
    print(f"o produto 2 e o mais barato, custando:{produto2}")
elif produto3<produto1 and produto3<produto2:
    print(f"o produto 3 e o mais barato, custando: {produto3}")