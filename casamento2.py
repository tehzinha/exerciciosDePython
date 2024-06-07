listaDeConvidados=[]
itens=[]
while True:
    convidados=input("Digite o nome do convidado:")
   
    if convidados in listaDeConvidados:
        print("Este nome ja foi inserido, digite novamente:")
        continue
    if(convidados!='sair'):
        listaDeConvidados.append(convidados)
    else:
        break
while True:
    presente=input("Digite o presente:")
    if (presente!='sair'):
        itens.append(presente)
    else:
        break
for i in range(0,len(listaDeConvidados and itens)):
    print(f'convidado',{listaDeConvidados[i]}, 'ficou com',{itens[i]})