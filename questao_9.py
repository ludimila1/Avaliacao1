kgmorango=int(input("Quantidade em kilos de morango: "))
kgmaca=int(input("Quantidade em kilos de maçã: "))
if kgmorango<=5:
    valormorango=kgmorango*2.5
    print("O valor a ser pago de morango é: ","%.2f" % valormorango)

elif kgmorango>5 or kgmorango>6 or kgmorango>7 or kgmorango>=8:
    valormorango=kgmorango*2.2
    print("O valor a ser pago de morango é: ","%.2f" % valormorango)

elif kgmorango>8 or kgmorango>11:
    valormorango=(kgmorango*2.2)*0.1
    print("O valor a ser pago de morango é: ","%.2f" % valormorango)

if kgmaca<=5:
    valormaca=kgmaca*1.8
    print("O valor a ser pago de maçã é: ","%.2f" % valormaca)

elif kgmaca>5 or kgmaca>6 or kgmaca>7 or kgmaca>=8:
    valormaca=kgmaca*1.5
    print("O valor a ser pago de maçã é: ","%.2f" % valormaca)

elif kgmaca>8 or kgmaca>16:
    valormaca=(kgmaca*1.5)*0.1
    print("O valor a ser pago de maçã é: ","%.2f" % valormaca)
