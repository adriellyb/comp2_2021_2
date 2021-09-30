## RESPOSTAS DAS QUESTÕES DO LABORATÓRIO 8

## ADRIELLY DA SILVA BALBINO - DRE 118156484

import matplotlib.pyplot as plt
import numpy as np

# 1
def racional(n: int):
    """Função recebe o numero de termos (n) de um array de intervado [0.1,2] e
    retorna o grafico das funções y1 = 1/x e y2 = 1/(x**2) sendo x cada elemento do array"""

    # Valores do eixo x
    x = np.linspace(0.1, 2, n)

    # Calculando a primeira função (1/x)
    y1 = 1/x

    # Calculando a segunda função (1/(x**2))
    y2 = 1/(x**2)

    # Criando e plotando o gráfico
    fig, ax = plt.subplots(figsize =(6,6))  # tamanho 6x6
    
    ax.plot(x, y1, 'cs-', linewidth=2, label=r'$y=\frac{1}{x}$')
    ax.plot(x, y2, 'mo-', linewidth=2, label=r'$y=\frac{1}{x^2}$')

    ax.legend(loc='upper right')        # posição do rótulo

    ax.set_xticks([0,1,2])              # pontos do eixo x
    ax.set_title('Funções racionais')   # titulo de grafico

    plt.show()
    
    return None

# 2
def polinomios(n: int):
    """Função cujo parâmetro de entrada é um inteiro indicando o grau máximo dos polinômios a serem
    desenhados e retorna o gráfico de todas as funções y=x**i para i de 1 até o grau máximo passado"""

    # Valores do eixo x
    x = np.linspace(-1, 1, 100)

    # Array com os valores de 1 ate o grau maximo
    expoentes = np.arange(1, n+1, 1)

    # Criando o gráfico
    fig, ax = plt.subplots(figsize =(6,6))

    # Calculando a função y = x^i
    for i in expoentes:
        y = x**i

        # Plotando as funcões no grafico
        ax.plot(x, y, linewidth=2, label=r'$x**{}$'.format(i))

        ax.legend(loc='lower right')

        ax.set_xticks([-1,0,1])
        ax.set_yticks([-1,0,1])


    plt.show()    

    return None

# 3
def fun(a: float, b: float, n: int):
    """Cria uma função com três parâmetros de entrada: floats a, b e inteiro n.Com estes parâmetros, criara um
    np.ndarray x com n pontos do intervalo [a,b] e plotara a função 1/sin(x) descontínua"""

    # Valores do eixo x
    x = np.linspace(a, b, n)

    # Extraindo valores de x cujo seno é diferente de 0
    x = np.extract(np.sin(x) != 0 , x)

    # Extraindo valores de x cujo módulo de 1/sin(x) é menor que 20
    x = np.extract(np.abs(1/np.sin(x)) < 20, x)

    # Inserindo o np.nan na posicao que há descontinuidade
    pos = np.where(np.diff(np.sign(np.sin(x))) > 1)[0]+1
    
    pos = np.append(pos, np.where(np.diff(np.sign(np.sin(x))) < -1)[0]+1) # nesta etapa, eu adicionei ao array posição o outro ponto de descontinuidade para retonar na função
    
    x = np.insert(x, pos, np.nan)
    
    # Crando gráfico e plotando a função
    fig, ax = plt.subplots(figsize =(6,6))
    
    ax.plot(x, 1/np.sin(x), 'co-', label=r'$\frac{1}{sin(x)}$')

    ax.legend(loc='upper center')

    plt.show()

    return pos
