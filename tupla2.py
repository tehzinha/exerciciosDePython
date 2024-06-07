tuplaValor=(5,6,80,90,100,200)
soma=0
for i in range(0, len(tuplaValor)):
    soma+=tuplaValor[i]
media=(soma)/len(tuplaValor)
print(f'A media é {media}')

menor=maior=0
for i in range(0,len(tuplaValor)):
    if(i==0):
        menor=maior=tuplaValor[i]
    else:
        if (tuplaValor[i]< menor):
            menor=tuplaValor[i]
        if (tuplaValor[i]>maior):
            maior=tuplaValor[i]
print(f'O menor valor é {menor}\nE o maior valor é{maior}')
