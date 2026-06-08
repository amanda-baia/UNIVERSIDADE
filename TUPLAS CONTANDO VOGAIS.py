#CRIAR UMA TUPLA COM VÁRIAS PALAVRAS SEM ACENTO

pal = ('aprender', 'vencer', 'volei', 'viagem', 'nacional', 'estudar', 'campeonato')


#MOSTRAR AS VOGAIS DE CADA PALAVRA:
for i in pal:
    print(f'\n Na palavra {i.upper()} temos: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

