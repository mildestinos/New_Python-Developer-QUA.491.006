class Aluno:
    def __init_(self,nome_aluno,matricula):
        self.__nome_aluno = nome_aluno
        self.__matricula = matricula

    @property
    def nome_aluno(self):
        return self.__nome_aluno
    
    @nome_aluno.setter
    def nome_aluno(self,nome_aluno):
        self.__nome_aluno - nome_aluno

    @property
    def matricula(self):
            return self.__matricula

    @matricula.setter
    def matricula(self,natricula):
        return self.__matricula
    
