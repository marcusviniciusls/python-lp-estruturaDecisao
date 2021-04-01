value = input("Digite o primeiro valor: ")
valorA = int(value)

value = input("Digite o segundo valor: ")
valorB = int(value)

if(valorB == 0):
    print("Não é possível dividir um número por zero")
else:
    resultado = valorA / valorB
    print("Resultado: ", str(resultado))