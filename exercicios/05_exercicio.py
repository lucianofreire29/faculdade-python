vtotal = float(input("digite o valor total da sua compra: "))



def desc():
    if vtotal >= 500:
        desconto = 15
        vdesconto = (desconto/100)*vtotal
        vfinal = vtotal - vdesconto
        
    elif vtotal < 500 and vtotal >= 200:
        desconto = 10
        vdesconto = (desconto/100)*vtotal
        vfinal = vtotal - vdesconto

    else:
        desconto = 0
        vdesconto = (desconto/100)*vtotal
        vfinal = vtotal - vdesconto
    return vdesconto , vfinal

vdesconto, vfinal = desc()

print(f"seu desconto é: R${vdesconto} \nvalor final a pagar:R${vfinal:.1f}")