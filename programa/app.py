import webbrowser
iwebsites = ['https://www.google.com/search?q=', 
            'https://pt.wikipedia.org/wiki/']

def pesquise(websites,pesquisa):
    """abre abas pesquisando, a quantidade de sites da lista.

    Args:
        websites (lista): _description_
        pesquisa (string): _description_
    """
    for url in websites:
        webbrowser.open(url + pesquisa)

pesquisa = str(input("Mulltipesquisador \n"))
pesquise(iwebsites, pesquisa)