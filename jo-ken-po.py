import random
pedra=1
papel=2
tesoura=3

jogue=int(input("Digite sua jogada:"))

if jogue==1:
    computador=random.randint(1,4)
    if computador==1:
        print("O jogador escolheu pedra empatou")
    elif computador==2:
        print("O jogador escolheu papel voce perdeu")
    elif computador==3:
        print("O jogador escolheu tesoura voce ganhou")
elif jogue==2:
    computador=random.randint(1,4)
    if computador==1:
        print("O jogador escolheu pedra voce ganhou")
    elif computador==2:
        print("O jogador escolheu papel empatou")
    elif computador==3:
        print("O jogador escolheu tesoura voce perdeu")
elif jogue==3:
    computador=random.randint(1,4)
    if computador==1:
        print("O jogador escolheu pedra voce perdeu")
    elif computador==2:
        print("O jogador escolheu papel voce ganhou")
    elif computador==3:
        print("O jogador escolheu tesoura empatou")
