def soma(a,b):
    return(a+b)
def subtracao(a,b):
    return(a-b)
def multiplicação(a,b):
    return(a*b)
def divisão(a,b):
    return(a/b)


resposta=int(input("Digite 1 para soma\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão"))
a=float(input("Digite o primeiro valor:"))
b=float(input("Digite o segundo valor:"))
if resposta==1:
    print(soma(a,b))
elif resposta==2:
    print(subtracao(a,b))
elif resposta==3:
    print(multiplicação(a,b))
elif resposta==4:
    print(divisão(a,b))