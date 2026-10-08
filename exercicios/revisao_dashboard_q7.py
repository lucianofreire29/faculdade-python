# QUESTÃO 7 - Gestão de Chamados de Suporte (Setor de TI)
# Fonte: DOC-20261008-WA0208.pdf - Revisão 02, exercício 2.
#
# ENUNCIADO
# O sistema de chamados precisa de um resumo diário. Crie uma função
# resumo_chamados que receba uma lista com tempos de resposta (em minutos).
# Ela deve retornar a quantidade de chamados e o tempo máximo de espera.
# Teste a função com a lista tempos = [15, 45, 10, 120, 30].
# Desempacote os resultados e exiba uma mensagem formatada alertando sobre
# o tempo máximo encontrado.


def resumo_chamados(tempos_resposta):
    # Como no enunciado, a lista deve conter pelo menos um tempo de resposta.
    quantidade = len(tempos_resposta)
    tempo_maximo = max(tempos_resposta)
    return quantidade, tempo_maximo


tempos = [15, 45, 10, 120, 30]

# A primeira variável recebe a quantidade; a segunda recebe o maior tempo.
quantidade, tempo_maximo = resumo_chamados(tempos)
print(
    f"Foram registrados {quantidade} chamados. "
    f"Atenção: o tempo máximo de espera foi de {tempo_maximo} minutos."
)

# RESULTADO ESPERADO (uma única linha)
# Foram registrados 5 chamados. Atenção: o tempo máximo de espera foi de 120 minutos.
# PARA A PROVA: len() conta os elementos; max() encontra o maior valor.
