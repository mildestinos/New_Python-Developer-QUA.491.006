

nome = input('Informe seu nome: ')
Peso = int(input('Informe seu peso: '))
Altura = float(input('Informe sua altura em metros: ').replace(',', '.'))

# saída de dados
print(f'Nome", {nome}!')
print(f'{Peso}: {type(Peso)}.')
print(f'{Altura}: {type(Altura)}')


while True:
    try:
        
        calculo = Peso * Altura**2

        print(f"\nResultado: {calculo:.2f} kg/m² de IMC.")
        
        if calculo <= 18.5:
            print("✅ Abaixo do peso.")
        else:
            if calculo >= 18.5 and calculo < 25:
                print("✅ Peso normal.")
            if calculo >= 30 and calculo < 35:
                print("✅ Sobrepeso.")
            if calculo >= 35 and calculo < 40:
                print("✅ Obesidade grau 1.")
            if calculo >=40:
                print("✅ Obesidade grau 2.")

    except ValueError:
        print("❌ Por favor, insira valores numéricos válidos.\n")
        continue

    opcao = input("\nDeseja verificar novamente? (s/n): ").strip().lower()
    
    match opcao:
        case "s":
            continue
        case "n":
            print("Programa finalizado. Obrigado por usar o programa!")
            break
        case _:
            print("Opção inválida. Encerrando o programa.")
            break
