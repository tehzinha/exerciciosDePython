def idade(ano):
    return(2023-ano)
feminino=1
masculino=2

nome=(input("Digite seu nome:"))
ano=int(input("Digite o ano em que nasceu:"))
print("Digite 1 para feminino e 2 para masculino")
sexo=(input("Digite seu sexo:"))
if sexo==1:
    sexo=feminino
elif sexo==2:
    sexo=masculino
resultado=idade(ano)

if resultado==40 and sexo==masculino:
    print("É necessário fazer um exame de próstata")
elif resultado==30 and sexo==feminino:
    print("É necessário fazer um exame mamário")
print("Seu nome é",nome,"seu sexo é",sexo,"e sua idade é",resultado)