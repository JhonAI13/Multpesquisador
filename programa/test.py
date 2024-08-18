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