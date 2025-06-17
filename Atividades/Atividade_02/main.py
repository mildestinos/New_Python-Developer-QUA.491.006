while True:
    try:
        # Entrada de dados
        nome = input('Informe seu nome: ').strip().title()
        peso = float(input('Informe seu peso em kg: ').replace(',', '.'))
        altura = float(input('Informe sua altura em metros: ').replace(',', '.'))

        # Cálculo do IMC
        imc = peso / altura**2
        print(f"\nO valor do IMC de {nome} é: {imc:.2f}.")

        # Condições baseadas no IMC
        if imc < 18.5:
            print(f"{nome} está abaixo do peso.")
        elif imc < 25:
            print(f"{nome} está no peso ideal.")
        elif imc < 30:
            print(f"{nome} está com sobrepeso.")
        elif imc < 35:
            print(f"{nome} está com obesidade grau I.")
        elif imc < 40:
            print(f"{nome} está com obesidade grau II.")
        else:
            print(f"{nome} está com obesidade grau III (mórbida).")

        # Deseja refazer?
        while True:
            prosseguir = input("\nDeseja refazer? (s/n): ").strip().lower()
            if prosseguir in ["s", "n"]:
                break
            else:
                print("Opção inválida. Digite apenas 's' ou 'n'.")

        if prosseguir == "n":
            print("Encerrando o programa. Até logo!")
            break

    except Exception as e:
        print(f"Não foi possível calcular o IMC. Erro: {e}")
