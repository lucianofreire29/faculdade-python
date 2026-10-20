cardapio = {100: ("cachorroQuente", 15.00), 101:("bauruSimples", 10.00), 102:("bauruComOvo", 10.00), 103:("hamburguer", 15.00), 104:("cheeseburguer", 17.00), 105:("refrigerante", 7.00)}


total_pedido = 0
total_item = 0

print("Bem-vindo ao cardápio do nosso restaurante!")
print("-------- Cardápio -------- ")
for codigo, (nome, preco) in cardapio.items():
    print(f"Código: {codigo} - {nome} - R${preco:.2f}")

while True:
    codigo_pedido = int(input("Digite o código do item que deseja pedir (ou 0 para finalizar): "))
    if codigo_pedido == 0:
        break
    quantidade = int(input("Digite a quantidade desejada: "))
    if codigo_pedido in cardapio:
        nome_item, preco_item = cardapio[codigo_pedido]
        total_item = preco_item * quantidade
        total_pedido += total_item
        print(f"Item adicionado: {nome_item} - R${preco_item:.2f} x {quantidade} = R${total_item:.2f}  ")
    else:
        print("Código inválido. Por favor, tente novamente.")

print(f"Total do pedido: R${total_pedido:.2f}")
