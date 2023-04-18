import time

prod = str(input("Informe o nome do produto escolhido: "))
quant = int(input("Informe a quantidade do produto escolhido: "))
val = float(input("Informe o valor do produto R$ "))

time.sleep(2)

cal = (quant * val)

pag = int(input("Qual a forma de pagamento:\n01-Dinheiro \n02-Cartão de Credito \n03-Pix \nResposta: "))

if pag == 1:
    print("O valor do produto {} será de R$ {:.2f}".format(prod, cal))

elif pag == 2:
    print("O valor do produto {} será de R$ {:.2f}".format(prod, cal))

elif pag == 3:
    print("O valor total do produto {} será de R$ {:.2f}".format(prod, cal))

else:
    print("A opção escolida é invalida !")
