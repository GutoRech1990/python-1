# escreva um algoritimo que crie uma tupla com 10 palavras.
# Encontre dentro dessa tupla as vogais de cada palavra

palavras = ('Mario' , 'Luigi' , 'Peach' , 'Yoshi' , 'Bowser')
for palavra in palavras:
    print(f'\nPalavra:{palavra.upper()}__Vogais:', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')