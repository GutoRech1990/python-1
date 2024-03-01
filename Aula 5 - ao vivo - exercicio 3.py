# Inicio da Funcao volume Feijoada
def volumeFeijoada ():
    print('----- Menu 1 de 3 - Volume Feijoada ------')
    while True:
        try:
            volumeF = int (input('Digite a quantidade desejada (ml): '))
            if (volumeF >= 300) and (volumeF <= 5000): # if 300 <= volumeF <= 5000:
             return volumeF * 0.08
            else:
                print('Atencao - quantida nao permitida')
                continue # retorna para o inicio
        except ValueError: # caso o usuario digite um valor nao numero ou nao inteiro
            print('Para de digitar valores nao inteiros')
# Fim da Funcao volume Feijoada

# Inicio da Funcao opcao Feijoada
def opcaoFeijoada ():
    print('----- Menu 2 de 3 - Opcao Feijoada ------')
    while True:
        opcaoF = input('Qual opcao de feijoada deseja \n +'
                       'b - Basica ( Feijao + paiol + costelinha) \n +'
                       'p - Premium ( Feijao + paiol + costelinha + partes de porco) \n +'
                       's - Suprema ( Feijao + paio; + costelinha + partes de porco + outros) \n +'
                       '>>')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Opcao invalida, escolha b,p ou s')
            continue # voltar para o inicio
# Fim da Funcao opcao Feijoada

# Inicio da Funcao acompanhamento Feijoada
def acompanhamentoFeijoada ():
    print('----- Menu 3 de 3 - Acompanhamneto Feijoada ------')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja mais algum adicional: \n +'
                                '0 - nao - encerrar pedido \n +'
                                '1 - 200g de arroz \n +'
                                '2 - 150g de couve cazida \n +'
                                '3 - 100g de couve cozida \n +'
                                '4 - 1 laranja descascada \n +'
                                '>>')
        if acompanhamentoF == '0':
            return acumulador
        elif acompanhamentoF == '1':
            acumulador += 5
            continue
        elif acompanhamentoF == '2':
            acumulador += 6
            continue
        elif acompanhamentoF == '3':
            acumulador += 7
            continue
        elif acompanhamentoF == '4':
            acumulador += 3
            continue
        else:
            print('Pare de digitar opcoes diferentes 0,1,2,3,4!')

# Fim da Funcao acompanhamento Feijoada

#Inicio do Main
print('----- Bem vindo ao Programa de Feijoada do José Augusto Rech------')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = (volume * opcao) + acompanhamento
print(f'Valor total R${total:.2f}, (Volume R$ {volume:.2f}, Tipo R$ {opcao:.2f}, Acompanhamento R${acompanhamento:.2f}')