import json
import os

usuarios = []

while True:
    usuario = {}

    print("1- Cadastrar novo usuario.")
    print("2- Salvar aquivo JSON.")
    print("3- Fazer leitura do JSON.")
    print("4- Sair do programa.")

    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            usuario['nome'] = input("Informe o nome: ").strip().lower()
            usuario['idade'] = int(input("Informe a idade: "))
            usuario['email'] = input("Informe o email: ").strip().lower()
            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso.")
            continue

        case "2":
            novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print("Arquivo salvo com sucesso.")
            continue

        case "3":
            with open(f"50_json_parte_04/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(f"{'-'*20} USUARIOS {'-'*20}\n")
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print("-" * 40)

        case "4":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
            continue
