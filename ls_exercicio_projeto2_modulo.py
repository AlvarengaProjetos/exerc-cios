def converte_string(string: str):
    """
    SUMÁRIO:
    Essa função converte uma string cujos valores estão separados pelo caractere ';'
    e retorna uma lista de tuplas com dois valores dentro de uma tupla.
    Ela precisa de um parâmetro em string no seguinte formato: 'chave1;valor1;chave2;valor2',
    e retorna uma lista de tuplas no formato: [(chave1, valor1), (chave2, valor2)]
    É uma função destinada à futura conversão para dicionários.

    VARIÁVEIS:
    temp -> uma variável do tipo string que existe apenas para salvar a string sem o ';'
    lista -> uma variável do tipo lista que armazena uma lista de tuplas da string que foi fornecida
            como parâmetro para a presente função.
    """
    temp = string.split(sep=';')
    lista = [
        (temp[i], temp[i+1]) 
        for i in range(0, len(temp), 2)
        ]
    return lista


def cadastra(dicionario: dict, lista: list):
    """
    SUMÁRIO:
    Essa função recebe como parâmetros um dicionário e uma lista de tuplas e adiciona as duas variáveis contidas
    na tupla de formato "[(chave, valor)]" adiciona ao dicionário no formato "{chave: valor}"

    """
    dict1 = {
        chave: valor
        for chave, valor in lista
        }
    dicionario.update(dict1)
    return dicionario           


def consulta(dicionario: dict, string: str):
    """
    SUMÁRIO:
    Essa função recebe um dicionário e uma string com várias chaves separadas por ';',
    e retornará o valor dessas chaves da string se a chave existir no dicionário.
    
    VARIÁVEIS:
    temp -> uma variável do tipo string que existe apenas para salvar a string sem o ';'
    
    dicionario_temp -> uma variável do tipo dict que cria um dicionário com as chaves fornecidas.
            o valor dessas chaves foi atribuído como '0' pois é irrelevante, a ideia é apenas 
            comparar chaves entre dicionários

    """
    
    temp = string.split(sep=';')
    lista_temporaria = [
        item 
        for item in temp
        ]

    for i in lista_temporaria:
        if i in dicionario:
            print(f'{i}: {dicionario[i]}')
        else:
            print(f'O VALOR {i} não está no banco de dados')
