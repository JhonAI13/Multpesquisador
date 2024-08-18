import webbrowser
txt = 'programa\\sites.txt'

def reescrever_primeira_linha(caminho_arquivo, nova_linha):
    # Lê o conteúdo do arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Substitui a primeira linha
    if linhas:
        linhas[0] = nova_linha + '\n'
    else:
        # Se o arquivo estiver vazio, adiciona a nova linha
        linhas.append(nova_linha + '\n')

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

def ler_e_converter_primeira_linha(caminho_arquivo):
    """
    Lê a primeira linha de um arquivo, divide a linha em substrings usando vírgulas como delimitadores,
    e converte essas substrings em uma lista de inteiros.

    :param caminho_arquivo: Caminho para o arquivo de texto.
    :return: Lista de inteiros obtidos da primeira linha do arquivo.
    """
    with open(caminho_arquivo, 'r') as arquivo:
        # Lê a primeira linha e remove espaços em branco
        primeira_linha = arquivo.readline().strip()
    
    # Divide a linha em substrings e converte em inteiros
    substrings = primeira_linha.split(',')
    
    return [int(substring) for substring in substrings]

def txt_para_lista(caminho_arquivo, lista):
    ordem = ler_e_converter_primeira_linha(caminho_arquivo)
    with open(caminho_arquivo, 'r') as arquivo:
        n = 0
        c = 0
        for linha in arquivo:
            if n != 0: #Verifica se é a primeira linha
                if n % 2 == 0: #Anda nas linhas pares - a 1 linha
                    c += 1
                    if c in ordem:
                        print(linha)
                        lista.append(str(linha))
            n += 1
    return lista

def interface(caminho_arquivo):
    lista = []
    resposta = str(input('Quer mudar os sites')).strip()
    if resposta in ("si", "sim", "s"):
        lista = txt_para_lista(caminho_arquivo, lista)
    else:
        with open(caminho_arquivo, 'r') as arquivo:
            n = 0
            l = 1
            for linha in arquivo:
                if n != 0: 
                    if n % 2 != 0: 
                        print(f'{l} {linha}', end='')
                        l += 1
                n += 1
        
        resposta = str(input('Quais sites quer?')).strip()
        reescrever_primeira_linha(caminho_arquivo, resposta)
        lista = txt_para_lista(caminho_arquivo, lista)
         
    return lista

def pesquise(): # mudar para funcionar com lsita
    """abre abas pesquisando, a quantidade de sites da lista.

    Args:
        websites (lista): _description_
        pesquisa (string): _description_
    """

    escolhidos = interface(txt)
    pesquisa = str(input("Multipesquisador \n"))
    for url in escolhidos: 
        webbrowser.open(url + pesquisa)

pesquise()
