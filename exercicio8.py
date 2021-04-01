value = input("Digite a sua idade: ")
idade = int(value)

if(idade <5):
    print("Sua idade não tem categoria")
elif(idade <8):
    print("Infantil")
elif(idade < 11):
    print("Juvenil")
elif(idade < 16):
    print("Adolescente")
elif(idade < 31):
    print("Adulto")
else:
    print("Senior")