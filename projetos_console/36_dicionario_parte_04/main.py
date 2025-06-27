#dicionario

usuario = dict(none = "Alexa Machado", idade = 40, email = "alex@gmail.com")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")


    '''
    Dicionários em Python são estruturas de dados que armazenam pares chave: valor.
    Eles são úteis quando você quer associar uma chave a um valor (como um nome a uma idade, por exemplo).
    
    
    
    '''