import math

value = input("Digite o valor A: ")
A = float(value)

value = input("Digite o valor B: ")
B = float(value)
value = input("Digite o valor C: ")
C = float(value)

if(A == 0):
    print("Não é possível calcular a equação do segundo grau")
else:
    delta = (B*B) - 4 * A * C
    if(delta < 0):
        print("Raiz quadrada do delta negativa")
    else:
        deltaQuadrada = math.sqrt(delta)
        x1 = (- B + deltaQuadrada) / 2 * A
        x2 = (- B - deltaQuadrada) / 2 * A
        print("Delta: ", str(delta))
        print("X1: ", str(x1))
        print("X2: ", str(x2))