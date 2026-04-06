# 30. Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja possível, exiba: “Entrada inválida”; Caso seja possível: Verifique se o número é par: Se for par e maior que 100 → exiba: “Par alto”; Se for par e menor ou igual a 100 → exiba: “Par baixo”; Caso não seja par, exiba: “Ímpar”.

a = (input("Digite um valor:"))

try:
    n = int(a)
    if (n % 2 == 0):
        if (n > 100):
            print ("Par alto")
        else:
            print ("Par baixo")
    else:
        print ("Ímpar")

except:
    print ("Entrada inválida!")
