def calculoDoQuadrado(lado):
    return (lado*lado)
def calculoDoCirculo(raio):
    return (3.14*(raio*raio))
def calculoDoRetangulo(base,altura):
    return (base*altura)
def calculoDoTrapezio(baseMenor,baseMaior,altura):
    return ((baseMaior+baseMenor)*altura)/2

print("Digite 1 para achar a area do quadrado")
print("Digite 2 para achar a area do circulo")
print("Digite 3 para achar a area do retangulo")
print("Digite 4 para achar a area do trapezio")

area=int(input("Digite o numero do calculo que quer achar"))

if area == 1:
    quadrado=float(input("Digite a medida do lado"))
    a=calculoDoQuadrado(quadrado)
    print("resultado é:", a, "metros")
elif area== 2:
    circulo=float(input("Digite a medida do raio"))
    b=calculoDoCirculo(circulo)
    print("o resultado é:", b,"metros")
elif area== 3:
    retangulo=float(input("Digite a medida da base"))
    Hretangulo=float(input("Digite a medida da altura"))
    c=calculoDoRetangulo(retangulo)
    print("o resultado é:", c,"metros")
elif area== 4:
    trapezio=float(input(" DIgite a medida da baseMenor"))
    Btrapezio=float(input(" Digite a medida da baseMaior"))
    Ctrapezio=float(input(" Digite a medida da altura"))
    d=calculoDoTrapezio(trapezio)
    print("o resultado é:", d, "metros")

print("GOSTOU DA NOSSA AJUDA?")







