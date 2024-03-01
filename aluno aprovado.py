#Um aluno, para passar de ano, precisa estar aprovado em todas as matérias que ele está cursando.
#Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias,
# somente. Escreva um algoritmo que leia a nota final do aluno em cada matéria, e informe na tela se ele passou de ano ou não.

m1 = float(input('Digite a nota da materia 1:'))
m2 = float(input('Digite a nota da materia 2:'))
m3 = float(input('Digite a nota da materia 3:'))

if m1 >=7 and m2 >=7 and m3 >=7:
    print('O aluno esta aprovado')
else:
    print('O aluno esta reprovado')


