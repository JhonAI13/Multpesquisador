def interface():
    lista = []
    resposta = "n"
    # resposta = str(input('Quer mudar os sites')).strip()
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
            l = 1
            for linha in arquivo:
                if n != 0: 
                    if n % 2 != 0: 
                        print(f'{l} {linha}', end='')
                        l += 1
                n += 1
        
        resposta = str(input('Quais sites quer?')).strip()
        resposta = resposta.replace(' ', '')
        resposta_lista_str = resposta.split(",")
        with open(r'programa\sites.txt', 'w') as arquivo:
            arquivo.write(linha)
        for numero in resposta_lista_str:
            lista.append(int(numero))
            # salvar na lista quais sites foram escolhidos
            # vai colocar os sites na lista em str
         
    return lista
print(interface())

# def escolhidos(iwebsites):
#     lista = ()
#     lista_escolhidos = ()
#     for nome in iwebsites:
#         print(nome)
#     perguntar()
#     return lista_escolhidos 

# def escolhas(iwebsites):
#     lista = ()
#     escolhidos = escolhidos(iwebsites)
#     for nome in iwebsites:
#         if nome in escolhidos:
#             lista.append(nome)
#     return lista
