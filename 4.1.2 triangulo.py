#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
#a) Equilátero (três lados iguais);
#b) Isósceles (dois lados iguais);
#c) Escaleno (três lados diferentes).
#Lembre-se de que, para formar um triangulo, nenhum dos lados pode ser igual a zero
# e um lado não pode ser maior do que a soma dos outros dois.

a = int (input('Digite a medida do lado A ( maior que zero ):'))
b = int (input('Digite a medida do lado B( maior que zero ):'))
c = int (input('Digite a medida do lado C( maior que zero ):'))
if a == b == c:
    print('Todos os lados sao iguais. Voce tem um triangulo equilatero')
elif (a != b and a != c and b != c):
    print('Todos os lados sao diferentes. Voce tem um triangulo escaleno')
elif ( a == b and a != c or b == c and b != a or c == a and c != b):
    print('Dois dos tres lados sao iguais. Voce tem um triangulo isoceles')

    




