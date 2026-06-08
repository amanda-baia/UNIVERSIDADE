#COLOCAÇÃO DOS 18 PRIMEIROS COLOCADOS NA TABELA DO CAMPEONATO DA VNL

times = ('Itália', 'Brasil', 'Japão', 'República Tcheca',
         'China', 'Polônia', 'Canadá', 'Estados Unidos',
         'Bélgica', 'Sérvia', 'Alemanha', 'Holanda',
         'Bulgária', 'Turquia', 'Ucrânia', 'Tailândia',
         'França', 'República Dominicana')

#Mostrar times em ordem de colocação:
print('-' * 30)
print(f' A lista de times da VNL 2026: {times}')
print('-' * 30)

# a) Mostrar os 5 primeiros:
print(f' Os 5 primeiros da Lista de times da VNL 2026 são: {times[0:5]}')
print('-' * 30)

# b) Os quatro últimos:
print (f' cOs quatro últimos da lista de times da VNL 2026: {times[-4:]}')
print('-' * 30)

# c) Os times em ordem alfabética:
print(f' Os times em ordem alfabética são:{sorted(times)} ')
print('-' * 30)

# d) A posição de um time específico:
print('-'*30)
pesquisa = input('Qual time você deseja buscar a posição? ').strip().title()

if pesquisa in times:
    posicao = times.index(pesquisa)
    print(f'O time {pesquisa} está na  {posicao}ª posição!')

    if pesquisa == 'Brasil':
        print("A rede treme, o Brasil inteiro vibra.🇧🇷🏐")
    elif pesquisa == 'Turquia':
        print("Foge enquanto dá, Karakurt!")

else:
    print(f'O time {pesquisa} não foi encontrado na tabela da VNL 2026.')

#Se fosse especifico: print(f'Os times Brasil está na {times.index("Brasil")+1}ª posição!')
print('-' * 30)

