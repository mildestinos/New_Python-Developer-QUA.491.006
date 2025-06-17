#Importar bibliotecas
import os

while True:
    nome = input("Informe seu nome: ")
    os.system("cls")
    print(f"Seja bem vindo,{nome}!")

    prosseguir = input("Deseja continuar? (S/N): ").lower().upper()

    match prosseguir:
       case "S":
        os.system("cls")
        continue
       case "n":
        break
       case _:
        print("Opção inválida. Encerrando o programa...")
        break