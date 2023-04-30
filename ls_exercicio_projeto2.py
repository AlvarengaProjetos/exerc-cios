import os
import ls_exercicio_projeto2_modulo

contador_para_apresentacao = 0
dicionario_itens = {
    'chave': 'valor',
    'chave1': 'valor1',
    'chave2': 'valor2',
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
        if chave in dicionario_itens:
            print(
            'A CHAVE digitada já está no dicionário, se quiser atualizar \
            o VALOR dessa CHAVE use a opção "(3) Atualizar item".'
            )
        else:
            dicionario_itens[chave] = valor
            print(f'A CHAVE "{chave}" e o VALOR "{valor}" foram adicionados com sucesso.')
            print(dicionario_itens)
            input('Pressione qualquer tecla para continuar: ')

    # BOTÃO 2 - CONSULTA DICIONÁRIO
    elif input_usuario == '2':
        decisao = input('Você gostaria de realizar uma consulta via função? [S]IM ou [N]ÃO? ')
        
        if decisao == 'S' or 's':
                string_para_exercicio = 'chave1;chave2;chave4'
                ls_exercicio_projeto2_modulo.consulta(dicionario_itens, string_para_exercicio)
        
        elif decisao == 'N' or 'n':
            print('\nSão as CHAVES e VALORES cadastradas:')
            if dicionario_itens == {}:
                print('O banco de cadastro está vazio.')
            else:
                for chave, valor in dicionario_itens.items():
                    print(chave + ':' , valor)
        else:
            print('Você não digitou um comando válido.')
        
        input('\nPressione qualquer tecla para continuar: ')

    # 3
    elif input_usuario == '3':
        item_atualizado = input('Digite o novo item que gostaria de atualizar no cadastro: ')
        indice = input('Digite o índice do item que gostaria de atualizar, "0" acessa o primeiro item, "1" o segundo item e assim por diante: ')
        
        try: 
            dicionario_itens[int(indice)] = item_atualizado
        except ValueError:
            print('O input do usuário não é um índice válido.')
        input('Pressione qualquer tecla para continuar: ')

    # 4
    elif input_usuario == '4':
        indice = input('Digite o índice do item que gostaria de deletar, "0" acessa o primeiro item, "1" o segundo item e assim em diante: ')
        try: 
            dicionario_itens.pop(int(indice))
        except:
            print('O input do usuário não é um índice válido.')
        input('Pressione qualquer tecla para continuar: ')

    # 5
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
