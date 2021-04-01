value = input("Digite o dia: ")
dia = int(value)

value = input("Digite o mês: ")
mes = int(value)

if(dia < 1 or dia > 31 or mes < 1 or mes > 12):
    print("Data inválidaA")
elif((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia > 31 or dia < 1)):
    print("Data inválidaB")
elif((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30)):
    print("Data inválidaC")
elif((mes == 2) and (dia < 1 or dia > 28)):
    print("Data inválidaD")
else:
    print("Data válidaE: ", str(dia), "/", str(mes))