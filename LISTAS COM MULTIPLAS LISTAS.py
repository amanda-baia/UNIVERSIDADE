#Expor a lista dentro da lista.

#Exemplo simples : galera = [['João', 19], ['Ana', 33],
#         ['Joaquim', 13], ['Maria', 45]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade.')

#Criando as Variáveis
galera = []
dado = []
totmai = totmen = 0

#Abrindo as opções para inserir o nome e idade dentro de uma lista de 3 pessoas:
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()

#Mostrar os maiores de idade:

for p in galera:
    if p[1] >= 18:
        print (f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print ('-' * 30)

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')

