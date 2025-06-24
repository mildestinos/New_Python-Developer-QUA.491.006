cidades = [
    "Brasília",
    "Brasília",
    "Salvador",
    "Fortaleza",    
    "São Paulo",
    "Brasília",
    "Salvador", 
    "Rio de Janeiro", 
    "Belo Horizonte", 
    "Curitiba",
    "São Paulo",
    "Rio de Janeiro", 
    "Porto Alegre",
    "Recife",
    "Manaus",
    "Belém",
    "Manaus",
    "Curitiba"
    ]

# usuário informa o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade: ").title().strip()

# programa indica quantas vezes  o item foi encontrado
qtde = cidades.count(cidade_pesquisada)

#programa informa quantas vezes o item foi encontrado
print(f"{cidade_pesquisada} foi encontrada {qtde} vezes na lista.")    