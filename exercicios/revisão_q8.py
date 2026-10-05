numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ").strip()

if operacao == "+":
    print(f"Resultado: {numero1 + numero2}")
elif operacao == "-":
    print(f"Resultado: {numero1 - numero2}")
elif operacao == "*":
    print(f"Resultado: {numero1 * numero2}")
elif operacao == "/":
    if numero2 != 0:
        print(f"Resultado: {numero1 / numero2}")
    else:
        print("Não é possível dividir por zero.")
else:
    print("Operação inválida.")