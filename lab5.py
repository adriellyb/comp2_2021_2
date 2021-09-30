## RESPOSTAS DOS EXERCÍCIOS DO LAB 5

## ADRIELLY DA SILVA BALBINO - DRE 118156484

# 1
import math

def absoluto(valor) -> float:
    """Funcao tem como entrada permitida um numero ou uma string de numero e retorna o valor
    absoluto, caso haja um entrada nao permitida, retorna uma mensagem de erro"""

    try:
        v = float(valor)
        return abs(v)
    except TypeError:
        print("TypeError para {}".format(type(valor)))
        return None
    except ValueError:
        print("ValueError para '{}'".format(valor))
        return None


# 2a
class Loja:

    def __init__(self, nome: str, produtos: dict = {}):
        """Funcao cria a classe Loja que possui como atributos o nome e um dicionário de produtos no qual
        as chaves são as categorias dos produtos e os valores são conjuntos das marcas daquela categoria"""
        self.nome = nome
        self.produtos = produtos

# 2b
    def adicionarProduto(self, categoria: str, marca: str):
        """Funcao adiciona uma marca a uma determinada categoria presente no dicionario. Caso esta
        categoria não exista, uma nova é criada através dos tratamentos de exceções"""

        try:
            self.produtos[categoria].add(marca)
        except KeyError:
            self.produtos[categoria] = {marca}
            return None

# 2c
    def verCategoria(self, categoria: str):
        """Funcao verifica quais marcas estão associadas a categoria desejada, caso não exista
        esta categoria, uma mensagem de erro é enviada"""

        try:
            return self.produtos[categoria]
        except KeyError:
            print("Categoria {} não catalogada.".format(categoria))
            return None

# 2d
    def removerMarca(self, marca: str):
        """Funcao remove a marca inserida como entrada de todos os conjuntos de todas as categorias que estiver presente"""

        for categoria in self.produtos.keys():
            try:
                self.produtos[categoria].remove(marca)
            except KeyError:
                pass

