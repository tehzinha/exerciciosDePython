
x1=x2=0
while True:
    a=float(input("Digite o valor do A:"))
    b=float(input("Digite o valor do B:"))
    c=float(input("Digite o valor do C:"))

    delta=(pow(b,1/2)-4*a*c)
    print(delta)
    if (delta<0):
        print("esse resultado não é válido, portanto não poderá continuar a equação")
    else:
        x1= float((-b + pow (delta,1/2)/2*a))
        x2= float((-b - pow(delta,1/2)/2*a))
    print(f'O valor de X1 é: {x1:.2f}')
    print(f'O valor de X2 é: {x2:.2f}')

    

