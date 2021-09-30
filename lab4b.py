## RESPOSTAS DO LABORATÓRIO EXTRA

## ADRIELLY BALBINO - DRE 118156484

# 1
class Dinheiro:

    def __init__(self, valor: float, moeda: str):
        conversor = dict([('BRL', 1), ('USD', 4.012), ('EUR', 4.451), ('JPY', 0.035)])

        if moeda in conversor:
            self.valor = valor*conversor[moeda]      #valor em reais
        else:
            print("Não é possivel converter para reais.")

    def valor_em(self, moeda: str) -> float:
        conversor = dict([('BRL', 1), ('USD', 4.012), ('EUR', 4.451), ('JPY', 0.035)])

        return self.valor/conversor[moeda]

    def __str__(self):

        return "{} BLR".format(str(self.valor))
        

# 2
def BrexitEmployment(cpf_yes: set, cpf_no: set, cpf_empregados: set, cpf_desempregados: set) -> str:

    """"Função retorna o percentual de pessoas empregadas e desempregadas dentro do conjunto
    dos que votaram sim ou não no Brexit"""

    # Total de votantes do Brexit
    votantes = len(cpf_yes.union(cpf_no))

    # Total de pessoas empregadas que votaram sim
    emp_sim = len(cpf_yes.intersection(cpf_empregados))

    # Total de pessoas empregadas que votaram não
    emp_nao = len(cpf_no.intersection(cpf_empregados))

    # Total de pessoas desempregadas que votaram sim
    desemp_sim = len(cpf_yes.intersection(cpf_desempregados))

    # Total de pessoas desempregadas que votaram não
    desemp_nao = len(cpf_no.intersection(cpf_desempregados))

    return "YES: {:.2f}% trabalham, {:.2f}% estão desempregados \nNO: {:.2f}% trabalham, {:.2f}% estão desempregados".format((emp_sim/votantes)*100,
                                                                                                             (desemp_sim/votantes)*100,
                                                                                                             (emp_nao/votantes)*100,
                                                                                                             (desemp_nao/votantes)*100)

