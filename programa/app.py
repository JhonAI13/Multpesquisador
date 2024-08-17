import webbrowser
iwebsites = {"google":'https://www.google.com/search?q=', 
            "wikipedia":'https://pt.wikipedia.org/wiki/'}



def interface():
    lista = []
    resposta = str(input('Quer mudar os sites')).strip()
    if resposta in ("si", "sim", "s"):
        with open(r'programa\sites.txt', 'r') as arquivo:
            n = 0
            for linha in arquivo:
                if n != 0: #Verifica se é a primeira linha
                    if n % 2 == 0: #Anda nas linhas pares - a 1 linha
                        print(linha)
                        lista.append(str(linha))
                n += 1
    else:
        with open(r'programa\sites.txt', 'r') as arquivo:
            n = 0
            for linha in arquivo:
                if n != 0: 
                    if n % 2 != 0: 
                        print(f'[linha]', end='')
                n += 1
        # perguntar quais os sites o usuario quer
            # google, wiki, google escola, translate
            # (1,2 , 3)
            # salvar na lista quais sites foram escolhidos
            # vai colocar os sites na lista em str
         
    return lista


def pesquise(websites, pesquisa): # mudar para funcionar com lsita
    """abre abas pesquisando, a quantidade de sites da lista.

    Args:
        websites (lista): _description_
        pesquisa (string): _description_
    """
    for url in websites: 
        webbrowser.open(websites[url] + pesquisa)


def pergunte():
    escolhidos = interface()
    return escolhidos, str(input("Mulltipesquisador \n"))
    
pesquise(iwebsites, pergunte())
