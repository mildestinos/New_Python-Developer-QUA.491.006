class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco  # sem acento, por padronização

    # nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # telefone
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # endereco
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    # Método que retorna os dados da pessoa
    def obter_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"E-mail: {self.email}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}\n"
        )


# Classe Veiculo
class Veiculo:
    def __init__(self, modelo, fabricante, cor, placa, ano, proprietario):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__cor = cor
        self.__placa = placa
        self.__ano = ano
        self.__proprietario = proprietario

    # modelo
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    # fabricante
    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    # cor
    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    # placa
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    # ano
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    # proprietario
    @property
    def proprietario(self):
        return self.__proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
        self.__proprietario = proprietario

    # Método para exibir os dados do proprietário
    def info_proprietario(self):
        return self.proprietario.obter_dados()
