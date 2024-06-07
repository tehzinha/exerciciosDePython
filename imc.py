def imc(peso,altura):
    return(peso/(altura*altura))

peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
resultado=imc(peso,altura)
print("Seu imc é:",resultado)

if (resultado<18.5):
    print("Voce esta abaixo do peso")
elif(resultado >=25 and resultado <=29.9):
    print("Voce esta no peso normal")
elif(resultado >=30 and resultado <=34.9):
    print("Voc esta acima do peso")
elif(resultado >=35 and resultado<=39.9):
    print("Voce esta no nivel de obesidade 2")
elif(resultado >=40):
    print("VOce esta no nivel de obesidade 3")
