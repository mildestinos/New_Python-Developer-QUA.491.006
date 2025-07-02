import os
import random

usuarios = []

while True:
    print("\n--- 🐍MENU ---")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar dados de um usuário")
    print("4 - Fazer o sorteio de usuário")
    print("5 - Excluir um usuário")
    print("6 - Sair")

    try:
        opcao = input("Informe a opção desejada: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        match opcao:
            case "1":  # cadastrar
                try:
                    novo_nome = input("Informe novo nome: ").title().strip()
                    usuarios.append(novo_nome)
                    print(f"{novo_nome} adicionado com sucesso!")
                except Exception as e:
                    print(f"Erro ao adicionar nome: {e}")

            case "2":  # listar
                try:
                    if usuarios:
                        print("Nomes Cadastrados:")
                        for i, nome in enumerate(usuarios, 1):
                            print(f"{i:02d}. {nome}")
                    else:
                        print("A lista está vazia.")
                except Exception as e:
                    print(f"Erro ao listar nomes: {e}")

            case "3":  # alterar dados
                try:
                    nome_antigo = input("Digite o nome que deseja alterar: ").title().strip()
                    if nome_antigo in usuarios:
                        novo_nome = input("Digite o novo nome: ").title().strip()
                        indice = usuarios.index(nome_antigo)
                        usuarios[indice] = novo_nome
                        print("Nome alterado com sucesso!")
                    else:
                        print("Nome não encontrado na lista.")
                except Exception as e:
                    print(f"Erro ao alterar nome: {e}")

            case "4":  # fazer sorteio
                try:
                    if usuarios:
                        sorteado = random.choice(usuarios)
                        print(f"Usuário sorteado: {sorteado}")
                    else:
                        print("A lista está vazia.")
                except Exception as e:
                    print(f"Não foi possível realizar o sorteio. {e}")

            case "5":  # excluir usuário
                try:
                    nome_excluir = input("Digite o nome que deseja excluir: ").title().strip()
                    if nome_excluir in usuarios:
                        usuarios.remove(nome_excluir)
                        print(f"{nome_excluir} foi removido da lista.")
                    else:
                        print("Nome não encontrado na lista.")
                except Exception as e:
                    print(f"Erro ao excluir nome: {e}")

            case "6":  # sair
                print("Encerrando o programa...")
                break

            case _:  # opção inválida
                print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
