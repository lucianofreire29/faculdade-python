velocidade = float(input("Qual é a velocidade do carro em km/h? "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado!")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")