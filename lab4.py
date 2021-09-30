## RESPOSTAS DA LISTA DE EXERCÍCIOS 4

## ADRIELLY DA SILVA BALBINO - DRE 118156484

# 1
def contatos(lista: list) -> dict:
    """Funcao recebe uma lista de dicionarios com as chaves em string e os valores em
    inteiros e retorna um unico dicionario com todos as chaves com seus valores adiconados
    em uma lista"""
    ## teste :
    ## contatos([{"Lucas":33358471, "Ugo":23568222, "Ana":34567117, "Nanda":43326989},{"Ana":65345643, "Douglas":23354893, "Renan":35768448, "Ingrid":42281003},{"Renan":78955987, "Olavo":24069878, "Sara":33561177, "Ugo":46589253}])

    contact_dict = dict()
    
    for dicio in lista:         #pegando cada dicionario na lista
        for key in dicio.keys():
            if key not in contact_dict: #conferindo se o novo dicionario já contem uma chave com mesmo nome
                contact_dict[key] = [dicio[key]]
            else:
                contact_dict[key].append(dicio[key])

    return contact_dict


# 2
def piano(notas: str) -> list:
    """Função recebe uma string com notas musicais e retorna uma lista coma a frequencia de cada uma delas"""

    # Definindo dicionario com as notas e sua respectivas frequencias
    dict_notas = dict([("C1", 65.5), ("C2", 131), ("C3", 262), ("C4", 524), ("C5", 1048),
                    ("D1", 73.5), ("D2", 147), ("D3", 294), ("D4", 588), ("D5", 1176), 
                    ("E1", 82.5), ("E2", 165), ("E3", 330), ("E4", 660), ("E5", 1320),
                    ("F1", 87.25), ("F2", 174.5), ("F3", 349), ("F4", 698), ("F5", 1396),
                    ("G1", 98), ("G2", 196), ("G3", 392), ("G4", 784), ("G5", 1568),
                    ("A1", 110), ("A2", 220), ("A3", 440), ("A4", 880), ("A5", 1760),
                    ("B1", 123.5), ("B2", 247), ("B3", 494), ("B4", 988), ("B5", 1976)])

    # Separando cada nota da string de entrada
    num_silabas = len(notas)//2 # assim saberemos o num de vezes que o looping irá rodar
    j = 1                       # valor inicial do looping

    i = 2                       #indice inicial do fatiamento da string
    lista_notas = [notas[:i]]   #lista com as notas com a primeira nota já inclusa

    while j < num_silabas: 
        list.append(lista_notas, notas[i:i+2])
        i += 2
        j += 1

    # Acessando as frequências no dicionario
    lista_freq = []
    for nota in lista_notas:
        list.append(lista_freq, dict_notas[nota])

    return lista_freq


# 3
def rezistor(cor_1: str, cor_2: str, cor_3: str) -> int:
    """Funcao recebe 3 parametros string cada um com uma cor, onde cada uma representa
    um valor de resistencia e retorna oa resistencia total """

    # Padronizando as strings de entrada
    cor_1 = cor_1.lower()
    cor_2 = cor_2.lower()
    cor_3 = cor_3.lower()
    
    # Criando dicionario com itens no formato (chave,valor)
    cores = dict([("preto",0), ("marrom",1), ("vermelho",2), ("laranja",3), ("amarelo",4)])

    # Concatenando os dois primeiros numeros
    S = str(cores[cor_1])+str(cores[cor_2])

    # Calculando a resistencia total
    R = int(S)*(10**cores[cor_3])

    return R
