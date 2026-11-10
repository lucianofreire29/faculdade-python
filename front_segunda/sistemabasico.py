from pathlib import Path
from decimal import Decimal, InvalidOperation

import requests
from flask import Flask, jsonify, render_template


PASTA = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(PASTA), static_folder=str(PASTA / "static"))
API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"


@app.get("/")
def inicio():
    return render_template("index.html")


@app.get("/api/cotacoes")
def pegar_cotacoes():
    try:
        resposta = requests.get(API_URL, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        cotacoes = []
        for codigo, nome in [("USD", "Dólar"), ("EUR", "Euro"), ("BTC", "Bitcoin")]:
            moeda = dados[f"{codigo}BRL"]
            valor = Decimal(moeda["bid"])
            if not valor.is_finite() or valor <= 0:
                raise ValueError("Cotação inválida")
            cotacoes.append({
                "moeda": nome,
                "codigo": codigo,
                "valor": str(valor),
                "atualizado_em": moeda["create_date"],
            })
        return jsonify(cotacoes=cotacoes)
    except requests.Timeout:
        return jsonify(erro="A API demorou para responder. Tente novamente."), 504
    except requests.RequestException:
        return jsonify(erro="Não foi possível consultar a API. Verifique a conexão e tente novamente."), 502
    except (ValueError, KeyError, TypeError, InvalidOperation):
        return jsonify(erro="A API retornou dados inválidos. Tente novamente mais tarde."), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
