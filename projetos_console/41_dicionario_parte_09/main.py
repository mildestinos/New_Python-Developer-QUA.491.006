usuario = [
    {
        'Nome': "Alexa Machado", 
        'idade': 40,
        'email': "alex@gmail.com",
        'Profissão': "programador"
    },
    {
        'Nome': "eric", 
        'idade': 49,
        'email': "eric@gmail.com",
        'Profissão': "surfista"
    },
    {
        'Nome': "Joaão", 
        'idade': 88,
        'email': "joão@gmail.com",
        'Profissão': "seifador"
    }
]

# exibir os dados

for usuario in usuario:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}:{usuario.get(chave)}")
        