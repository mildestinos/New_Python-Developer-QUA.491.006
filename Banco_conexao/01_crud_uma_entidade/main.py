from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Importa a Base e a entidade do arquivo entidades.py
from entidades import Base, Pessoa


# --------- Utilidades ----------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def criar_tab_pessoa(engine):
    try:
        Base.metadata.create_all(engine)
        print("Tabela criada com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao Banco. {e}")


# --------- Operações CRUD ----------
def cadastrar_pessoa(session):
    try:
        nome = input("Digite Nome do Usuário: ").strip().title()
        email = input("Digite Seu Email: ").strip().lower()
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ").strip()

        data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

        nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_formatada)
        session.add(nova_pessoa)
        session.commit()
        print(f"Pessoa '{nome}' cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
        session.rollback()


def listar_pessoas(session):
    try:
        pessoas = session.query(Pessoa).all()
        if pessoas:
            print("\nLista de Pessoas:")
            for p in pessoas:
                nasc_str = p.data_nasc.strftime('%d/%m/%Y') if p.data_nasc else "-"
                print(f"ID: {p.id_pessoa} | Nome: {p.nome} | Email: {p.email} | Nasc: {nasc_str}")
        else:
            print("Nenhuma pessoa cadastrada.")
    except Exception as e:
        print(f"Erro ao listar: {e}")


def atualizar_pessoa(session):
    try:
        id_alvo = int(input("Digite o ID da pessoa que deseja atualizar: ").strip())

        # SQLAlchemy 2.x: prefira session.get(Model, pk)
        pessoa = session.get(Pessoa, id_alvo)
        if not pessoa:
            print("Pessoa não encontrada.")
            return

        print("Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual ({pessoa.nome}): ").strip()
        novo_email = input(f"Email atual ({pessoa.email}): ").strip().lower()
        atual_data = pessoa.data_nasc.strftime('%d/%m/%Y') if pessoa.data_nasc else "-"
        nova_data = input(f"Data Nasc atual ({atual_data}): ").strip()

        if novo_nome:
            pessoa.nome = novo_nome.title()
        if novo_email:
            pessoa.email = novo_email
        if nova_data:
            pessoa.data_nasc = datetime.strptime(nova_data, "%d/%m/%Y").date()

        session.commit()
        print("Pessoa atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
        session.rollback()


def deletar_pessoa(session):
    try:
        id_alvo = int(input("Digite o ID da pessoa que deseja deletar: ").strip())
        pessoa = session.get(Pessoa, id_alvo)
        if not pessoa:
            print("Pessoa não encontrada.")
            return

        confirmar = input(f"Tem certeza que deseja deletar '{pessoa.nome}'? (s/n): ").strip().lower()
        if confirmar == 's':
            session.delete(pessoa)
            session.commit()
            print("Pessoa deletada com sucesso!")
        else:
            print("Operação cancelada.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        session.rollback()


# --------- App ---------
def main():
    # Garante diretório do banco (opcional)
    db_path = "01_crud_uma_entidade/database"
    os.makedirs(db_path, exist_ok=True)

    engine = create_engine(f"sqlite:///{db_path}/db_crud.db", echo=False, future=True)
    criar_tab_pessoa(engine)

    Session = sessionmaker(bind=engine, future=True)
    session = Session()

    while True:
        limpar_tela()
        print("MENU".center(30, "-"))
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoa")
        print("4 - Deletar Pessoa")
        print("5 - Sair")
        print("-" * 30)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            cadastrar_pessoa(session)
        elif opcao == "2":
            limpar_tela()
            listar_pessoas(session)
        elif opcao == "3":
            limpar_tela()
            atualizar_pessoa(session)
        elif opcao == "4":
            limpar_tela()
            deletar_pessoa(session)
        elif opcao == "5":
            print(f'{"-"*30}\nFIM DO PROGRAMA\n{"-"*30}')
            break
        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")

    session.close()


if __name__ == "__main__":
    main()
