import webbrowser, time, sys

txt = 'C:\\Users\\jonat\\Documents\\GitHub\\Multpesquisador\\programa\\sites.txt'

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
                        # print(linha)
                        lista.append(str(linha))
            n += 1
    return lista

def interface(caminho_arquivo):
    lista = []
    resposta = str(input('Quer mudar os sites: ')).strip()
    if resposta in ("si", "sim", "s"):
        with open(caminho_arquivo, 'r') as arquivo:
            n = 0
            l = 1
            for linha in arquivo:
                if n != 0: 
                    if n % 2 != 0: 
                        print(f'{l} {linha}', end='')
                        l += 1
                n += 1
        
        resposta = str(input('Quais sites quer? \n')).strip()
        reescrever_primeira_linha(caminho_arquivo, resposta)
        lista = txt_para_lista(caminho_arquivo, lista)
    else:
        lista = txt_para_lista(caminho_arquivo, lista)
         
    return lista

def barra_de_carregamento(tempo_total, largura=10):
    for i in range(tempo_total + 1):
        porcentagem = (i / tempo_total) * 100
        barra = ('#' * int(largura * i // tempo_total)).ljust(largura)
        sys.stdout.write(f'\r[{barra}] {porcentagem:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # Simula o tempo de carregamento

def pesquise(): 
    """abre abas pesquisando, a quantidade de sites da lista.

    Args:
        websites (lista): _description_
        pesquisa (string): _description_
    """

    escolhidos = interface(txt)
    barra_de_carregamento(3)
    pesquisa = str(input("\nMultipesquisador \n"))
    if pesquisa != '':
        for url in escolhidos: 
            webbrowser.open(url + pesquisa)

def rodar():
    primeira_iteracao = True

    while True:
        if not primeira_iteracao:
            resposta = input("Deseja continuar? : ").strip().lower()
            if resposta not in ("si", "sim", "s"):
                print("Encerrando o Multipesquisador.")
                break
        else:
            primeira_iteracao = False
        pesquise()

rodar()