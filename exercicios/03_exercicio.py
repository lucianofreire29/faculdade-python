n1= float(input("digite a nota 1:"))
n2= float(input("digite a nota 2:"))

med= (n1+n2)/2


def media():
    if med >=7:
        return "aprovado"
    else:
        return "reprovado"

print(f"sua nota:{med:.1f} \nsituação:{media()}")