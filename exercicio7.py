import math

value = input("Digite um valor: ")
valor = int(value)

if valor > 0:
    raizQuadrada = math.sqrt(valor)
    print("Raiz Quadrada: ", str(raizQuadrada))
else:
    print("O valor não tem possibilidade de operar com raiz quadrada")

