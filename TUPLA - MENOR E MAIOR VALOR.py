# O PROGRAMA VAI GERAR 5 NUMEROS ALEATORIOS E COLOCAR EM UMA TUPLA

#Importar números inteiros aleatoriamente:
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10),randint(1, 10))

print('-'*30)

#MOSTRAR A LISTAGEM DE NÚMEROS GERADOS
print(f'Os valores sorteados foram:')
for n in numeros:
    print(f'{n} ', end='')

#INDICAR O MENOR E MAIOR VALOR DA TUPLA
print('-'*30)
print(f' \n O maior valor sorteado foi {max(numeros)}')
print(f' \n O menor valor sorteado foi {min(numeros)}')