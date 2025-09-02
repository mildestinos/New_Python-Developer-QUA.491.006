from datetime import datetime, date
import os
import csv
from sqlalchemy import inspect

# ============== UTIL / UX DE CONSOLE ==============
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# ============== EXPORTAÇÃO (NOVOS ARQUIVOS) ==============
def gerar_nome_arquivo_unico(pasta="export", base="pessoas", extensao="csv", usar_timestamp=True):
    os.makedirs(pasta, exist_ok=True)
    if usar_timestamp:
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        return os.path.join(pasta, f"{base}_{ts}.{extensao}")
    # fallback incremental
    caminho = os.path.join(pasta, f"{base}.{extensao}")
    if not os.path.exists(caminho):
        return caminho
    i = 2
    while True:
        cand = os.path.join(pasta, f"{base}_v{i}.{extensao}")
        if not os.path.exists(cand):
            return cand
        i += 1

def _formatar_valor_csv(v):
    if v is None:
        return ""
    if isinstance(v, datetime):
        return v.strftime('%d/%m/%Y %H:%M:%S')
    if isinstance(v, date):
        return v.strftime('%d/%m/%Y')
    return str(v)

def exportar_pessoas_csv(session, Pessoa, caminho_arquivo=None, pasta="export",
                         base="pessoas", separador=';', incluir_cabecalho=True, novo_arquivo=True):
    """Exporta tabela Pessoa para CSV em arquivo único (timestamp por padrão)."""
    try:
        if novo_arquivo or not caminho_arquivo:
            caminho_arquivo = gerar_nome_arquivo_unico(pasta=pasta, base=base, extensao="csv", usar_timestamp=True)

        pessoas = session.query(Pessoa).order_by(Pessoa.id_pessoa).all()

        with open(caminho_arquivo, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f, delimiter=separador, quoting=csv.QUOTE_MINIMAL)
            if incluir_cabecalho:
                w.writerow(['id_pessoa', 'nome', 'email', 'data_nasc'])
            for p in pessoas:
                data_fmt = p.data_nasc.strftime('%d/%m/%Y') if getattr(p, 'data_nasc', None) else ''
                w.writerow([p.id_pessoa, p.nome, p.email, data_fmt])

        print(f"Export OK: {caminho_arquivo} ({len(pessoas)} registros).")
    except Exception as e:
        print(f"Falha ao exportar Pessoa -> CSV. Erro: {e}")

def exportar_banco_csv(session, pasta_saida="export", separador=';', sufixo_timestamp=True):
    """Exporta TODAS as tabelas (um CSV por tabela). Usa timestamp para gerar sempre outro arquivo."""
    try:
        engine = session.get_bind()
        insp = inspect(engine)
        os.makedirs(pasta_saida, exist_ok=True)
        preparer = engine.dialect.identifier_preparer

        ts = datetime.now().strftime('%Y%m%d_%H%M%S') if sufixo_timestamp else None
        total = 0

        for tabela in insp.get_table_names():
            colunas_meta = insp.get_columns(tabela)
            if not colunas_meta:
                continue

            colunas = [c['name'] for c in colunas_meta]
            nome_base = f"{tabela}_{ts}" if ts else tabela
            caminho_arquivo = os.path.join(pasta_saida, f"{nome_base}.csv")

            col_idents = ", ".join(preparer.quote(c) for c in colunas)
            tbl_ident = preparer.quote(tabela)
            sql = f"SELECT {col_idents} FROM {tbl_ident}"

            with engine.connect() as conn, \
                 open(caminho_arquivo, 'w', newline='', encoding='utf-8-sig') as f:
                w = csv.writer(f, delimiter=separador, quoting=csv.QUOTE_MINIMAL)
                w.writerow(colunas)
                result = conn.exec_driver_sql(sql)
                for row in result:
                    w.writerow([_formatar_valor_csv(v) for v in row])

            total += 1
            print(f"[OK] {tabela} -> {caminho_arquivo}")

        print(f"Exportação concluída. Arquivos gerados: {total}.")
    except Exception as e:
        print(f"Falha na exportação completa. Erro: {e}")

# ============== SUAS ROTINAS (AJUSTADAS) ==============
def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome da Pessoa: ").strip().title()
        email = input("Digite o Email: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email == email).all()

        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail já cadastrado !")
        else:
            data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ").strip()
            data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
            nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_nasc)

            session.add(nova_pessoa)
            session.commit()

            print(f"\nA Pessoa: {nome}, foi cadastrada com Sucesso!")
    except Exception as e:
        print(f"Não foi possível cadastrar! Erro: {e}")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPESSOAS CADASTRADAS:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            data_txt = pessoa.data_nasc.strftime('%d/%m/%Y') if getattr(pessoa, 'data_nasc', None) else ''
            print(f"Data_Nasc: {data_txt}")
            print(f"{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possível listar! Erro: {e}")

