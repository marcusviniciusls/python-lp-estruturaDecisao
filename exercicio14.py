value = input("Digite o Ano: ")
ano = int(value)

if(ano % 4 != 0):
    print("Ano não é bisexto")
elif(ano % 4 == 0 and ano % 100 != 0):
    print("Ano bisexto")
elif(ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print("Ano bisexto")
else:
    print("Ano não é bisexto")