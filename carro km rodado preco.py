#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

KMs = int (input('Quantos KMs voce rodou?'))
D = int (input('Quantos dias voce ficou com o carro?'))
VP = ((60*D)+(KMs*0.15))
print(('O valor devido da sua locacao eh de {}').format(VP))



