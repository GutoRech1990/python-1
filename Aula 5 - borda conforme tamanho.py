def borda (s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('Analise e desenvolvimento de softwares')
borda('Jose Augusto Rech')
borda('BR,LU')
