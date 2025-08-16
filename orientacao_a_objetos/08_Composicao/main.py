import classes as c

def main():
    # Criando o proprietário do veículo com dados em branco
    proprietario = c.Pessoa(
        nome="",
        cpf="",
        email="",
        telefone="",
        endereco=""
    )

    # Criando o veículo com dados em branco (passa proprietario como None inicialmente)
    carro = c.Veiculo(
        modelo="",
        fabricante="",  # corrigido aqui
        cor="",
        placa="",
        ano="",
        proprietario=None  # melhor usar None e atribuir depois
    )

    # Coletando dados do proprietário
    print("DADOS DO PROPRIETARIO:")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o email: ").strip().lower()
    proprietario.telefone = input("Informe o telefone: ").strip()
    proprietario.endereco = input("Informe o endereço: ").strip().title()

    # Coletando dados do veículo
    print("DADOS DO VEÍCULO:")
    carro.fabricante = input("Informe o Fabricante: ").strip().title()
    carro.modelo = input("Informe o modelo: ").strip().title()
    carro.cor = input("Informe a cor: ").strip()
    carro.placa = input("Informe a placa: ").strip().upper()
    carro.ano = input("Informe o ano: ").strip()

    # Atribuindo o proprietário ao veículo
    carro.proprietario = proprietario

    # Exibindo os dados
    print("\nExibindo os dados do veículo:\n")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Ano: {carro.ano}")
    print(f"Placa: {carro.placa}")
    print(f"Cor: {carro.cor}")
    print(f"Dados do Proprietário do veículo: {carro.proprietario.nome}")

if __name__ == "__main__":
    main()
