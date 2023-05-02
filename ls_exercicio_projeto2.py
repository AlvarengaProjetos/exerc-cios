import os
import ls_exercicio_projeto2_modulo

contador_para_apresentacao = 0
dicionario_itens = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
    }

# LIMPAR O CONSOLE
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # APRESENTAÇÃO NO PRIMEIRO ACESSO
    if contador_para_apresentacao == 0:
        print(
            '======================================================================\n',
            'PROGRAMA DE CADASTRO DE MATERIAL\n',
            '======================================================================\n',
            'Bem-vindo ao programa de cadastro de material!'
        )
        contador_para_apresentacao += 1

    # O IMPUT DO USUÁRIO COM O MENU DE OPÇÕES
    input_usuario = input(
        'Escolha uma das opções abaixo:\n'
        '(1) Cadastrar item;\n'
        '(2) Consultar item;\n'
        '(3) Atualizar item;\n'
        '(4) Excluir item;\n'
        '(5) Exibir cadastro;\n'
        'Ou digite "quite" para sair: '
        )

    # DIVISÃO LÓGICA DO INPUT DO USÁRIO
    
    # BOTÃO 1 - ADICIONA CHAVE E VALOR
    if input_usuario == '1':
        chave = input('Digite a CHAVE a ser cadastrada: ')
        valor = input('Digite o VALOR da chave a ser cadastrado: ')
        lista_de_tupla_chave_valor = [(chave, valor)]

        if chave in dicionario_itens:
            print(
                'A CHAVE digitada já está no dicionário, se quiser '
                'atualizar o VALOR dessa CHAVE use a opção (3) Atualizar item. '
                'Pressione qualquer tecla para continuar.'
                )
            input('Pressione qualquer tecla para continuar: ')
        else:
            ls_exercicio_projeto2_modulo.cadastra(dicionario_itens, lista_de_tupla_chave_valor)
            for chave, valor in dicionario_itens.items():
                    print(chave + ':' , valor)
            input('Pressione qualquer tecla para continuar: ')
        

    # BOTÃO 2 - CONSULTA DICIONÁRIO
    elif input_usuario == '2':
        decisao = input('Você gostaria de realizar uma consulta via função? [S]IM ou [N]ÃO? ')
        
        if decisao == 'S' or 's':
            string_para_exercicio = 'chave1;chave2;chave4'
            
            if dicionario_itens == {}:
                print('O banco de dados está vazio.') 
            else:
                ls_exercicio_projeto2_modulo.consulta(dicionario_itens, string_para_exercicio)   
                
        
        elif decisao == 'N' or 'n':
            print('\nSão as CHAVES e VALORES cadastradas:')
            if dicionario_itens == {}:
                print('O banco de dados está vazio.')
            else:
                for chave, valor in dicionario_itens.items():
                    print(chave + ':' , valor)
        else:
            print('Você não digitou um comando válido.')
        
        input('\nPressione qualquer tecla para continuar: ')

    # BOTÃO 3 - ATUALIZAR ITEM
    elif input_usuario == '3':
        chave = input('Digite o nova CHAVE a ser atualizada no banco de dados: ')
        valor = input('Digite o novo VALOR da nova CHAVE: ')
        
        if chave in dicionario_itens:
            dicionario_itens[chave] = valor
        else:
            print('Use a função de CADASTRAR ITEM para introduzir novos itens ao banco de dados.')

    # BOTÃO 4 - EXCLUIR ITEM 
    elif input_usuario == '4':
        chave = input('Digite a CHAVE a ser deletada no banco de dados: ')
                
        if chave in dicionario_itens:
            dicionario_itens.pop(chave)
            for chave, valor in dicionario_itens.items():
                    print(chave + ':' , valor)
            
            input('\nPressione qualquer tecla para continuar: ')
        else:
            print('Não existe essa CHAVE no banco de dados.')
            input('\nPressione qualquer tecla para continuar: ')

    # BOTÃO 5 - EXIBIR CADASTRO
    elif input_usuario == '5':
        if dicionario_itens != {}:
            for chave, valor in dicionario_itens.items():
                print(f'{chave}: {valor}')
        else:
            print('Cadastro vazio.')
        input('Pressione qualquer tecla para continuar: ')

    # FINALIZAR O PROGRAMA
    elif input_usuario == 'quite':
        print('Finalizando Aplicação.')
        break
    else:
        input('Digite um comando válido. Pressione qualquer tecla para continuar.')

    # LIMPAR O CONSOLE
    os.system('CLS')
