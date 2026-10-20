distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco = distancia * 0.60
else:
    preco = distancia * 0.55

print(f"Preço da passagem: R$ {preco:.2f}")