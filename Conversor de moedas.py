#Conversor de moedas

n1 = float(input('Insira o primeiro valor em reais: '))

#Considere 1 dolar = 3,27 reais

print('O valor em dolar é {:.2f}:'.format(n1/3.27))
print ('Com R${:.2f} você pode comprar US$ {:.2f}'.format(n1, n1/3.27))



