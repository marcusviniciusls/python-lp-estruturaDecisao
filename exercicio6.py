value = input("Digite o valor A: ")
numberA = int(value)

value = input("Digite o valor B: ")
numberB = int(value)

if numberA % numberB == 0:
    print("O valor A é divisivel por B")
else:
    print("O valor A não é divisivel por B")