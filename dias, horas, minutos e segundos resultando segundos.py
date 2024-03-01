d = int(input('Quantos dias?'))
h = int(input('Quantas horas?'))
m = int(input('Quantos minutos?'))
s = int(input('Quantos segundos?'))

res= ((d*24*60*60)+(h*60*60)+(m*60)+(s))
mostrar = 'O total de segundos eh {}'.format(res)
input(mostrar)

