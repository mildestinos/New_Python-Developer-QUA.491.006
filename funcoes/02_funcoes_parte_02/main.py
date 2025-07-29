#função def diz ao Python que você está criando uma função.
def mostrar_msg(nome):
    return f"seja bem vindo,{nome}"


#programa principal
nome = input("Digite seu nome: ").strip().title()
print(mostrar_msg(nome))
