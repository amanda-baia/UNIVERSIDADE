# 0-20 - Expor por extenso

#Criando a lista:
cont = ('zero','um','dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze','quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
#Limitando os valores ao intervalo 0-20:
    while True:
        num = int(input ('Insira um valor entre 0 e 20:'))
        if 0 <= num <= 20:
            break
        print('Tente novamente, valor inválido!')
        print('-' * 30)

    #Escrever por extenso:
    print(f' Você digitou o número {cont[num]}')
    print('-'*30)

    #Condição de parada para o programa:
    resposta = input('Quer continuar? [S/N]:')

    if resposta == 'n' or resposta == 'N':
        break

print('FIM DO PROGRAMA. Hasta luego!')


