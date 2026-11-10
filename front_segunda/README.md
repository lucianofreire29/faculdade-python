# Meu App — cotações

O botão “Olá usuario” consulta o backend Python, que faz uma requisição à AwesomeAPI para obter as cotações de compra (`bid`) de dólar, euro e bitcoin em reais. Cada resultado mostra a data de atualização informada pela API.

## Executar

No terminal, a partir da raiz do repositório:

```sh
cd front_segunda
python -m pip install -r requirements.txt
python sistemabasico.py
```

Abra http://127.0.0.1:5000 e clique no botão. Use a página servida pelo Python; abrir o HTML diretamente ou pelo Live Server não conecta a rota do backend.

O servidor usa apenas o endereço local e pode ser encerrado com Ctrl+C. Não há banco de dados nesta etapa.

## API

- Endpoint: https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL
- Documentação: https://docs.awesomeapi.com.br/api-de-moedas

A consulta precisa de internet e está sujeita aos limites e ao cache do provedor. Falhas de conexão, demora e respostas inválidas aparecem como mensagem na página. O erro `getaddrinfo failed` indica que a máquina não conseguiu resolver o endereço da API; verifique a conexão/DNS da rede.
