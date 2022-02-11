## RESPOSTAS DOS EXERCÍCIOS DO LABORATÓRIO 10

## ADRIELLY DA SILVA BALBINO - DRE 118156484

import pandas as pd
import matplotlib.pyplot as plt

# 1
def suites():
    """Função não recebe parâmetro e retorna a frequência de cada valor da coluna 'suíte'
    além de seu gráfico em pizza destas frequencias"""

    # Importando a planilha "dados.csv"
    df = pd.read_csv("dados.csv")

    # Calculando a frequencia de cada valor de "suíte"
    freq = df["suites"].value_counts()

    # Criando e plotando o gráfico da frequencia
    fig, axes = plt.subplots()

    axes.axis('equal')   # 1:1 - circular
    freq.plot.pie(ax = axes, autopct = '%1.1f%%')    # Pizza

    plt.show()

    return freq

# 2
def area():
    """Função não recebe parâmetro e retorna o histograma de áreas dos apartamentos, concretamente, e a
    distribuição de frequências de 20 classes uniformes das áreas"""

    # Importando a planilha "dados.csv"
    df = pd.read_csv("dados.csv")

    # Coletando os valores das areas dos apts 
    areas = df["area"]

    # Criando e plotando o gráfico das frequencias
    fig, axes = plt.subplots()

    areas.plot.hist(ax = axes, bins = 20, color='g')  #Histograma

    plt.show()

    return df[df["area"] == df["area"].max()] 

# 3
def procura(preco: int, area: int, condominio: int):
    """Função recebe 3 números que correspondem, respectivamente, ao preco, a area e ao condominio. O valor de retorno
    será um subconjunto de dados de apartamentos que respeitem as seguntes regras:

    1ª) preço do apt deve ser < ou = ao preço passado
    2ª) area do apt deve ser > ou = a area passada
    3ª) condominio do apt deve ser < ou = ao condominio passado

    Além disso, a função também retorna um gráfico de barras com as frequencias dos valores da coluna 'bairro' do subconjunto"""

    # Importando a planilha "dados.csv"
    df = pd.read_csv("dados.csv")

    # Extraindo dados que respeitem a primeira regra
    df = df[df["preco"] <= preco]

    # Extraindo dados que respeitem a segunda regra
    df = df[df["area"] >= area]

    # Extraindo dados que respeitem a terceira regra
    df = df[df["condominio"] <= condominio]

    # Calculando a frequencia dos valores de 'bairro' do subconjunto
    freq = df["bairro"].value_counts()

    # Criando e plotando o gráfico das frequencias
    fig, axes = plt.subplots()

    freq.plot.bar(ax = axes, rot = 0, color='tab:orange')       #Barras

    plt.show()

    return freq
