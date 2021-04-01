value = input("Digite a média do primeiro semestre: ")
nota01 = float(value)

value = input("Digite a média do segundo semestre: ")
nota02 = float(value)

media = (nota01 * 4 + nota02 * 6) / (4+6)

value = input("Digite em % a sua frequencia: ")
frequencia = float(value)

if(frequencia < 70):
    print("Reprovado por falta")
elif(media < 4):
    print("Reprovado por Nota. Nota: ", str(media))
elif(media < 6):
    print("Exama. Nota: ", str(media))
else:
    print("Aprovado. Nota: " , str(media))