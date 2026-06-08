#Ler um programa que adiciona nome e peso de várias pessoas
from itertools import count

galera = []
dados = []
mai = men = 0

#Criar o input para adicionar os dados:
while True:

    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite o peso em kg: ')))

    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    galera.append(dados[:])
    dados.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'N':
        break

print ('-'*30)
print (f'Os dados foram {galera}')
print ('-'*30)

# Imprimir a quantidade de pessoas cadastradas:
print(f' A quantidade de pessoas cadastradas foi de: {len(galera)} pessoas')
print ('-'*30)
# Imprimir a listagem das pessoas mais pesadas:
print(f' O maior peso foi de {mai} Kg')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}')
print ('-'*30)

# Imprimir a listagem das pessoas mais leves:
print(f' O menor peso foi de {men} Kg')
print ('-'*30)