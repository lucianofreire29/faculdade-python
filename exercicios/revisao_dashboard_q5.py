# QUESTÃO 5 - Limpeza de Banco de Dados (Setor de TI)
# Fonte: DOC-20261008-WA0207.pdf - Exercício Revisão AV1, exercício 5.
#
# ENUNCIADO
# O sistema de e-commerce descontinuou alguns produtos. Você tem o dicionário:
# produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}.
# O item "radio" deve ser removido por estar obsoleto. Crie um código que:
# 1. Remova o item "radio" do dicionário usando o método .pop().
# 2. Imprima o valor do produto que foi removido para fins de log.
# 3. Verifique se o produto "celular" ainda existe e imprima True ou False.

produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}

# pop() faz duas coisas: remove o par chave/valor e retorna o valor removido.
valor_removido = produtos.pop("radio")
print(f"Valor do produto removido: R$ {valor_removido:.2f}")

# A expressão com in já produz um booleano: não é preciso usar if/else aqui.
print("celular" in produtos)

# RESULTADO ESPERADO
# Valor do produto removido: R$ 200.00
# True
# PARA A PROVA: pop("radio") retorna 200, e não a palavra "radio".
