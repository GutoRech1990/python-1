#escreva um algoritimo que leia um valor e que imprima a quantidade de cedulas
#necessarias para pagar esse mesmo valor
#Para simplificar, vamos trabalhar apenas com valores inteiros e com cedulas de R$ 100, 50, 20, 10, 5, 1

valor = int (input('Digite um valor:'))
if valor >= 100:
    cedulas100 = valor // 100
    valor -= cedulas100 * 100
    print(f'Cedulas de 100 : {cedulas100}')
if valor >= 50:
    cedulas50 = valor // 50
    valor -= cedulas50 * 50
    print(f'Cedulas de 50 : {cedulas50}')
if valor >= 20:
    cedulas20 = valor // 20
    valor -= cedulas20 * 20
    print(f'Cedulas de 20 : {cedulas20}')
if valor >= 10:
    cedulas100 = valor // 10
    valor -= cedulas100 * 10
    print(f'Cedulas de 10 : {cedulas100}')
if valor >= 5:
    cedulas5 = valor // 5
    valor -= cedulas5 * 5
    print(f'Cedulas de 5 : {cedulas5}')
if valor:
    cedulas1 = valor
    print(f'Cedulas de 1 : {cedulas1}')