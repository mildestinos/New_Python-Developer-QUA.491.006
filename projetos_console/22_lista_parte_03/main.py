# listas
cidades = [
    "São Paulo", 
    "Rio de Janeiro", 
    "Belo Horizonte", 
    "Curitiba", 
    "Porto Alegre"
] 
for i in range(len(cidades)):
    print(f"Indice{i}:{cidades[i]}.")

try:
    # usuário informa cidade a ser incluída na lista
    nova_cidade = input("Informe cidade nova: ").title().strip()
    i = int(input("Informe o índice onde a cidade será inserida: "))

    if i >= 0 and i <= len(cidades):

        # nova cidade é inserida na lista
        cidades.insert(i, nova_cidade)
        print("Cidade inserida com sucesso!")
    else:
        
        print("Indice invalido.")
        
except Exception as e:
    print(f"Não foi possível inserier item na lista.{e}.")
finally:
   #re-exibir a lista e suas posições
    for i in range(len(cidades)):
        print(f"Indice{i}:{cidades[i]}.")