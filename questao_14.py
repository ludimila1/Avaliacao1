cont=0
conte=0
vogal = "aeiou"
espaco=" "
frase=str(input("Digite uma frase: "))
for i in frase:
    if i in vogal:
        cont=cont+1
    elif i in espaco:
        conte=conte+1
print("Quantidade de vogal:",cont)        
print("Quantidade de espaço:",conte)
