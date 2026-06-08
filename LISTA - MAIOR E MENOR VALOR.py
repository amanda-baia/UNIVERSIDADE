#LER 5 NÚMEROS E GUARDAR UMA LISTA:
print('-'*30)
while True:

    numeros = []
    mai = 0
    men = 0
    lista = []
    for c in range(0, 5):
          lista.append(int(input(f'Insira um número inteiro para a posição {c}:')))
          if c == 0:
             mai = men = lista[0]
          else:
             if lista[c] > mai:
                 mai = lista[c]
                 if lista[c] < men:
                    men = lista[c]

    print ('-' * 30)
    print (f'Você digitou os valores {lista}')
    print ('-' * 30)


    print(f'O maior valor sorteado foi o {mai}, nas posições ', end='')

    for i, v in enumerate(lista):
        if v == mai:
            print(f'{i}... ', end='')

    print ('-' * 30)

    print(f'O menor valor sorteado foi o {men} , nas posições ', end='')
    for i, v in enumerate(lista):
        if v == men:
            print(f'{i}...', end='')

        print ('-' * 30)


    resposta = input('Quer continuar? [S/N]:')
    if resposta == 'n' or resposta == 'N':
        print('FIM DO PROGRAMA. Hasta luego!')
        break


print ('-' * 30)


