aux = input("Digite um valor: ")
valor = int(aux)

aux = input("Digite outro valor: ")
valorSegundo = int(aux)

if(valor == valorSegundo):
    print("Os números são iguais")
elif(valor > valorSegundo):
    print("Número Maior", str(valor))
else:
    print("Número Maior", str(valorSegundo))

