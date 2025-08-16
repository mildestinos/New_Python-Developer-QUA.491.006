#importa o dataclass
from dataclasses import dataclass
# classe pessoa
@dataclass
class Pessoa:
    #atributos
    nome:str
    email:str
    cpf:str
    idade:int
    altura: float

    def __str__(self):
        return (f"Nome: {self.nome} ({len(self.nome)} letras)\n"
            f"E-mail: {self.email}\n"
            f"CPF: {self.cpf}\n"
            f"Idade: {self.idade} anos\n"
            f"Altura: {self.altura:.2f} m")
    def __len__(self):
        return self.idade
    

    