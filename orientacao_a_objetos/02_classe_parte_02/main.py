# Classe Pessoa
class Pessoa:
    # Construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    # Ação de se apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu email é {self.email}.")


# Algoritmo principal
if __name__ == "__main__":
    # Instanciando a classe Pessoa
    usuario = Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )

    try:
        usuario.nome = input("Digite seu nome: ").strip().title()
        usuario.idade = int(input("Digite sua idade: "))
        usuario.telefone = input("Digite seu telefone: ").strip()  # Corrigido: adicionado parênteses
        usuario.cpf = input("Digite seu CPF: ").strip()  # Corrigido: adicionado parênteses
        usuario.email = input("Digite seu email: ").strip().lower()

        # Apresentando os dados
        print(usuario.apresentar())

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
