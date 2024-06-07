saldo=20
cachorroQuente=10
milho=10
bauruSimples=5
hamburguer=51
cheeseburguer=6.28
refrigerante=5
print("Cardápio:\n Cachorro quente 1:$10\n Milho 2:10\n Bauru Simples 3:$5\n Hambúrguer 4:$5\n Cheeseburguer 5:%6.28\n Refrigerante 6:$5")
print("Seu saldo é de $20")
while True:
    pedido=float(input("Digite o número do seu pedido:"))
    if pedido==1:
        saldo=(saldo-cachorroQuente)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    elif pedido==2:
        saldo=(saldo-milho)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    elif pedido==3:
        saldo=(saldo-bauruSimples)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    elif pedido==4:
        saldo=(saldo-hamburguer)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    elif pedido==5:
        saldo=(saldo-cheeseburguer)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    elif pedido==6:
        saldo=(saldo-refrigerante)
        if saldo<=0:
            print("Seu saldo acabou!")
            break
        else:
            print("Seu saldo é:",saldo)
    

    
    

   
    
