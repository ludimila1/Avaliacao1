ganha=float(input("Quanto você ganha por hora? "))
trabalhada=int(input("Quantas horas você trabalha por mês? "))

salario=ganha*trabalhada
print("Seu salário bruto foi: ", salario)
inss=(salario*0.08)
print("INSS: ", inss)
sindicato=(salario*0.05)
print("Sindicato: ", sindicato)
ir=(salario*0.11)
print("Imposto de Renda: ", ir)
salariol= salario-(inss+sindicato+ir)
print("Salário Líquido: ", salariol)
