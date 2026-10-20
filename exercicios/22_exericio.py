candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos_candidatos = {codigo: 0 for codigo in candidatos}
votos_nulos = 0
votos_brancos = 0

print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Voto nulo")
print("6 - Voto em branco")
print("0 - Encerrar votação")

while True:
    voto = int(input("\nDigite o código do voto: "))

    if voto == 0:
        break
    elif voto in candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Código inválido. O voto não foi contabilizado.")

total_votos = sum(votos_candidatos.values()) + votos_nulos + votos_brancos

print("\nRESULTADO DA ELEIÇÃO")
for codigo, nome in candidatos.items():
    print(f"{nome}: {votos_candidatos[codigo]} voto(s)")

print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_brancos}")
print(f"Total de votos: {total_votos}")

if total_votos > 0:
    percentual_nulos = votos_nulos / total_votos * 100
    percentual_brancos = votos_brancos / total_votos * 100
else:
    percentual_nulos = 0
    percentual_brancos = 0

print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")