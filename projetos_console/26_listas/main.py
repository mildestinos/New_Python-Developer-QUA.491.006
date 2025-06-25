#bibliotecas

import os
import random


#lista

nomes = []

while True:
    
    print("1 - Inserir nome na lista")
    print("2 - Exibir nomes na lista") 
    print("3 - Sortear nome")
    print("4 - Sair do programa")
       
    opcao = input("Escolha uma opção: ")

    os.system("cls" if os.name == "nt" else "clear")
    
    match opcao:

        case "1":
             try:
                
               novo_nome = input("Infome nome: ").title().strip()
               os.system("cls" if os.name == "nt" else "clear")
               nomes.append(novo_nome)
               print(f"Nome '{novo_nome}' adicionado com sucesso!")
             except Exception as e:
                print(f"Não foi possívem inserir o nome na lista.{e}.")   

          
        case "2":
            try:
                #ordenar a lista
                nomes.sort()
                for nome in nomes:
                    print(nome)
                    print("-" * 40)
            except Exception as e:
                    print(f"Não foi possível exibir o nome da lista. {e}.")
            finally:
                continue

        case "3":
            i =  random.randint(0, len(nomes) - 1)  
            print(f"Nome sorteado: {nomes[i]}")
            continue
        case "4":
            print("Programa enceerrado...")
            break
        case _:
            print("Opção inválida.")
            continue
               
