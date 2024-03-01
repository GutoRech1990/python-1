print('Bem vindo a Pizzaria do José Augusto Rech')
print('|--------------------Cardapio-------------------|')
print('|Codigo | Descricao |Pizza Media-M|PizzaGrande-G|')
print('|    21 | Napolitana| R$ 20,00    | R$ 26,00    |')
print('|    22 | Marguerita| R$ 20,00    | R$ 26,00    |')
print('|    23 | Calabresa | R$ 25,00    | R$ 32,50    |')
print('|    24 | Toscana   | R$ 30,00    | R$ 39,00    |')
print('|    25 | Portuguesa| R$ 30,00    | R$ 39,00    |')
print('|_______________________________________________|')
acumulador = 0
while True:
    tamanho = input('Entre com o tamnho de pizza desejado ( M ou G )')
    tamanho = tamanho.upper()
    if tamanho != 'M' and tamanho != 'G':
        print('Opcao invalida, escolha outro tamanho')
        continue #se o usuario digitar algo invlido, volta para o comeco do while
    codigo = input('Entre com o codigo da pizza desejada ( 21,22,23,24,25 )')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print('Opcao invalida, escolha outro codigo')
        continue
    if codigo == '21' and tamanho == 'M':
        print('Voce escolheu a pizza Napolitana tamanho M')
        acumulador += 20 #pegue o valor que tinha no acumulador e some com 20
    elif codigo == '21' and tamanho == 'G':
        print('Voce escolheu a pizza Napolitana tamanho G')
        acumulador += 26 #pegue o valor que tinha no acumulador e some com 26
    elif codigo == '22' and tamanho == 'M':
        print('Voce escolheu a pizza Marguerita tamanho M')
        acumulador += 20 #pegue o valor que tinha no acumulador e some com 20
    elif codigo == '22' and tamanho == 'G':
        print('Voce escolheu a pizza Marguerita tamanho G')
        acumulador += 26 #pegue o valor que tinha no acumulador e some com 26
    elif codigo == '23' and tamanho == 'M':
        print('Voce escolheu a pizza Calabresa tamanho M')
        acumulador += 25 #pegue o valor que tinha no acumulador e some com 25
    elif codigo == '23' and tamanho == 'G':
        print('Voce escolheu a pizza Calabresa tamanho G')
        acumulador += 32.50 #pegue o valor que tinha no acumulador e some com 32,50
    elif codigo == '24' and tamanho == 'M':
        print('Voce escolheu a pizza Toscana tamanho M')
        acumulador += 30 #pegue o valor que tinha no acumulador e some com 30
    elif codigo == '24' and tamanho == 'G':
        print('Voce escolheu a pizza Toscana tamanho G')
        acumulador += 39 #pegue o valor que tinha no acumulador e some com 39
    elif codigo == '25' and tamanho == 'M':
        print('Voce escolheu a pizza Portuguesa tamanho M')
        acumulador += 30 #pegue o valor que tinha no acumulador e some com 30
    elif codigo == '25' and tamanho == 'G':
        print('Voce escolheu a pizza Portuguesa tamanho G')
        acumulador += 30 #pegue o valor que tinha no acumulador e some com 30
    pedir_mais = input('Deseja pedir mais alguma pizza?(S para sim ou qualquer tecla para sair):')
    pedir_mais = pedir_mais.upper() # caso o usuario digite em minisculo
    if pedir_mais == 'S':
        continue
    else:
        print(f'O valor total a ser pag: R${acumulador:.2f}')
        break

