# listas

nomes = [
    "alexa",
    "joana",
    "joão",
    "Mariana",
    "Marios",
    "Fernanda"
]

# exibir a lista
for nome in nomes:
    print(nome)

# usuário informa nome a ser incluído na lista   
novo_nome = input("Informe nome novo: ").title().strip()

# novo nome é inserido na lista
nomes.append(novo_nome)

# re-exibir a lista
for nome in nomes:
    print(nome)