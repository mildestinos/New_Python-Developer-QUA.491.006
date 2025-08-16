from abc import ABC
from abc import abstractmethod

# Classe Abstrar
class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo):
      # Atributos Private
        self.__saldo = saldo

#Método GET E SET
@property
def saldo(self):
    return self.__saldo

@saldo.setter
def saldo(self, saldo):
    self.__saldo = saldo

    # Métado de Ação
    @abstractmethod
    def confultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        super().__init__(saldo)

#TITULAR DA CONTA
@property
def titular(self):
  return self.__titular

@titular.setter
def titular(self, titular):
    self.__titular = titular
    
#CPF DO TITULAR
@property
def cpf(self):
  return self.__cpf

@cpf.setter
def cpf(self, cpf):
    self.__cpf = cpf

#AGÊNCIA DO TITULAR
@property
def agencia(self):
  return self.__agencia

@agencia.setter
def agencia(self, agencia):
    self.__agencia = agencia

#CONTA DO TITULAR
@property
def conta(self):
  return self.__conta

@cpf.setter
def conta(self, conta):
    self.__conta = conta

#Métado da Interface
def consultar_dados(self):
    print(f"{'-'*20} DADOS DA CONTA {'-'*20}\n")
    print(f"Titular da Conta: {self.__titular}")
    print(f"CPF do Titular: {self.__cpf}")
    print(f"Agência: {self.__agencia}")
    print(f"Número da Conta: {self.__conta}")
    print(f"Saldo: R$ {self.__saldo:.2f}")


    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo