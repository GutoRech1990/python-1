      # tela de boas vindas e de solicitacao do valor e da quantidade de produtos
print('Bem vindo a loja do José Augusto Rech')
vlr_prod = (float(input('Digite o valor de cada produto:')))
qtd_prd = (int(input('Digite a quantidade do produto:')))
# verificacao da quantidade para o calculo e impressao do valor sem e com o frete
if qtd_prd >=0 and qtd_prd <11:
  frete = 30 #variavel contendo o valor do frete
  print(f'O valor sem frete é de R${vlr_prod*qtd_prd:.2f}')
  print(f'O valor com frete é de R${(vlr_prod*qtd_prd)+frete:.2f}, (frete de R${frete:.2f})')
# verificacao da quantidade para o calculo e impressao do valor sem e com o frete
elif qtd_prd >=11 and qtd_prd <101:
  frete = 60 #variavel contendo o valor do frete
  print(f'O valor sem frete é de R${vlr_prod*qtd_prd:.2f}')
  print(f'O valor com frete é de R${(vlr_prod*qtd_prd)+frete:.2f}, (frete de R${frete:.2f})')
# verificacao da quantidade para o calculo e impressao do valor sem e com o frete
elif qtd_prd >=101 and qtd_prd <1001:
  frete = 120 #variavel contendo o valor do frete
  print(f'O valor sem frete é de R${vlr_prod*qtd_prd:.2f}')
  print(f'O valor com frete é de R${(vlr_prod*qtd_prd)+frete:.2f}, (frete de R${frete:.2f})')
else:
  # verificacao da quantidade para o calculo e impressao do valor sem e com o frete
  if qtd_prd >= 1001:
    frete = 240 #variavel contendo o valor do frete
    print(f'O valor sem frete é de R${vlr_prod*qtd_prd:.2f}')
    print(f'O valor com frete é de R${(vlr_prod*qtd_prd)+frete:.2f}, (frete de R${frete:.2f})')

