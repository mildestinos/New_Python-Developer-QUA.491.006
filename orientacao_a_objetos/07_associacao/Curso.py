class Curso:
    def __init__(self,nome_curso):
        self.__nome_curso = nome_curso
        
        @property
        def