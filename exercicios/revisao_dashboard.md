# Revisão para a AV1 - Dashboard Analítico em Python

Material de estudo baseado nas duas listas do professor Otonio Castro, de
02/10/2026. Cada arquivo tem o enunciado, a solução comentada e a saída esperada.
As questões 1 a 5 vêm do PDF `DOC-20261008-WA0207.pdf`; as questões 6 e 7
correspondem aos exercícios 1 e 2 de `DOC-20261008-WA0208.pdf` (Revisão 02).

## Arquivos e resultados

| Arquivo | Tema | Resultado principal |
| --- | --- | --- |
| [revisao_dashboard_q1.py](revisao_dashboard_q1.py) | Atualizar e adicionar chaves | Alon: 4500; Marcos: 2000 |
| [revisao_dashboard_q2.py](revisao_dashboard_q2.py) | Entrada, condição e consulta | Mouse: 120; produto ausente: mensagem de erro |
| [revisao_dashboard_q3.py](revisao_dashboard_q3.py) | Valores, soma e média | Total: 80000; média: 20000 |
| [revisao_dashboard_q4.py](revisao_dashboard_q4.py) | Lista dentro de dicionário | Média de Paula: 9.67 |
| [revisao_dashboard_q5.py](revisao_dashboard_q5.py) | Remoção e existência | Valor removido: 200; celular existe: True |
| [revisao_dashboard_q6.py](revisao_dashboard_q6.py) | Função, repetição e unpacking | Matriz: 45000 / 15000; Filial Sul: 12000 / 6000 |
| [revisao_dashboard_q7.py](revisao_dashboard_q7.py) | Quantidade e máximo | 5 chamados; máximo: 120 minutos |

## Como executar

No terminal, dentro da pasta do repositório:

```bash
python exercicios/revisao_dashboard_q1.py
python exercicios/revisao_dashboard_q2.py
```

Troque o número para executar as demais questões. Dependendo da instalação,
o comando será `python3` ou `py`. Não é necessário instalar bibliotecas.
Somente a questão 2 pede uma entrada; as demais usam os dados do enunciado.

## 1. Entenda as estruturas

```python
notas = [10, 9, 10]                    # Lista: coleção acessada por índice.
cliente = {"nome": "Paula", "idade": 25}  # Dicionário: pares chave/valor.
resultado = (29, 3)                    # Tupla: sequência imutável.
```

- `notas[0]` retorna `10`: o primeiro índice é zero.
- `cliente["nome"]` retorna `"Paula"`: no dicionário, usamos a chave.
- `desempenho["Paula"]` na questão 4 retorna a lista inteira `[10, 9, 10]`.

## 2. Operações que aparecem na prova

| Operação | O que faz | Exemplo |
| --- | --- | --- |
| `d[chave]` | Acessa o valor da chave | `clientes["Alon"]` |
| `d[chave] = valor` | Adiciona ou substitui um valor | `clientes["Marcos"] = 2000` |
| `d[chave] += valor` | Soma ao valor existente | `clientes["Alon"] += 1500` |
| `chave in d` | Verifica a existência da chave | `"celular" in produtos` |
| `d.values()` | Obtém os valores do dicionário | `vendas_regiao.values()` |
| `list(...)` | Cria uma lista | `list(vendas_regiao.values())` |
| `d.pop(chave)` | Remove a chave e retorna seu valor | `produtos.pop("radio")` |
| `sum(lista)` | Soma os elementos | `sum([10, 9, 10])` retorna `29` |
| `len(lista)` | Conta os elementos | `len([10, 9, 10])` retorna `3` |
| `max(lista)` | Encontra o maior elemento | `max([15, 45, 120])` retorna `120` |

**Média = soma dos valores / quantidade de valores.** Use `len()` para obter
a quantidade, sem depender de um número escrito manualmente no cálculo.

## 3. Entrada e condição: questão 2

```python
produto = input("Produto: ").strip().lower()
```

