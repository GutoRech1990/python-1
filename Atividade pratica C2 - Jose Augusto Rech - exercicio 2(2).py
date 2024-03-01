#tela de boas vindas juntamento com as opcoes disponiveis no cardapio
print('Bem vindo a Sorveteria do José Augusto Rech')
print('_________________________________________________________________________________________________')
print('| Código |     Descricao        | Tamanho P (500 ml) | Tamanho M (1000 ml) | Tamanho G (2000 ml)|')
print('|-----------------------------------------------------------------------------------------------|')
print('|  TR    | Sabores Tradicionais |      R$ 6,00       |      R$ 10,00       |      R$ 18,00      |')
print('|  ES    | Sabores Especiais    |      R$ 7,00       |      R$ 12,00       |      R$ 21,00      |')
print('|  PR    | Sabores Premium      |      R$ 8,00       |      R$ 14,00       |      R$ 24,00      |')
print('-------------------------------------------------------------------------------------------------')
acumulador = 0 #acumulador de incio 0
while True: #criação do loop
    tamanho = input('Digite o tamanho do pote de sorvete desejado (P,M,G):')
    tamanho = tamanho.upper() #forçar o tamanho com caracter maiusculo
    codigo = input('Digite o codigo do sorvete desejado ( TR, ES, PR):')
    codigo = codigo.upper() #forçar o código com caracter maiusculo
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G' or codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('Tamanho ou Código inválido(s).')
        continue #caso o usuário tenha digitado o tamnho errado, voltara para o inicio
    if codigo == 'TR' and tamanho == 'P':
        print('Voce escolheu o sabor tradicional no tamanho P')
        acumulador += 6 # o valor que tinha no acumulador será somado com 6
    elif codigo == 'TR' and tamanho == 'M':
        print('Voce escolheu o sabor tradicional no tamanho M')
        acumulador += 10 # o valor que tinha no acumulador será somado com 10
    elif codigo == 'TR' and tamanho == 'G':
        print('Voce escolheu o sabor tradicional no tamanho G')
        acumulador += 18 # o valor que tinha no acumulador será somado com 18
    elif codigo == 'ES' and tamanho == 'P':
        print('Voce escolheu o sabor especial no tamanho P')
        acumulador += 7 # o valor que tinha no acumulador será somado com 7
    elif codigo == 'ES' and tamanho == 'M':
        print('Voce escolheu o sabor especial no tamanho M')
        acumulador += 12 # o valor que tinha no acumulador será somado com 12
    elif codigo == 'ES' and tamanho == 'G':
        print('Voce escolheu o sabor especial no tamanho G')
        acumulador += 21 # o valor que tinha no acumulador será somado com 21
    elif codigo == 'PR' and tamanho == 'P':
        print('Voce escolheu o sabor premium no tamanho P')
        acumulador += 8 # o valor que tinha no acumulador será somado com 8
    elif codigo == 'PR' and tamanho == 'M':
        print('Voce escolheu o sabor premium no tamanho M')
        acumulador += 14 # o valor que tinha no acumulador será somado com 14
    elif codigo == 'PR' and tamanho == 'G':
        print('Voce escolheu o sabor premium no tamanho G')
        acumulador += 24 # o valor que tinha no acumulador será somado com 24
    mais_pedido = input('Deseja pedir mais algum sorvete? Digite "S" para sim ou qualquer outra tecla para sair:')
    mais_pedido = mais_pedido.upper()
    if mais_pedido == 'S':
        continue # caso o usuario digite S para fazer mais pedidos, voltará para a tela de pedidos
    else:
        print(f'O valor total a pagar da sua compra é de R${acumulador:.2f}')
        break # encerrando o loop caso não tenha mais pedidos a ser feito