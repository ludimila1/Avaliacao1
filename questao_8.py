cont=0
resposta=input("Telefonou para a vítima? S/N ")
resposta.lower()
if resposta=="s":
    cont=cont+1

resposta=input("Esteve no local do crime? S/N ")
resposta.lower()
if resposta=="s":
    cont=cont+1
    
resposta=input("Mora perto da vítima? S/N ")
resposta.lower()
if resposta=="s":
    cont=cont+1

resposta=input("Devia para a vítima? S/N ")
resposta.lower()
if resposta=="s":
    cont=cont+1

resposta=input("Já trabalhou com a vítima? S/N ")
resposta.lower()
if resposta=="s":
    cont=cont+1

if cont==2:
    print("Suspeita")

elif cont==3 or cont==4:
    print("Cúmplice")

elif cont==5:
    print("Assassino")

else:
    print("Inocente")
    
