# imagine que voce esta desenvolvendo um software de controle de estoque para uma mercearia.
# este software deve ter o seguinte meni e opcoes:
# 1. Cadastrar
# 2. Consultar Produto(s)
#     1) Consultar todos os produtos
#     2) Consultar produto por codigo
#     3) Consultar produto(s) por fabricante
#     4) Retornar
# 3. Remover Produto
# 4. Sair


# -----------Inicio das Variaveis Globais ---------#
lista_produto = []
codigo_produto = 0

# -----------Fim das Variaveis Globais ---------#



#-------------Inicio de cadastrar_produtos()---------#
def cadastrar_produto(codigo):
    print('Bem vindo ao menu de Cadastrar Produto')
    print(f'Codifo do Produto {codigo_produto}')
    nome = input('Digite o nome do produto:')
    fabricante = input('Digite o fabricante do produto:')
    preco = input('Digite o preco do produto:')
    dicionario_produto = {'codigo'    : codigo,
                          'nome'      : nome,
                          'fabricante': fabricante,
                          'preco'     : preco}
    lista_produto.append(dicionario_produto.copy())
#-------------Fim de cadastrar_produtos()---------#



#-------------Inicio de consultar_produtos()---------#
def consultar_produto():
    print('Bem vindo ao menu de Consultar Produto')
    while True:
        opcao_consultar = input('\nEscolha a opcao desejada:\n'
                                '1 - Consultar todos os Produto\n'
                                '2 - Consultar Produto por codigo(s)\n'
                                '3 - Consultar Produto por fabricante\n'
                                '4 - Retornar\n'
                                '>>')
        if opcao_consultar == '1':
            print('Voce escolheu a opcao Consultar todos os produtos')
            for produto in lista_produto: #produto vai varrer toda a lista de produtos
                print('------------------------------')
                for key, value in produto.items(): # varrer todos os conjuntos key e value do dicionario produto
                    print(f'{key}: {value}')
                print('------------------------------')
        elif opcao_consultar == '2':
            print('Voce escolheu a opcao Consultar produtos por codigo')
            valor_desejado = int(input('Digite o Codigo desejado:'))
            for produto in lista_produto:
                if produto['codigo'] == valor_desejado: # o valor do campo codigo desse dicionario é igual o valor desejado?
                    print('------------------------------')
                    for key, value in produto.items():  # varrer todos os conjuntos key e value do dicionario produto
                        print(f'{key}: {value}')
                    print('------------------------------')
        elif opcao_consultar == '3':
            print('Voce escolheu a opcao Consultar produtos por fabricante')
            valor_desejado = input('Digite o Fabricante desejado:')
            for produto in lista_produto:
                if produto['fabricante'] == valor_desejado:  # o valor do campo codigo desse dicionario é igual o valor desejado?
                    print('------------------------------')
                    for key, value in produto.items():  # varrer todos os conjuntos key e value do dicionario produto
                        print(f'{key}: {value}')
                    print('------------------------------')
        elif opcao_consultar == '4':
            return # sai da funcao consultar_produtoe volta para o Main
        else:
            print('Opcao invalida, tente novamente')
            continue  # voltar para o inicio do laco

#-------------Fim de consultar_produtos()---------#



#-------------Inicio de remover_produtos()---------#
def remover_produto():
    print('Bem vindo ao menu de Remover Produto')
    valor_desejado = int(input('Digite o codigo do produto que deseja remover:'))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado:
            lista_produto.remove(produto)
            print('Produto removido com sucesso!!!')


#-------------Fim de remover_produtos()---------#



#-------------Inicio de Main---------#
print('Bem vindo a Mercearia do José Augusto Rech')
while True:
    opcao_principal = input('\nEscolha a opcao desejada:\n'
                            '1 - Cadastrar Produto\n'
                            '2 - Consultar Produto(s)\n'
                            '3 - Remover Produto\n'
                            '4 - Sair\n'
                            '>>')
    if opcao_principal == '1':
        codigo_produto = codigo_produto + 1
        cadastrar_produto(codigo_produto)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        break # encerra o laco principal
    else:
        print('Opcao invalida, tente novamente')
        continue #voltar para o inicio do laco

#-------------Fim de Main---------#