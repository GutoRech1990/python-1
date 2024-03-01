# pedir a quantidade de KWh
#pedir o tipo de instalacao ( R residencial, I industrial, C comercio )
# residencial até 500 preco 0.40......acima de 500 preco 0.65
# comercial até 1000 preco 0.55.....acima de 1000 preco 0.60
# industrial até 5000 preco 0.55....acima de 5000 preco 0.60

KWh = float (input('Digite a quantidade de KWh consumidos:'))
instalacao = input('Digite o tipo de instalacao, R,C,I:')

if instalacao == 'R':
    if KWh <= 500:
        preco = KWh * 0.40
        print(f'Valor a pagar de {preco}')
    else:
        preco = KWh * 0.65
        print(f'Valor a pagar de {preco}')
if instalacao == 'C':
    if KWh <= 1000:
        preco = KWh * 0.55
        print(f'Valor a pagar de {preco}')
    else:
        preco = KWh * 0.60
        print(f'Valor a pagar de {preco}')
if instalacao == 'I':
    if KWh <= 5000:
        preco = KWh * 0.55
        print(f'Valor a pagar de {preco}')
    else:
        preco = KWh * 0.60
        print(f'Valor a pagar de {preco}')