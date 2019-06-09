numero=int(input("Digite um número inteiro de 1 até 10: "))
cont=1
if numero>=1 and numero<=10:
    while cont<=10:
        mult=numero*cont
        print (numero," X ", cont," = ", mult)
        cont=cont+1

else:
    print("Apenas números de 1 até 10")
