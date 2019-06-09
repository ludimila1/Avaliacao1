cont=0
vogal_espaco = "aeiou "
frase=str(input("Digite uma frase: "))
for i in frase:
    if i in vogal_espaco:
        cont=cont+1
print(cont)        
