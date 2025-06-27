#dicionario

usuario = {
    'Nome': "Alexa Machado", 
    'idade': 40,
    'email': "alex@gmail.com",
    'Profissão': "programador"
}

for chave, valor in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-" *40)


# usuario informa a chave que deseja alterar
chave = input("Informe a chave que deseja alterar: ").strip()

#usuario informa o novo valor
if chave in usuario:
    usuario[chave] = input("Informe o novo valor de {chave}: ").strip()
else:
    print(f"A chave não existe no dicionário.")

print("-" * 40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")    