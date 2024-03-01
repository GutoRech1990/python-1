#esreva um algoritimo que le um nome e uma idade
#caso onnome seja Vinicius, escreva na tela
#caso nao, verifique a idade...se maior que 18 anos, informe que é de menor
#se for maior de 100 anos informe que possivelmente nao existe


nome = input('Qual o seu nome?')
idade = int (input('Qual sua idade?'))

if nome == 'Vinicius':
    print(f'Ola {nome}')
elif idade < 18:
    print(f'Ola {nome}.Voce é menor de idade!')
elif idade >100:
    print(f'Ola {nome}.Voce provavelmente nao existe!')
