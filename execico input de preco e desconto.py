#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
#Calcule e exiba o valor do desconto e o preço final do produto (exercício da apostila - aula 2)

preco = float (input('Digite o preco do produto:'))
d = float (input('Digite o % de desconto:'))
desconto = preco * (d/100)
print(('o valor do desconto eh {}').format(desconto))
pfinal = preco - desconto
print(('o valor final eh {}').format(pfinal))




