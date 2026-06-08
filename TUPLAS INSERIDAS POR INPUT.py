# LEIA 4 VALORES E GUARDE EM UMA TUPLA

num = (int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')))

print('-'*30)
print(f'Os valores digitados foram:{num}')

print('-'*30)

# A) QUANTAS VEZES APARECEU O VALOR 9:

print(f'O valor 9 apareceu {num.count(9)} vez(es)')
print('-'*30)

# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3:
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print("O valor 3 não foi digitado em nenhuma colocação")
print('-'*30)

# C) QUAIS OS NÚMEROS PARES:
for n in num:
    if n%2==0:
        print(f' O(s) número(s) par(es) apresentado(s) foi/foram: {n} ',end='')