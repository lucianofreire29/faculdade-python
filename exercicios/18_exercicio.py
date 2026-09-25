produtos_baguncados = ["iphone 13", "MACBOOK PRO", "airPoDs Pro","iPad mini", "caixa de som bluetooth"]



def padronizar_texto(texto):
    return texto.strip().title()



for  produtos in produtos_baguncados:
    print(padronizar_texto(produtos))

