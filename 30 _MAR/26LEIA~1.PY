#26. Leia um número inteiro. Classifique o número de acordo com as seguintes regras Se for maior que 0. Se for menor que 10 exiba Pequeno. Se estiver entre 10 e 100 exiba Médio. Se for maior que 100 exiba Grande. Caso contrário, exiba Negativo ou zero

n = int (input ("Insira um número"))

if (n >= 0) and (n < 10):
    print ("Pequeno")
elif (n >= 10) and (n < 100):
    print ("Médio")
elif (n > 100):
    print ("Grande")
else:
    print ("Negativo ou Zero")