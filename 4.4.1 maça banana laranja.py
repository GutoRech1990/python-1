#Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas.
# Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
#Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
# Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85.

print('Qual produto voce gostaria de comprar?')
print('1 - Maca')
print('2 - Laranja')
print('3 - Banana')

produto = int (input('Qual sua escolha?'))
qtd = int (input('Qual a quantidade?'))

if ( produto == 1):
    pagar = (qtd * 2.30)
    print(f'Voce comprou {qtd} maca(s). O valor a pagar eh de {pagar}' )
else:
    if (produto == 2):
        pagar = (qtd*3.60)
        print(f'Voce comprou {qtd} laranja(s). O valor a pagar eh de {pagar}')
    else:
        if (produto == 3):
            pagar = (qtd*1.85)
            print(f'Voce comprou {qtd} banana(s). O valor a pagar eh de {pagar}')
        else:
            print('Produto inexistente')






