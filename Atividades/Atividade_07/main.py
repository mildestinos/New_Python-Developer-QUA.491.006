"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa

# NOTE - a lista deve começar vazia. Exemplo: lista = []

"""

import os   

lista = []

while True:
    print("\n--- menu 🐍 ---")
    print("1 - Cadastre novo nome na lista")
    print("2 - Liste todos os nomes na lista")  
    print("3 - Pesquise por um nome na lista")
    print("4 - Altere um nome na lista")
    print("5 - Exclua um nome na lista")
    print("6 - Sair do programa")   

    try:
        opcao = input("Informe a opção desejada: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        match opcao:
            case "1":
                try:
                    novo_nome = input("Informe novo nome: ").title().strip()
                    lista.append(novo_nome)
                    print(f"{novo_nome} adicionado com sucesso!")
                except Exception as e:
                    print(f"Erro ao adicionar nome: {e}")

            case "2":
                try:
                    if lista:
                        print("Nomes cadastrados:")
                        for i, nome in enumerate(lista, 1):
                            print(f"{i:02d}. {nome}")
                    else:
                        print("A lista está vazia.")
                except Exception as e:
                    print(f"Erro ao listar nomes: {e}")

            case "3":
                try:
                    nome = input("Digite o nome para pesquisar: ").title().strip()
                    if nome in lista:
                        print(f"Nome '{nome}' encontrado na lista.")
                    else:
                        print(f"Nome '{nome}' não encontrado.")
                except Exception as e:
                    print(f"Erro ao pesquisar nome: {e}")

            case "4":
                try:
                    nome_antigo = input("Digite o nome que deseja alterar: ").title().strip()
                    if nome_antigo in lista:
                        novo_nome = input("Digite o novo nome: ").title().strip()
                        indice = lista.index(nome_antigo)
                        lista[indice] = novo_nome
                        print("Nome alterado com sucesso!")
                    else:
                        print("Nome não encontrado na lista.")
                except Exception as e:
                    print(f"Erro ao alterar nome: {e}")

            case "5":
                try:
                    nome = input("Digite o nome que deseja excluir: ").title().strip()
                    if nome in lista:
                        lista.remove(nome)
                        print("Nome excluído com sucesso!")
                    else:
                        print("Nome não encontrado na lista.")
                except Exception as e:
                    print(f"Erro ao excluir nome: {e}")

            case "6":
                print("Programa encerrado. Até logo!")
                break

            case _:
                print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")  # pausa para o usuário ver o resultado
        os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
