# RESPOSTAS DA LISTA DE EXERCÍCIOS 2

class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def alterarMatricula(self, matricula):
        """Altera a matricula"""
        if self.matricula == matricula:
            print("A matrícula já está " + matricula)
        else:
            self.matricula = matricula
            print("A matrícula foi alterada para " + matricula)
            
    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

        
#=======================================

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")

# 1a
    def consultarVagas(self):
        """Função consulta o número de vagas totais e vagas livres que possuem 
        numa determinada disciplina"""
        
        vagas_preenchidas = len(self.alunos)    #numero de alunos na disciplina
        vagas_livres = self.vagas - vagas_preenchidas
        
        return "Vagas totais: {}. Vagas livres: {}".format(self.vagas, vagas_livres)


# 1b
    def __str__(self):
        """Função imprime informações da disciplina como o nome, num de vagas
        totais e livres e infos do alunos inscritos (nome, DRE, matrícula)"""

        string = "" #string vazia que sera preenchida com os dados dos alunos
        
        if len(self.alunos) == 0:
            return "{}, sem alunos inscritos.\n{}".format(self.nome, Disciplina.consultarVagas(self))
        elif len(self.alunos) > 0:
            for i in range(len(self.alunos)): #pelo for pegamos os dados de cada aluno inscrito e...
                str_aluno = "\n{}".format(self.alunos[i])
                string  = string+str_aluno              # ...adicionamos a string vazia
            return "{}, alunos inscritos:{}\n{}".format(self.nome, string, Disciplina.consultarVagas(self))
        

#=======================================
from datetime import date
import time


# 2a
class Pessoa:
    def __init__(self, nome, dataNascimento, nomeDeMae, nomeDePai):
        """Cria um objeto de classe Pessoa com atributos nome, data de nascimento,
        nome da mãe e nome do pai"""
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.nomeDeMae = nomeDeMae
        self.nomeDePai = nomeDePai

# 2b
    def idade(self, data = date.today().strftime("%d/%m/%Y")):
        """Função calcula a idade da pessoa dado como parâmetro uma data em formato
        string tendo como valor default a data atual"""

        # transformando a string em valor de tempo
        struct_dataNascimento = time.strptime(self.dataNascimento, "%d/%m/%Y") #data de nascimento
        struct_data = time.strptime(data, "%d/%m/%Y")                       # data passada como parametro

        #calculando a idade
        diferencaAno = struct_data.tm_year - struct_dataNascimento.tm_year

        if (struct_data.tm_year < struct_dataNascimento.tm_year):
            return "Não é possível calcular com uma data anterior ao nascimento"

        # codicionais caso o mes passado como parametro for menor ou igual a o mes de nascimento 
        if (struct_data.tm_mon < struct_dataNascimento.tm_mon):
            diferencaAno = diferencaAno - 1
        elif (struct_data.tm_mon == struct_dataNascimento.tm_mon):
            if (struct_data.tm_mday < struct_dataNascimento.tm_mday):
                diferencaAno = diferencaAno - 1
        
        return diferencaAno

# 2c
    def __str__(self):
        """Função imprime informações da pessoa como o nome, data de nascimento, nome
        da mãe e nome do pai"""

        return "nome: {}, idade: {}, mae: {}, pai: {}".format(self.nome, Pessoa.idade(self), self.nomeDeMae, self.nomeDePai)
