vendas_regiao={"norte":15000, "sul":22000, "leste": 18000, "oeste": 25000}

faturamento = list(vendas_regiao.values())

total = sum(faturamento)

media = total/len(faturamento)

print(f"o faturamento total: {total}\n e a media das regiões{media}")