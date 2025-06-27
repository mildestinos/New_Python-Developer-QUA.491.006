#dionario

chaves = ('Nome','idade','email','telefone','Profissão')

usuario = {
    chaves[0]: "Alex machado",
    chaves[1]: 40,
    chaves[2]: "Alex@gmail.com",
    chaves[3]: "55-5555555",
    chaves[4]: "programamador",
}

for chave in chaves:
    print ("*"*40)
    print(f"{chave}: {usuario.get(chave)}")
