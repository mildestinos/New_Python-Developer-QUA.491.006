#listas
cidades = [
    "São Paulo", 
    "Rio de Janeiro", 
    "Belo Horizonte", 
    "Curitiba", 
    "Porto Alegre"
] 

# excluir nomes da lista
for i in range(len(cidades)):
    print(f"{i}: {cidades[i]}.")

#usuário informa o nome da cidade a ser excluída
try:
    i=int(input("Informe o índice da cidade que deseja excluir: ")) 
    if i >= 0 and i < len(cidades):

        # exclui cidade da lista
        del cidades[i]
        print("Cidade excluída com sucesso!")
    else:
        print("Índice inválido.")
except Exception as e:
    print(f"Não foi possível excluir a cidade.{e}.")    
finally:
    # re-exibir a lista e suas posições
    for i in range(len(cidades)):
        print(f"{i}: {cidades[i]}.")
    