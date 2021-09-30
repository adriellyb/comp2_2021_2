## RESPOSTAS DA LISTA DE EXERCÍCIOS 3

## ADRIELLY DA SILVA BALBINO - DRE 118156484

class VeiculoAutomotor():
    
    def __init__(self, dono, placa, combustivel):
        """Cria um objeto da superclasse VeiculoAutomotor com atributos dono, placa, combustível"""
        # obj, str, str, str -> none
        self.dono = dono
        self.placa = placa
        self.combustivel = combustivel
    
    def __str__(self):
        """Função retorna string com os dados da classe VeiculoAutomotor"""
        # obj -> str
        return "Dono: {}, placa: {}, combustível: {}".format(self.dono, self.placa, self.combustivel)


# 1a
class Automovel(VeiculoAutomotor):
    
    def __init__(self, dono, placa, combustivel, lugares, portas, ano):
        """Função cria um objeto da subclasse Automovel com os atributos dono, placa, combustível
        lugares, portas e ano."""
        # obj, str, str, str, str, int, int -> none
        super().__init__(dono, placa, combustivel)
        self.lugares = lugares
        self.portas = portas
        self.ano = ano

# 1b
    def __str__(self):
        """Função retorna string com os dados da classe Automovel"""
        # obj -> str
        string = super().__str__()
        string += ", lugares: {}, portas: {}, ano: {}".format(self.lugares, self.portas, self.ano)

        return string

# 1c
    def trocarDono(self, novoDono):
        """Função recebe nome do novo dono e muda o atributo dono do objeto"""
        # obj, str -> none
        self.dono = novoDono


# 2a
class Caminhao(VeiculoAutomotor):
    
    def __init__(self, dono, placa, combustivel, cargaMax):
        """Função cria um objeto da subclasse Caminhao com os atributos dono, placa, combustível
        e a carga máxima suportada."""
        # obj, str, str, str, int -> none
        super().__init__(dono, placa, combustivel)
        self.cargaMax = cargaMax


# 2b
    def __str__(self):
        """Função retorna string com dados da classe Caminhao"""
        # obj -> str
        string = super().__str__()
        string += ", carga máxima: {} toneladas".format(self.cargaMax)

        return string
