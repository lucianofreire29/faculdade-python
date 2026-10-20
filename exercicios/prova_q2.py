valor_da_casa = float(input("digite o valor da casa: "))

salario =float(input("digite o valor do salario: "))

tempo_de_pagamento = float(input("digite o valor do tempo de pagamento: "))

if valor_da_casa > (salario * 0.3):
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")

prestacao = valor_da_casa / (tempo_de_pagamento * 12)
print(f"Valor da prestação: R$ {prestacao:.2f}")