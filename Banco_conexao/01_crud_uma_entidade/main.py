from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

# Criar base declarativa
Base = declarative_base()

# Definir classe Pessoa
class Pessoa(Base):
    __tablename__ = "pessoa"

    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    data_nasc = Column(Date, nullable=False)

# Função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def criar_tab_pessoa(engine):
    try:
        Base.metadata.create_all(engine)
        print("Tabela criada com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao Banco. {e}")

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
    pessoas = session.query(Pessoa).all()
    if pessoas:
        print("\nLista de Pessoas:")
        for p in pessoas:
            print(f"ID: {p.id_pessoa} | Nome: {p.nome} | Email: {p.email} | Nasc: {p.data_nasc.strftime('%d/%m/%Y')}")
    else:
        print("Nenhuma pessoa cadastrada.")

def atualizar_pessoa(session):
    try:
        id_alvo = int(input("Digite o ID da pessoa que deseja atualizar: "))
        pessoa = session.query(Pessoa).get(id_alvo)
        if not pessoa:
            print("Pessoa não encontrada.")
            return

        print("Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual ({pessoa.nome}): ").strip().title()
        novo_email = input(f"Email atual ({pessoa.email}): ").strip().lower()
        nova_data = input(f"Data Nasc atual ({pessoa.data_nasc.strftime('%d/%m/%Y')}): ").strip()

        if novo_nome:
            pessoa.nome = novo_nome
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
        id_alvo = int(input("Digite o ID da pessoa que deseja deletar: "))
        pessoa = session.query(Pessoa).get(id_alvo)
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

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    criar_tab_pessoa(engine)

    Session = sessionmaker(bind=engine)
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

        match opcao:
            case "1":
                limpar_tela()
                cadastrar_pessoa(session)
            case "2":
                limpar_tela()
                listar_pessoas(session)
            case "3":
                limpar_tela()
                atualizar_pessoa(session)
            case "4":
                limpar_tela()
                deletar_pessoa(session)
            case "5":
                print(f'{"-"*30}\nFIM DO PROGRAMA\n{"-"*30}')
                break
            case _:
                print("Opção inválida!")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
