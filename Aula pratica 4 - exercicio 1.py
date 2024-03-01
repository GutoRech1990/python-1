print ('Calculadora')
print (' + adicao')
print (' - subtracao')
print (' * multiplicacao')
print (' / divisao')
print (' Presione "s" para sair')
op = input ('Qual opercao deseja fazer?')
x = int (input('Digite um valor:'))
y = int (input('Digite outro valor:'))
while op != 's':
    if op == '+':
      res = x + y
      print(f'Resultado: {x} + {y} = {res}')
    elif op == '-':
      res = x - y
      print(f'Resultado: {x} - {y} = {res}')
    elif op == '*':
      res = x * y
      print(f'Resultado: {x} * {y} = {res}')
    elif op == '/':
      res = x / y
      print(f'Resultado: {x} / {y} = {res}')
    op = input('Qual opercao deseja fazer?')
    x = int(input('Digite um valor:'))
    y = int(input('Digite outro valor:'))