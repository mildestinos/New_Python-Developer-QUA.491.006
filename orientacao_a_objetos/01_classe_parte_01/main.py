# Classe
class Pessoa:
    # Atributos da classe
    Nome = "Eric"
    idade = 30
    telefone = "(61) 8852-4175"
    cpf = "123.456.789-00"
    email = "adm.esv@gmail.com"

    # Método para se apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.Nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu email é {self.email}.")

# Programa principal
if __name__ == "__main__":
    # Instanciando a classe Pessoa
    usuario = Pessoa()

    # O objeto se apresenta
    usuario.apresentar()
