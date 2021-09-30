## RESPOSTAS DA LISTA DE EXERCICIOS 6

## ADRIELLY DA SILVA BALBINO - DRE 118156484

# 1
def escreverNoArquivo(nomearquivo: str, lista: list) -> int:
    """Funcao recebe um arquivo e uma lista de objetos para escrever neste arquivo
    e retorna o numero total de caracteres escritos no arquivo"""

    f = open(nomearquivo, 'w')
    contador = 0

    for item in lista:
        contador += f.write(str(item)+'\n')

    f.close()
    return contador


# 2
# Obs.: os tipos de dado foram limitados apenas a strings e numeros
def retornarLista(str_lista: str) -> list:
    """Função recebe uma lista em formato string e deve retornar a mesma em formato list
    convertendo cada item na lista pelo tipo de dado mais apropriado"""

    listafinal = []

    # Tirando os colchetes e aspas da string-lista
    string = str.strip(str_lista, "[]")
    string = str.replace(string, "'", "")

    # Particionando a string usando a virgula como separador
    lista = str.split(string, ",")

    for item in lista:
        try:
            valor = float(item)
            list.append(listafinal, valor)
        except ValueError:
            list.append(listafinal, item)

    return listafinal


# 3
# Obs.: os tipos de dado foram limitados apenas a strings, numeros e listas
def lerArquivo(arquivo: str) -> type:
    """Função lê um arquivo que possui um conteudo por linha, converte a cada linha para
    o seu tipo exato e retona uma lista com todos os elementos"""

    f = open(arquivo, 'r')
    listafinal = []
    
    # Particionando a string usando a quebra de linha como separador
    lista = str.split(f.read(), "\n")


    for item in lista:
        try:
            valor = float(item)
            list.append(listafinal, valor)
        except ValueError:
            if item.find("[") != -1:
                listafinal.append(retornarLista(item))
            else:
                listafinal.append(item)
    f.close()                

    return listafinal





    
