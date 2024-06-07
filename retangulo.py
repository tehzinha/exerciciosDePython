
def perimetro(lado,lado2,lado3,lado4):
    return(lado+lado2+lado3+lado4)
lado=lado3=0
lado2=lado4=0
print("Quer saber o perímetro de algum retangulo?")
lado=float(input("Digite o valor do primeiro lado:"))
lado2=float(input("DIgite o valor do outro lado:"))

resultado=perimetro(lado,lado2,lado3,lado4)
print("O perimetro desse retangulo é:", resultado)