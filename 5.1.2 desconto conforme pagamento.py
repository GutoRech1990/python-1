#Uma loja de departamentos está oferecendo diferentes formas de pagamento,
# conforme opções listadas a seguir. Faça um algoritmo que leia o valor total de uma compra e
# calcule o valor do pagamento final de acordo com a opção escolhida.
#Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela.
# Ao final, apresente o valor total da compra e o valor das parcelas:
#• Pagamento à vista – conceder desconto de 5%;
# • Pagamento em 3x – o valor não sofre alterações;
# • Pagamento em 5x – acréscimo de 2%;
#• Pagamento em 10x – acréscimo 8%.

print('Bem vindo a tela de pagamento, abaixo as opções disponiveis')
print('1 - A vista, com desconto de 5%')
print('2 - Em 3x, sem alteracoes')
print('3 - Em 5x, com acrescimo de 2%')
print('4 - Em 10x, com acrescimo de 8%')
op = int(input('Qual a opcao desejada?:'))
valor = float(input('Qual o valor da sua compra?'))
if op == 1:
    res = valor - (valor * 0.05)
    print(f'Valor original:R${valor}, seu valor com pagamento a vista:R${res}')
elif op == 2:
    parc = valor / 3
    print(f'O valor total da sua compra é de R${valor} , e sera parcelado em 3 parcelas iguais de R${parc}')
elif op == 3:
    valor_acresc_2 = valor + (valor * 0.02)
    parc = valor_acresc_2 / 5
    print(f'O valor total da sua compra é de R${valor_acresc_2} , e sera parcelado em 5 parcelas iguais de R${parc}')
elif op == 4:
    valor_acresc_8 = valor + (valor * 0.08)
    parc = valor_acresc_8 / 10
    print(f'O valor total da sua compra é de R${valor_acresc_8}, e sera parcelado em 10 parcelas iguais de R${parc}')






