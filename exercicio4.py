timeA = input("Digite o nome do Time A: ")
timeB = input("Digite o nome do Time B: ")

aux = input("Digite os gols do Time A: ")
golsA = int(aux)

aux = input("Digite os gols do Time B: ")
golsB = int(aux)

if(golsA == golsB):
    print("EMPATE!")
elif (golsA > golsB):
    print(str(timeA) ," Venceu!")
else:
    print(str(timeB) ," Venceu!")

