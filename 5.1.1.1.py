print('Caluladora')
print('+ para adicao')
print('- para subtracao')
print('* para multiplicacao')
print('/ para divisao')
print('outra tecla para sair')

op = input('Qual operacao?')
x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))

if op == '+':
    res = x + y
    print(f'O resultado de {x} + {y} é {res}')
elif op == '-':
    res = x - y
    print(f'O resultado de {x} - {y} é {res}')
elif op == '*':
    res = x * y
    print(f'O resultado de {x} * {y} é {res}')
elif op == '/':
    res = x / y
    print(f'O resultado de {x} / {y} é {res}')
else:
    print('Opercao invalida')

print('Encerrando programa')