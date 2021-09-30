## LISTA DE EXERCICIOS 1
import math

#1
def concatena(string1, string2, m, n):
    """Função retorna a concatenação da primeira string sem os m primeiros caracteres, com a segunda sem
os últimos n caracteres."""

    return string1[m:]+string2[:-n]


#2
def sublista(lista, m, n):
    """ A função retorna uma sublista formada por todos os números da
lista que são maiores que m e menores que n."""
    
    sublist = []

    for i in lista:
        if i>m and i<n:
            list.append(sublist, i)

    return sublist

#3
def fun(palavra, lista_str):
    """ A função junta a string palavra com as strings da lista em uma frase, separando as strings
com espaço."""

    return palavra+" "+str.join(" ", lista_str)


#4a
def numeroEuler(n):
    """ Função calcula o valor de e por meio da séria acima até o n–ésimo termo do
somatório, onde o número n é passado como um parâmetro. """

    i = 0
    soma = 0
    while i<=n:
        soma = soma + (1/math.factorial(i))
        i = i+1

    return soma


#4b
def precisaoEuler(erro):
    """ a função descubre quantos termos da série devem ser calculados para
que o erro absoluto entre math.e e o valor de e da série seja inferior a um erro passado como
parâmetro."""

    i = 0
    e_calc = numeroEuler(i)
    
    while math.e - e_calc > math.fabs(erro):
        i = i+1
        e_calc = numeroEuler(i)

    return i


#4c
def main():
    """" A função possui a mesma funcionalidade da função precisaoEuler acima,
mas pede ao usuário informar a precisão desejada"""

    erro=float(input("Informe a precisão desejada: "))

    print(precisaoEuler(erro))

    return 0

if __name__=="__main__":
    main()



