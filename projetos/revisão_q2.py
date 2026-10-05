
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = float(input("Há quantos anos você fuma? "))

total_cigarros = cigarros_por_dia * anos_fumando * 365
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (24 * 60)

print(f"Total de dias de vida perdidos: {dias_perdidos:.2f}")