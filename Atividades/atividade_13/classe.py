import json



# classe
class Conta:
    def __init__(self, titular, cpf, agencia, conta, saldo):
        # atributos
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []  # opcional: registrar histórico

    # métodos
    def consultar_dados(self):
        print(f"Titular: {self.titular}.")
        print(f"CPF: {self.cpf}.")
        print(f"Agência: {self.agencia}.")
        print(f"Número da conta: {self.conta}.")
        print(f"Saldo: R${self.saldo:.2f}.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor  # Corrigido: usar self.saldo
            self.extrato.append(f"Depósito: +R${valor:.2f}")
        else:
            print("Valor inválido para depósito.")
        return self.saldo
        
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor  # Corrigido: usar self.saldo
            self.extrato.append(f"Saque: -R${valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")
        return self.saldo
    
    def imprimir_extrato(self):
        dados = {
            "titular": self.titular,
            "cpf": self.cpf,
            "Agência": self.agencia,
            "Conta": self.conta,
            "Saldo": self.saldo
        }            
        with open("extrato.json", "w",encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

