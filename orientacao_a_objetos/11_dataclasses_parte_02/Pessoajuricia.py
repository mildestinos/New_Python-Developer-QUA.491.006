import Pessoa
from dataclasses import dataclass

@dataclass
class Pessoajuridica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia> str
    cnpj: str

class Empresa:
    def __init__(self, nome, cnpj, endereco, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return (
            f"{'-'*20} Dados da empresa {'-'*20}\n"
            f"Nome: {self.nome}\n"
            f"CNPJ: {self.cnpj}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}\n"
            f"{'-'*54}"
        )
