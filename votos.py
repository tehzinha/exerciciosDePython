galego=0
thiago=0
maria=0

while True:
    print("Digite 1 para votar no canditato 1")
    print("Digite 2 para votar no canditato 2")
    print("Digite 3 para votar no canditato 3")
    print("DIgite 0 para encerrar a votação")

    tehzinha=int(input("Digite o número do seu voto"))

    if tehzinha == 0:
        break

    if tehzinha== 1:
        galego+=1
    elif tehzinha== 2:
        thiago+=1
    elif tehzinha== 3:
        maria+=1

    else:
        print("Voto Inválido")

print("Resultado da votação")
print("Tehzinha 1", galego,"votos")
print("Tehzinha 2", thiago, "votos")
print("Tehzinha 3", maria, "votos")


