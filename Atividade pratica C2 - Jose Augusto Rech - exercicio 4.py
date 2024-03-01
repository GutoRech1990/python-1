# -----------Inicio das Variaveis Globais ---------#
lista_funcionarios = []
ID_funcionario = 0
# -----------Fim das Variaveis Globais ------------#

# ---------Início de cadastrar_funcionario()-------#
def cadastrar_funcionario(ID):
    print('Bem vindo ao menu Cadastrar Funcionário')
    print(f'Codigo do funcionario {ID_funcionario}')
    nome = input('Digite o nome do funcionario:')
    setor = input('Digite o setor do funcionario:')
    salario = input('Digite o salário do funcionario:')
    dicionario_funcionario = {'ID'     : ID,
                              'nome'   : nome,
                              'setor'  : setor,
                              'salario': salario}
    lista_funcionarios.append(dicionario_funcionario.copy())
# ---------Fim de cadastrar_funcionario()----------#

# ---------Início de consultar_funcionario()-------#
def consultar_funcionario():
    print('Bem vindo ao menu Consultar Funcionário')
    while True:
        opcao_consultar = input('\nEscolha a opcao desejada:\n'
                                '1 - Consultar todos os funcionários\n'
                                '2 - Consultar funcionário por ID\n'
                                '3 - Consultar funcionário por Setor\n'
                                '4 - Retornar\n'
                                '>>')
        if opcao_consultar == '1':
            print('Voce escolheu a opcao >Consultar todos os funcionários<')
            for funcionario in lista_funcionarios: #funcionario vai varrer toda a lista de funcionarios
                print('----------------------------------')
                for key, value in funcionario.items(): #varrer todos os conjuntos key e value do dicionario funcionario
                    print(f'{key}: {value}')
                print('----------------------------------')
        elif opcao_consultar == '2':
            print('voce escolheu a opcao >Consultar funcionario por ID<')
            funcionario_desejado = int (input('Digite o ID desejado:'))
            for funcionario in lista_funcionarios:
                if funcionario['ID'] == funcionario_desejado: # o valor do campo ID desse dicionario é igual o valor desejado?
                    print('----------------------------------')
                    for key, value in funcionario.items():
                        print(f'{key}: {value}')
                    print('----------------------------------')
        elif opcao_consultar == '3':
            print('Voce escolheu a opcao >Consultar funcioário por Setor<')
            setor_desejado = input('Digite o Setor desejado:')
            for funcionario in lista_funcionarios:
                if funcionario ['setor'] == setor_desejado: # o valor do campo é igual o valor desejado?
                    print('----------------------------------')
                    for key, value in funcionario.items(): # varrer todos os conjuntos key e value do dicionario funcionario
                        print (f'{key}: {value}')
                    print('----------------------------------')
        elif opcao_consultar == '4':
            return # sai da opcao consultar produtos e volta para o Main
        else:
            print('Opcao invalida, tente novamente')
            continue # voltar para o inicio do laco
# ---------Fim de consultar_funcionario()---------#

# ---------Início de remover_funcionario()-------#
def remover_funcionario():
    print('Bem vindo ao menu Remover Funcionario')
    valor_desejado = int (input('Digite o ID do funcionario que deseja remover:'))
    for funcionario in lista_funcionarios:
        if funcionario ['ID'] == valor_desejado:
            lista_funcionarios.remove(funcionario)
            print('Funcionario removido com sucesso!!!')
# ------------Fim de remover_funcionario()-------#

# ---------------Início de Main------------------#
print('Bem vindo ao Software de Controle de Funcionários do José Augusto Rech')
while True:
    opcao_principal = input('\nEscolha a opcao desejada:\n'
                             '1 - Cadastrar Funcionário\n'
                             '2 - Consultar Funcionário(s)\n'
                             '3 - Remover funcionário\n'
                             '4 - Sair\n'
                             '>>')
    if opcao_principal == '1':
        ID_funcionario += 1
        cadastrar_funcionario(ID_funcionario)
    elif opcao_principal == '2':
        consultar_funcionario()
    elif opcao_principal == '3':
        remover_funcionario()
    elif opcao_principal == '4':
        break # encerra o laco
    else:
        print('Opcao invalida, tente novamente')
        continue #volta para o inicio do laco
# ------------------Fim de Main------------------#






