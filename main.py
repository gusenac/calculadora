
operacao = input("Digite a operacao desejada (soma, subtração, multiplicação, divisão): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "soma":
	resultado = int(numero1) + int(numero2)
if operacao == "subtração":
	resultado = int(numero1) - int(numero2)
if operacao == "multiplicação":
	resultado = int(numero1) * int(numero2)
if operacao == "divisão":
	resultado = int(numero1) / int(numero2)
    
print("O resultado é : " + str(resultado))