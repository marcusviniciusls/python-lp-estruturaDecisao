value = input("Digite a quantidade de dias utéis no mês: ")
diaUtil = int(value)

value = input("Digite a quantidade de horas trabalhadas no mês: ")
horasTrabalhadasMes = int(value)

value = input("Digite o seu valor/hora: ")
valorHora = int(value)

horasUtilMes = diaUtil * 8

if(horasUtilMes > horasTrabalhadasMes):
    valorAdicional = (horasUtilMes - horasTrabalhadasMes) * valorHora
    salario = valorHora * horasUtilMes
    salarioTotal = valorAdicional + salario
    print("O valor de Horas Extras: ", str(valorAdicional))
    print("O valor do salário: ", str(valorAdicional))
    print("Salário Total: ", str(salarioTotal))
else:
    print("Você trabalhou menos que o esperado no mês: ")
    salario = valorHora * horasUtilMes
    print("Salário Total: ", str(salario))




