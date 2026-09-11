MENU = """
===== MENU =====
1 - Pagamento ou Boleto
2 - Entrega ou Atraso
3 - Outros assuntos
"""

print(MENU)

opcao = int(input("Escolha uma opção: "))


def filtro(opcao):
    match opcao:
        case 1:
            return "Encaminhado para o Financeiro"
        case 2:
            return "Encaminhado para a Logística"
        case 3:
            return "Encaminhado para o Suporte Geral"
        case _:
            return "Opção inválida!"


resultado = filtro(opcao)

print(resultado)