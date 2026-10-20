'''deposito_inicial = float(input("Digite o valor do depósito inicial: "))

juros = float(input("Digite a taxa de juros (em %): "))

tempo = int(input("Digite o tempo de aplicação (em meses): "))

montante = deposito_inicial * (1 + juros / 100) ** tempo

print(f"O montante final é: {montante:.2f}")'''


#vendas = [2000,5000,1000,8000,3000]

'''comissao_total = 0


for venda in vendas:
    if venda > 4000:
        comissao = 0.10
    else:
        comissao = 0.05
    print(f"Venda: {venda:.2f} - Comissão: {comissao * venda:.2f}")'''

'''meta = {"janeiro": 1000, "fevereiro": 1200, "março": 1100}

gastos = {"janeiro": 900, "fevereiro": 1350, "março": 1100}


for mes in meta:
    if mes in gastos:
        if gastos[mes] > meta[mes]:
            print(f"No mês de {mes}, a meta foi ultrapassada.")
        else:
            print(f"No mês de {mes}, a meta não foi ultrapassada.")
    else:
        print(f"Não há dados de gastos para o mês de {mes}.")'''


precos = {"celular": 1500,"tablet":2500,"notebook":5000}

percentual_aumento = float(input("Digite o percentual de aumento (em %): "))

for produto in precos:
    precos[produto] *= (1 + percentual_aumento / 100)

print("Preços atualizados:")
for produto, preco in precos.items():
    print(f"{produto}: R$ {preco:.2f}")