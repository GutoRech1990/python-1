x = int (input('Digite um valor:'))
y = int ( input('Digite outro valor:'))
cont = 1
multi = 0
while (cont <= x):
    multi = multi + y
    cont = cont + 1
print(f'O resultado de {x} x {y} é igual a {multi}')