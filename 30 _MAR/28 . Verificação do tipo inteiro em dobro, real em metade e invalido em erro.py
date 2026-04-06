# 28. Leia um valor informado pelo usuário. Verifique o tipo da variável. Caso seja possível interpretá-lo como um valor numérico. Se for um número inteiro, exiba o dobro. Caso seja um número real, exiba a metade. Caso não seja possível interpretar como número, exiba Tipo inválido.

a = (input("Digite o primeiro valor: "))

print ("O tipo original é:", type(a))

try:
    numero = float(a)
    if numero.is_integer():
        numero = int (numero)
        print ("Dobro:", numero * 2)
    else:
        print ("Metade:", numero/2)

except:
    print ("Tipo inválido")

