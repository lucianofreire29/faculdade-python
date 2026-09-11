vendas_vend = float(input("digite as suas vendas: "))
meta_ind = float(input("digite sua meta individual: "))
vendas_loja = float(input("digite a venda da loja: "))
meta_total = float(input("digite a meta da loja: "))

def bater():
    if vendas_vend >=meta_ind and vendas_loja >= meta_total:
        bonus = 20
        bonus_des = (bonus/100)*vendas_vend
        
    else:
        bonus = 0
        bonus_des=(bonus/100)*vendas_vend
    return bonus_des

bonus_des = bater()

print (f"seu bonus este mes e de: {bonus_des}")
