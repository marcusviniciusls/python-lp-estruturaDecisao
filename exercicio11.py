value = input("Digite o valor total do Produto: ")
valorProduto = float(value)

print("1 - A vista em dinheiro ou cheque, recebe 10% de desconto")
print("2 - A vista no cartão de crédito, recebe 5% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em quatro vezes, preço normal de etiqueta mais juros de 7%")
value = input()
opcao = int(value)

if(opcao <= 0 or opcao >= 5):
    print("Opção inválida")
elif(opcao == 1):
    valorFinal = valorProduto * 0.9
    print("Valor Final: ", str(valorFinal))
elif(opcao==2):
    valorFinal = valorProduto * 0.95
    print("Valor Final: ", str(valorFinal))
elif(opcao==3):
    valorFinal = valorProduto / 2
    print("Valor Parcelado em duas parcelas de : R$ ", str(valorFinal))
else:
    valorFinal = (valorProduto * 1.07) / 4
    print("Valor Parcelado com juros de 7% em quatro parcelas de : R$ ", str(valorFinal))