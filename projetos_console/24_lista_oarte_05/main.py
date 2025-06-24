#lista
itens = [
    "arroz", 
    "feijão", 
    "macarrão", 
    "farinha", 
    "açúcar",
    "ovos", 
    "leite", 
    "frutas", 
    "verduras", 
    "frango"
]

# exibe listas de compras
for i in range(len(itens)):
    print(f"Indice {i}: {itens[i]}.") 

#usuário informa o indice a ser alterado

try:
    # usuário informa i indice a ser alterado
    i= int(input("Informe o índice do item que deseja alterar: "))

    if i < 0 or i >= len(itens):
      
      itens[i] = input("Informe o novo item: ").strip().lower()
    print(f"Item alterado com sucesso")

except Exception as e:
    print(f"Erro ao alterar o item da lista.{e}.")  
finally:
        for i in range(len(itens)):
         print(f"Indice {i}: {itens[i]}.") 