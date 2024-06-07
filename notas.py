nome= 47

def calculoDaMedia(n1,n2,n3,n4,n5):
    return((n1+n2+n3+n4+n5)/5)

while True:
   n1=float(input("Digite a 1ª nota:"))
   n2=float(input("Digite a 2ª nota:"))
   n3=float(input("Digite a 3ª nota:"))
   n4=float(input("Digite a 4ª nota:"))
   n5=float(input("Digite a 5ª nota:"))
   media=calculoDaMedia(n1,n2,n3,n4,n5)
   print("A media é:",media)
   break

if (media<6):
       print(f"\033[31m Aluno {nome} tem a media {media}aluno reprovado")
elif ( media>=6):
       print(f"\033[33m Aluno {nome} tem a media {media} e esta na media")
elif (media >=7 and media <9):
       print(f"\033[32 Aluno {nome} tem a media {media} e foi bom]")
elif (media >=9 and media <=10):
       print(f"\033[34m Aluno {nome} tem a media {media} e foi muito bom]")




    