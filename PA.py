numero=int(input("Digite o numero:"))
termos=[numero]

for i in range(1,6):
    proximoTermo=termos[i-1]+2
    termos.append(proximoTermo)

print("Os 5 numeros dessa PA são:")
for termo in termos:
    print(termo)