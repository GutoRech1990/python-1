#desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual.
# Calcule a sua idade e apresente na tela.
#Para fins de simplificação, despreze o dia e o mês do ano.
# Após o cálculo, verifique se a idade é maior ou igual a 18 anos e
# apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.

ano_nasc = int (input('Em que ano voce nasceu?'))
ano_atual = int (input('Em que ano estamos?'))
nome = input('Qual o seu nome?')
idade = ano_atual - ano_nasc
print(f'A sua idade é {idade}')
if idade < 18:
    print(f'Voce ainda nao pode dirigir {nome} :(')
elif idade >= 18:
    print(f'Parabens {nome}, voce ja pode dirigir :)')

