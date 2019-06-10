medias=[]
contador=0
notas=0
for i in range(10):
  for j in range(4):
    nota=float(input('Digite a nota '+ str(j+1) + ' do aluno: ' ))
    notas=nota+notas
    media= notas/4
  print(" ")
  if media > 7.0 or media==7.0:
    contador=1+contador
  else:
    contador=0+contador
  notas=0
  print('O numero de alunos com notas maior que 7.0 é = ',contador)
