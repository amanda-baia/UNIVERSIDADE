#CRIAR UMA TUPLA COM PRODUTOS E PREÇOS EM SEQUÊNCIA

produtos = ('Borracha',2,
            'Lápis', 1.50,
            'Apontador', 1.20,
            'Caderno', 12,
            'Agenda', 9,
            'Lápis de cor', 16,
            'Livro', 34.90)

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f' {produtos[pos]:.<29}', end ='')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')
print('-'*40)