def pesquisar_pessoas(session, Pessoa):
    print(f"{'-'*20}  Filtrar pessoas por campo  {'-'*20}")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de Nasc.")
    print("5 - Retornar")

    campo = input("Informe o Campo a pesquisar: ").strip()
    limpar()

    pessoas = []
    match campo:
        case "1":
            valor = input("Digite o ID: ").strip()
            try:
                id_val = int(valor)
            except ValueError:
                print("ID inválido! Use número inteiro.")
                return
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa == id_val).all()
        case "2":
            valor = input("Digite o Nome: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o E-mail: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a Data de Nasc. (dd/mm/aaaa): ").strip()
            try:
                data_nasc = datetime.strptime(valor, "%d/%m/%Y").date()
                pessoas = session.query(Pessoa).filter(Pessoa.data_nasc == data_nasc).all()
            except ValueError:
                print("Data inválida!")
                return
        case "5":
            return
        case _:
            print("Campo inexistente!")
            return

    limpar()
    print("\nRESULTADO DA PESQUISA:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            data_txt = pessoa.data_nasc.strftime('%d/%m/%Y') if getattr(pessoa, 'data_nasc', None) else ''
            print(f"Data de Nasc.: {data_txt}\n")
            print(f"{'-'*40}\n")
    else:
        print("Nenhum registro encontrado!")

def alterar_dados(session, Pessoa):
    try:
        print("1 - Buscar por ID")
        print("2 - Buscar por Email")
        opcao = input("Escolha o campo para localizar a pessoa: ").strip()

        match opcao:
            case "1":
                id_txt = input("Informe o ID: ").strip()
                try:
                    id_pessoa = int(id_txt)
                except ValueError:
                    print("ID inválido! Use número inteiro.")
                    return
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe Email: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case _:
                print("Opção inválida!")
                return

        if pessoa:
            novo_nome = None
            novo_email = None
            nova_data_nasc = None

            while True:
                print("\nQual campo deseja alterar:\n")
                print(f"ID: {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                data_txt = pessoa.data_nasc.strftime('%d/%m/%Y') if getattr(pessoa, 'data_nasc', None) else ''
                print(f"3 - Data de Nasc.: {data_txt}")
                print("4 - Sair")
                campo = input("Informe o Campo: ").strip()

                limpar()

                match campo:
                    case "1":
                        novo_nome = input("Informe o novo Nome: ").strip().title()
                        print(f"Nome a ser cadastrado: {novo_nome}.")
                    case "2":
                        novo_email = input("Informe o novo E-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if novo_email in [p.email for p in pessoas if p.id_pessoa != pessoa.id_pessoa]:
                            print("E-mail já cadastrado!")
                            novo_email = None
                        else:
                            print(f"E-mail a ser cadastrado: {novo_email}.")
                    case "3":
                        nova_data_nasc = input("Informe a nova Data de Nasc. (dd/mm/aaaa): ").strip()
                        print(f"Data de nascimento a ser cadastrada: {nova_data_nasc}.")
                    case "4":
                        break
                    case _:
                        print("Campo inexistente!")
                        continue

            if novo_nome:
                pessoa.nome = novo_nome
            if novo_email:
                pessoa.email = novo_email
            if nova_data_nasc:
                try:
                    pessoa.data_nasc = datetime.strptime(nova_data_nasc, "%d/%m/%Y").date()
                except ValueError:
                    print("Data inválida, não alterada.")

            session.commit()
            print("Dados alterados com sucesso!")
        else:
            print("Pessoa não encontrada!")
    except Exception as e:
        print(f"Não foi possível alterar! Erro: {e}")
        session.rollback()

# ==================== GANCHOS DE USO ====================
# Exemplos de chamadas (coloque no seu menu principal ou onde fizer sentido):
# exportar_pessoas_csv(session, Pessoa, novo_arquivo=True)  # gera export/pessoas_YYYYMMDD_HHMMSS.csv
# exportar_pessoas_csv(session, Pessoa, novo_arquivo=True, pasta="exports_diarios")
# exportar_pessoas_csv(session, Pessoa, novo_arquivo=True, base="backup_pessoas")
# exportar_banco_csv(session, sufixo_timestamp=True)        # um CSV por tabela, todos com timestamp
