vendas = [1500,2000,800,3500,1200]

tvendas = sum(vendas)

medvendas = tvendas / len(vendas)

maiorvendas = max(vendas)
menorvendas = min(vendas)

print(f"total de vdnas na semana: {tvendas}")
print(f"media de vendas: {medvendas}")
print(f"valor maior de vendas: {maiorvendas}, valor menor de vendas:{menorvendas}")
