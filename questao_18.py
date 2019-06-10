dia=int(input("Digite o dia: "))
mes=int(input("digite o mes: "))
ano= int(input("digite o ano: "))
cont=0
meses=[" ","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
for i in range(13):
    if dia>31 or dia<1:
        break
    elif mes>13 or mes<1:
        break
    elif i==mes:
        print(dia," de ",meses[i], " de ", ano )
        cont=cont+1


    
    


