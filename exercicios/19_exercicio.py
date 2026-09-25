
def imposto (valor_servico):
    if valor_servico > 5000:
        imposto = valor_servico * 0.05
    else:
        imposto = valor_servico * 0.03
    return imposto

print (f"O imposto ISS do valor de R$5.000,00: R${imposto(8000):.2f}")
print (f"O imposto ISS do valor de R$2.000,00: R${imposto(2000):.2f}")