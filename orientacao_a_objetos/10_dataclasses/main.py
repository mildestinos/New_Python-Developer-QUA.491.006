import Pessoa

def main():
    usuario = Pessoa.Pessoa(
        nome="", email="", cpf="", idade=0, altura=0.0
    )

    # Inputs do usuário
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.email = input("Informe seu e-mail: ").strip().lower()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.altura = float(input("Informe sua altura: ").replace(",", "."))

    # Exibindo os dados
    print("\n--- Dados cadastrados ---")
    print(usuario)

if __name__ == "__main__":
    main()
