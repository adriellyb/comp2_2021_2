## RESPOSTA DOS EXERCÍCIOS LABORATÓRIO 7

## ADRIELLY DA SILVA BALBINO - DRE 118156484

import numpy as np

# 1
def senoPositivo(a:float, b:float, n:int): # -> numpy.ndarray 
    """Função tem como parametros de entrada o inicio do intervalo (a), o final do intervalo (b) e o numero de elementos (n).
    Ela deve criar um np.ndarray (x) de n pontos do intervalo [a,b] e retornar os elementos de x cujos seno é positivo"""

    # Criando o vetor x
    x = np.linspace(a,b,n) 

    # Calculando seno de cada elemento do array
    array_seno = np.sin(x)

    # Verificando os senos positivos
    condition = array_seno > 0

    # Retirando os valores de seno maior que 0
    array = np.extract(condition, x)

    return array

# 2
def polinomio(vetor: float, z:float) -> float:
    """Cria a função chamada polinomio cujo parâmetro de entrada é um np.ndarray unidimensional
    e um número real z. O valor de retorno é volor do polinômio p(x) no ponto z"""

    # Criando um vetor com os expoentes
    expoentes = np.arange(0,len(vetor))

    # Calculando o polinômio
    poli = np.sum(vetor*(z**expoentes))

    return poli

# 3
def ortogonal(matriz) -> bool:
    """Função que recebe uma np.ndarray bidimensional (uma matriz) e retorna o valor booleno True
    caso a matriz é ortogonal e False caso a matriz não é ortogonal."""

    # Verificando se a matriz é bidimensional
    if len(matriz.shape) <= 1:
        return False
    elif matriz.shape[0] <= 1:
        return False

    # Verificando se a matriz é quadrada
    if matriz.shape[0] != matriz.shape[1]:
        return False

    # Calculando a transposta de M
    transposta = np.transpose(matriz)

    return np.allclose(transposta@matriz, np.identity(matriz.shape[0]))
