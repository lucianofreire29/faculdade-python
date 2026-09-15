precos = [100,250,500]
vinhos = ["branco","tinto","champagne"]

MENU = """
===== Vinhos =====
1 - branco
2 - tinto
3 - champagne
"""

print(MENU)

opcao = int(input("Escolha uma opção: "))

novopreco = int(input("digite o novo preço: "))

if opcao >= 1 and opcao <=3 :
    posicao = opcao - 1
    precos[posicao] = novopreco

print(vinhos)
print(precos)