#deletar item do dicionário

usuario = {
    'Nome': "Alexa Machado", 
    'idade': 40,
    'email': "alex@gmail.com",
    'Profissão': "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
    print("-" * 40)

    # usuario informa a chava que desaja excluir
chave = input("Informe a chave que deseja excluir: ").strip().strip()

#verifica se a chave existe no dicionário

if chave in usuario:

    del usuario[chave]
else:
    print("CHAVE NÃO EXISTE NO DICIONÁRIO")

print("-" * 40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")   