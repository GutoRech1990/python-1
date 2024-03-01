# Inicio da funcao metragem_limpeza
def metragem_limpeza ():
    print('>>>>>>>>>Menu 1 - Opcoes de metragens<<<<<<<<<<')
    while True:
        try:
            metragemL = int (input( 'Digite a metragem desejada (m2) entre 30 e 699:'))
            if (30<= metragemL < 300):
                print('E necessario contratar 1 pessoa')
                return 60 + (0.3 * metragemL)
            elif (300<= metragemL < 700):
                print('E necessario contratar 2 pessoas')
                return  120 + (0.5 * metragemL)
            else:
                print('Atencao - metragem digitada nao esta disponivel!')
                continue
        except ValueError:
            print('Voce deve digitar um valor numero inteiro entre')
# Fim da funcao metragem-limpeza

# Inicio da funcao tipo_limpeza
def tipo_limpeza():
    print('>>>>>>>>>>Menu 2  - Tipos de Limpezas <<<<<<<<<<<<')
    while True:
        tipoL = input('Digite o tipo de limpeza desejada \n'
                      'B - Basica - indicada para sujieras semanais ou quinzenais\n'
                      'C - Completa - Indicada para sujeiras antigas e/ou nao rotineiras\n'
                      '>>')
        tipoL = tipoL.upper()
        tipoL = tipoL.strip()
        if tipoL == 'B':
            print('Voce selecionou a limpeza basica')
            return 1.00
        elif tipoL == 'C':
            print('Voce selecionou a limpeza completa')
            return 1.30
        else:
            print('Opcao invalida, digite B ou C')
            continue # caso a opcao digitada seja invalida, voltar para o inicio
# Fim da funcao tipo_limpeza

# Inicia da funcao adicional_limpeza
def adicional_limpeza():
    print('>>>>>>>Menu 3 - Adicioanais <<<<<<<<<')
    acumulador = 0
    while True:
        adicionaisL = input('Digite o adicional desejado:\n'
                            '0 - Nao desejo mais nada (encerrar)\n'
                            '1 - Passar 10 pecas de roupas - R$ 10,00\n'
                            '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n'
                            '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'
                            '>>')
        if adicionaisL == '0':
            return acumulador
        elif adicionaisL == '1':
            acumulador += 10
            continue
        elif adicionaisL == '2':
            acumulador += 12
            continue
        elif adicionaisL =='3':
            acumulador += 20
            continue
        else:
            print('Opcao invalida, digite 0, 1, 2 ou 3!')
# Fim da funcao adicional_limpeza

# Inicio do Main
print('--------Bem vindo a empresa de limpezas do José Augusto Rech-----------')
metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicional = adicional_limpeza()
total = (metragem * tipo) + adicional
print(f'Valor total a ser pago de R${total:.2f}, (metragem R${metragem:.2f}, tipo R${tipo:.2f}, adicionais R${adicional:.2f})')