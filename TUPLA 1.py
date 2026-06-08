lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

#Ignorando o último ítem, vou contar quantos itens possuo na tupla:
#for c in range(0, len(lanche)):
#    print(c)

#Mostrando todos os nomes:
# c = contagem dos números
#for c in range(0, len(lanche)):
   # print(f'Eu vou comer {lanche[c]} na posição {c}')


#Poderia fazer usando for - mostrando todos:

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')


