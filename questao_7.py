salario=int(input("Qual é o seu salário? "))
if salario<=280:
    atual=(salario*0.2)+salario
    print("O salário antes do reajuste:", salario)
    print("O percentual de aumento aplicado: 20%")
    print("O valor do aumento:",(salario*0.2))
    print("O novo salário depois do aumento:", atual)

elif salario>280 and salario<=700:
    atual=(salario*0.15)+salario
    print("O salário antes do reajuste:", salario)
    print("O percentual de aumento aplicado: 15%")
    print("O valor do aumento:",(salario*0.15))
    print("O novo salário depois do aumento:", atual)

elif salario>700 and salario<=1500:
    atual=(salario*0.10)+salario
    print("O salário antes do reajuste:", salario)
    print("O percentual de aumento aplicado: 10%")
    print("O valor do aumento:",(salario*0.10))
    print("O novo salário depois do aumento:", atual)

elif salario>1500:
    atual=(salario*0.05)+salario
    print("O salário antes do reajuste:", salario)
    print("O percentual de aumento aplicado: 5%")
    print("O valor do aumento:",(salario*0.05))
    print("O novo salário depois do aumento:", atual)
    

