'''
# TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.

3. Opções do menu:
4. - Criar novo arquivo JSON (usuário irá informar o diretório).
5. - Abrir arquivo JSON (usuário irá informar o diretório).
6. - Cadastrar novo usuário em um JSON.
7. - Listar todos os usuários de um arquivo JSON.
8. - Pesquisar por um usuário de um arquivo JSON.
9. - Alterar dados de um usuário em um arquivo JSON.
10. - Deletar usuário de um arquivo JSON.
11. - Sair do programa

12. Dados do usuário:
13. - Nome
14. - Data de nascimento
15. - CPF
16. - E-mail
17. - Telefone
18. - Filme favorito do usuário
'''

import os
import json

usuarios = {}

#OPÇÃO DE MENU

print("\n========== 🐍MENU PRINCIPAL ==========")
print("1 - Criar novo arquivo JSON (usuário irá informar o diretório).")
print("2 - Abrir arquivo JSON (usuário irá informar o diretório).")
print("3 - Cadastrar novo usuário em um JSON.")
print("4 - Listar todos os usuários de um arquivo JSON.")
print("5 - Pesquisar por um usuário de um arquivo JSON.")
print("6 - Alterar dados de um usuário em um arquivo JSON.")
print("7 - Deletar usuário de um arquivo JSON.")
print("8 - Sair do programa.")
print("====================================")

try:
        opcao = input("Informe a opção desejada: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        match opcao:
                
                #Criar novo arquivo JSON (usuário irá informar o diretório)

            case "1":
                nome_arquivo = input("Informe o nome do novo arquivo: ").strip().lower()
                caminho_arquivo = f"Atividades_10/{nome_arquivo}.json"
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                print("Arquivo criado com sucesso.")
        
                #Abrir arquivo JSON (usuário irá informar o diretório)  
                 
            case "2":
                caminho_arquivo = input("Informe o caminho do arquivo JSON: ").strip()
                if not os.path.exists(caminho_arquivo):
                    print("Arquivo não encontrado.")
                    caminho_arquivo = ""
                else:
                    print("Arquivo carregado com sucesso.")

        
        
            case "3":
                if not caminho_arquivo:
                    print("Nenhum arquivo carregado. Use a opção 1 ou 2 primeiro.")
                    continue
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                
                usuario = {
                    "nome": input("Nome: "),
                    "nascimento": input("Data de nascimento: "),
                    "cpf": input("CPF: "),
                    "email": input("E-mail: "),
                    "telefone": input("Telefone: "),
                    "filme": input("Filme favorito: ")
            }

                usuarios.append(usuario)
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print("Usuário cadastrado com sucesso.")
        
        
                case "4":
        
        
                case "5":
        
        


#DADOS DO USUARIO








