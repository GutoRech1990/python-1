while True:
    nome = input('Qual o seu nome?')
    if (nome != 'GutoRech'):
        continue
    senha = input('Qual a senha?')
    if (senha == '12345'):
        break
print('Acesso concedido')
