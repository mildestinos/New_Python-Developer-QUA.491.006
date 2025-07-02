"""
Atividade 09 - Crie um programa que faça as seguintes operacoes:
1. cadastre novos usuarios
2. liste todos os usuarios cadastrados
3. altere os dados de um usuario
4. sortear um usuario cadastrado
5. excluir um usuario cadastrado
6. sair do programa

DADOS DO USUARIO:
nome completo
data de nascimento
email
cpf
telefone
genero
data de cadastro
hora de cadastro

"""

import os
import random
from datetime import datetime

lista_de_usuarios = []
tupla_chaves_usuario = ("Nome", "Data de Nascimento", "E-mail", "CPF", "Telefone", "Genero", "Data de Cadastro", "Hora de Cadastro")

while True:

    print("\n")
    print(f"{"="*30} MENU {"="*30}")
    print("1. Cadastrar novo usuário")
    print("2. Listar todos os usuários cadastrados")
    print("3. Alterar dados de um usuário")
    print("4. Sortear um usuário cadastrado")
    print("5. Excluir um usuário cadastrado")
    print("6. Sair do programa")
    opcao = input("Escolha uma opção: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:

        # CADASTRAR
        case "1":
            try:
                usuario = {
                    tupla_chaves_usuario[0]: input("Nome completo: ").strip(),
                    tupla_chaves_usuario[1]: input("Data de nascimento (dd/mm/aaaa): ").strip(),
                    tupla_chaves_usuario[2]: input("Email: ").strip(),
                    tupla_chaves_usuario[3]: input("CPF: ").strip(),
                    tupla_chaves_usuario[4]: input("Telefone: ").strip(),
                    tupla_chaves_usuario[5]: input("Gênero: ").strip(),
                    tupla_chaves_usuario[6]: datetime.now().strftime("%d/%m/%Y"),
                    tupla_chaves_usuario[7]: datetime.now().strftime("%H:%M:%S")
                }
                lista_de_usuarios.append(usuario)
                print("Usuário cadastrado com sucesso!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar cadastrar o novo usuario. Erro: {e}")
            finally:
                continue
        
        # LISTAR
        case "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                if not lista_de_usuarios:
                    print("Nenhum usuário cadastrado.\n")
                else:
                    for usuario in lista_de_usuarios:
                        print("-"*60)
                        print(f"Indice: {lista_de_usuarios.index(usuario)}")
                        for chave in usuario:
                            print(f"{chave.capitalize()}: {usuario[chave]}")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar listar os usuários. Erro: {e}")
            finally:
                continue
        
        # ALTERAR
        case "3":
            try:
                indice_usuario_alterar = int(input("Informe o indice do usuario que deseja alterar: ").strip())
                if indice_usuario_alterar >= 0 and indice_usuario_alterar < len(lista_de_usuarios):
                    chave_usuario_alterar = input("Informe o nome da chave do usuario que deseja alterar: ").strip().capitalize()
                    if chave_usuario_alterar in lista_de_usuarios[indice_usuario_alterar]:
                        novo_valor_chave_usuario_alterar = input(f"Digite o novo valor para '{chave_usuario_alterar}': ").strip()
                        lista_de_usuarios[indice_usuario_alterar][chave_usuario_alterar] = novo_valor_chave_usuario_alterar
                        print("Alteração realizada com sucesso!\n")
                    else:
                        print(f"A chave '{chave_usuario_alterar}' não existe no dicionário.\n")
                else:
                    print(f"O indice '{indice_usuario_alterar}' não existe!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar alterar o usuário. Erro: {e}")
            finally:
                continue
        
        # SORTEAR
        case "4":
            try:
                if not lista_de_usuarios:
                    print("Nenhum usuario cadastrado.\n")
                else: 
                    dicionario_usuario_sorteado = random.choice(lista_de_usuarios)
                    print("O usuario sorteado é...\n")
                    for chave in dicionario_usuario_sorteado:
                        print(f"{chave.capitalize()}: {dicionario_usuario_sorteado[chave]}")
                    print("\n")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar sortear um usuario. Erro: {e}")
            finally:
                continue
        
        # EXCLUIR
        case "5":
            try:
                indice_usuario_excluir = int(input("Informe o indice do usuario que deseja excluir: ").strip())
                dicionario_usuario_excluir = lista_de_usuarios[indice_usuario_excluir]
                if indice_usuario_excluir >= 0 and indice_usuario_excluir < len(lista_de_usuarios):
                    del(lista_de_usuarios[indice_usuario_excluir])
                    print(f"Usuario '{dicionario_usuario_excluir.get('Nome')}' excluido com sucesso!\n")
                else:
                    print(f"O indice '{indice_usuario_excluir}' não existe!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar excluir o usuário. Erro: {e}")
            finally:
                continue
        
        # SAIR
        case "6":
            print("Saindo do programa...")
            break
        
        case _:
            print("Opção inválida. Tente novamente.")
            continue