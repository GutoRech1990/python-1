def valida_string (pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len (s1)
    return s1
x = valida_string('Digite uma string:',10,30)
print(f'Voce digitou a string:{x}. \nDado valido, encerrando programa')
