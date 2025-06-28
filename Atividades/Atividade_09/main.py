'''
# TODO - atividade: Crie um programa que faça as seguintes funções:
# Cadastre um novo usuário
# Liste todos os usuários cadastrados
# Altere os dados de um usuário
# Fazer o sorteio de usuário
# Exclua um usuário
# Saia do programa
# NOTE - dados do usuário:
# - Nome completo
# - Data de Nascimento
# - E-mail
# - CPF
# - Telefone
# - Gênero
# - Data do cadastro (pegar do sistema)
# - Hora do cadastro (pegar do sistema)
# ---


'''
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
            case "1": #cadastrar
                try:
                    novo_nome = input("Informe novo nome: ").title().strip()
                    usuarios.append(novo_nome)
                    print(f"{novo_nome} adicionado com sucesso!")
                except Exception as e:
                    print(f"Erro ao adicionar nome: {e}")

            case "2": #listar
                try:
                    if usuarios:
                        print("Nomes Cadastrados")
                        for i, nome in enumerate(usuarios,1):
                            print(f"{i:02d}. {nome}")
                    else:
                        print("A lista Esta vazia")
                except Exception as e: 
                    print(f"Erro ao listar  nomes: {e}")

            case "3": #alterar dados
                try:
                    nome_antigo = input ("Digite o nome que deseja alterar:").title().strip()
                    if nome_antigo in usuarios:
                        novo_nome = input ("Digite o  novo nome:").title().strip()
                        indice = usuarios.index (nome_antigo)
                        usuarios[indice] = novo_nome
                        print("Nome alterado com sucesso!")
                    else:
                         print("nome não encontrado da lista.")
                except Exception as e:
                    print(f"Erro ao alterar nome: {e}")

            case "4": # fazer sorteio
                try:
                    if usuarios:
                        for usuario in sorted (usuarios):
                            print(usuarios)
                    else:
                        print("A lista está vazia.")
                except Exception as e:
                    print(f"Não foi possível realizar o sorteio. {e}.")
    finally:
        continue

                        
        case _:
                    print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")  # pausa para o usuário ver o resultado
        os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

