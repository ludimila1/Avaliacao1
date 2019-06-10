tamanho_metro=float(input("Quantos metros quadrados tem a área a ser pintada? "))
litro= tamanho_metro/3
if litro%18==0:
    lata=litro/18
    preco = lata * 80
    print ("latas",lata)
    print ("R$ ", preco)

else:
    lata=int(litro/18)+1
    preco = lata * 80
    print ("latas",lata)
    print ("R$ ", preco)
