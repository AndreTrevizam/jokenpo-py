from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0,2)

print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador=int(input('Qual a sua jogada? '))

print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!')
sleep(1)
print('-=' * 11)

print(f'O computador jogou: {itens[cpu]}')
print(f'Você jogou: {itens[jogador]}')
print(f'-=' * 11)

#verificar PEDRA
if cpu == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('Jogador VENCEU!')

    elif jogador == 2:
        print('Jogador PERDEU!')

    else:
        print('Jogada invalida')

#verificar PAPEL
elif cpu == 1:
    if jogador == 0:
        print('Jogador PERDEU!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('Jogador VENCEU!')

    else:
        print('Jogada invalida')

#verificar TESOURA
elif cpu == 2:
    if jogador == 0:
        print('Jogador VENCEU')                     

    elif jogador == 1:
        print('Jogador PERDEU!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('Jogada invalida')