A entrada `"  MOUSE  "` passa a ser `"MOUSE"` com `strip()` e vira `"mouse"`
com `lower()`. `strip()` remove espaços apenas do começo e do fim.
`input()` retorna texto; neste exercício não precisamos converter para número.

```python
if produto in estoque:
    print(estoque[produto])
else:
    print("Produto não encontrado no sistema")
```

O `if` testa uma condição. Se for verdadeira, executa o primeiro bloco;
caso contrário, executa o `else`. A indentação (normalmente quatro espaços)
define quais instruções pertencem a cada bloco.

## 4. Funções e desempacotamento: questões 6 e 7

```python
def analisar_vendas(vendas):
    total = sum(vendas)
    media = total / len(vendas)
    return total, media

total_filial, media_filial = analisar_vendas([10000, 15000, 20000])
```

1. `def` define a função; o bloco só executa quando ela é chamada.
2. `vendas` é o parâmetro que recebe a lista enviada na chamada.
3. `return total, media` devolve uma tupla com dois valores, nessa ordem.
4. O desempacotamento guarda `45000` em `total_filial` e `15000.0` em `media_filial`.

**`return` e `print` têm funções diferentes:** `return` entrega um resultado
para quem chamou a função; `print` exibe uma informação na tela. Uma função
sem `return` explícito devolve `None`.

## 5. Repetição e mensagens formatadas

```python
for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]
```

O `for` percorre as chaves do dicionário. A cada volta, `filial` recebe um nome,
e `dados_filiais[filial]` obtém a lista de vendas correspondente.

```python
print(f"Total: R${total:.2f}")
```

O `f` permite inserir valores entre `{}`. `:.2f` exibe duas casas decimais;
usa ponto como separador e arredonda apenas a apresentação. Por isso a média
de Paula aparece como `9.67`, embora `29 / 3` tenha mais casas decimais.

## Erros comuns para revisar

- Usar `clientes["Alon"] = 1500` quando é necessário somar com `+=`.
- Procurar `"Mouse"` em um dicionário cuja chave é `"mouse"`, sem normalizar a entrada.
- Acessar uma chave inexistente com `d[chave]`: isso causa `KeyError`.
- Esquecer `values()`: percorrer um dicionário diretamente fornece suas chaves.
- Usar `sum()` quando se quer quantidade (`len()`) ou maior valor (`max()`).
- Usar `//` na média: ele faz divisão pelo piso; use `/` para este cálculo.
- Esquecer os dois-pontos em `if`, `else`, `for` e `def`, ou errar a indentação.
- Inverter as variáveis ao desempacotar: a ordem deve acompanhar o `return`.

As listas fornecidas são não vazias. Com uma lista vazia, calcular
`sum(lista) / len(lista)` causa `ZeroDivisionError` e `max(lista)` causa
`ValueError`. As funções das questões 6 e 7 pressupõem listas não vazias,
como as dos enunciados; não há média nem máximo definidos para uma lista vazia.

## Treino rápido sem olhar o código

1. Se Alon comprar mais 500 após a atualização, qual será seu faturamento?
2. O que acontece ao digitar `"  MONITOR "` na questão 2?
3. Qual é a diferença entre `len([15, 45, 10])` e `sum([15, 45, 10])`?
4. O que `produtos.pop("radio")` retorna? O produto continua no dicionário?
5. O que `analisar_vendas([100, 200, 300])` retorna?
6. Como guardar separadamente os resultados de `resumo_chamados([8, 20, 5])`?

### Confira depois de tentar

1. `5000`: 3000 + 1500 + 500.
2. A entrada vira `"monitor"` e o programa mostra a quantidade `30`.
3. `len()` retorna `3`; `sum()` retorna `70`.
4. Retorna `200`; a chave `"radio"` é removida.
5. A tupla `(600, 200.0)`.
6. `quantidade, maior_tempo = resumo_chamados([8, 20, 5])`: quantidade `3`, maior tempo `20`.

Para estudar, tente prever cada saída antes de executar. Depois altere um valor
e refaça o cálculo à mão. Por fim, reescreva as soluções consultando apenas os enunciados.
