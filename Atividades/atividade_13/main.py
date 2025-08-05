import classe as c
import os

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    cc= c.Conta(titular="", cpf="", agencia="", conta="", saldo=0.0)

    cc.titular = input("Digite o nome do titular da conta: ").strip().title()   
    cc.cpf = input("Digite o CPF do titular: ").strip()
    cc.agencia = "1010-1"
    cc.conta = "10101-1"

    limpar()
    while True:
        print(f"{'-'*20} Banco Cobra 🐍{'-'*20}")
        print("1. Consultar dados")
        print("2. depositar valor")
        print("3. Sacar Valor")
        print("4. Imprimir extrato")
        print("5. Sair do programa")
        opcao = input("Escolha uma opção: ").strip()
        limpar()
        match opcao:
            case "1":
                cc.consultar_dados()
                continue
                                   
            case "2":
                try:
                    valor= float(input("Digite o valor a ser depositado: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:  
                        print(f"Depósito realizado com sucesso! Novo saldo: R$ {cc.depositar(valor):.2f}")
                    else:
                        print("Valor inválido. Tente novamente.")
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue
            case "3":
                try:
                    valor = float(input("Digite o valor do saque: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:
                        if valor <= cc.saldo:
                            print(f"Saque realizado com sucesso! Novo saldo: R$ {cc.sacar(valor):.2f}")
                            ...
                        else:
                            print("Saldo insuficiente.")
                        ...
                    else:
                        print("Valor inválido. Tente novamente.")   
                except Exception as e:
                    print(f"Erro: {e}") 
                        
                finally:
                    continue
                
            case "4":
                try:
                    cc.imprimir_extrato()
                    print("Extrato gerado com sucesso no arquivo 'extrato.json'.")
                    ...
                except Exception as e:
                    print(f"Erro ao gerar extrato: {e}")
                finally:
                    continue
            case "5":
                print("Programa encerrado.")
                break
                ...

            case _:
                print("Opção inválida.")
                continue






"""
# TODO - atividade: Crie um programa de aplicativo de banco, onde:
# O usuário cria uma conta no banco com os seguintes dados:
# -- Titular da conta
# -- CPF do titular
# -- Agência
# -- Número da conta
# -- Saldo
# -- O usuário pode fazer no programa:
# -- Consultar dados
# -- Depositar valor
# -- Sacar valor
# -- Imprimir extrato (entende-se: gerar arquivo com os dados da conta)
# -- Sair do programa
# NOTE - o nome da classe é conta.
"""
 