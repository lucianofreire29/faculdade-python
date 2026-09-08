valor = input("digite o valor do investimento: ")

valor = valor.replace("R$", "").strip()

if "," in valor:
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

valor = float(valor)



def investimento():
    if valor < 1000:
        return "Perfil iniciante:Sugerimos Tesouro Direto"
    elif valor >= 1000 and valor <= 5000:
        return "Perfil moderado: Sugerimos fundos imobiliários"
    else:
        return "Perfil arrojado: Sugerimos Ações"

print(investimento())