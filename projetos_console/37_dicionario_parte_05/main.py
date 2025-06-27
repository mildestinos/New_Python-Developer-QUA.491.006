usuario = {
    'Nome': "Alexa Machado", 
    'idade': 40,
    'email': "alex@gmail.com"
}

# Exibir os valores
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")

# Adicionar nova chave e valor
usuario['Profissão'] = input("Informe a profissão: ").strip()

print("-" * 40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
