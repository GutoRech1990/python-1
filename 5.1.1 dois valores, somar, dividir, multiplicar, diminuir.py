#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário
# qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/).
# Exiba na tela o resultado da operação desejada.
x = print(input('Digite um valor:'))
y = print(input('Digite outro valor:'))
operacao = print(input('Digite + para somar, - para subtrair, * para multiplicar ou / para dividir:'))
if (operacao == '+'):
    res = (x+y)
    print(f'O resultado é {res}')
elif (operacao == '-'):
    res = (x - y)
    print(f'O resultado é {res}')
elif (operacao == '*'):
    res = (x * y)
    print(f'O resultado é {res}')
elif (operacao == '/'):
    res = (x / y)
    print(f'O resultado é {res}')
