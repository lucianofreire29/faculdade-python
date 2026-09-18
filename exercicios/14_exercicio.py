estoque = {"teclado":50, "mouse":120, "monitor":30}

produto = input("digite o nome do produto: ")

if produto in estoque:
    print(f"quantidade do produto: {estoque[produto]}")

else:
    print("produto indisponível")