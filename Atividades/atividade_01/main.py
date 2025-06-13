# TODO ATIVIDADE

'''
ODO - atividade:
Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário qual o melhor combustível para abastecer.
#NOTE - o usuário poderá informar várias vezes os valores, e irá encerrar o programa quando desejar.
#NOTE - cálculo: compensa etanol caso ele tenha até 70% do valor da gasolina.
#NOTE - DIVIRTAM-SE!!!! =D

'''
while True:
    try:
        etanol = float(input("Informe o valor do etanol R$: ").replace(',', '.'))
        gasolina = float(input("Informe o valor da gasolina R$: ").replace(',', '.'))
        calculo = (etanol / gasolina) * 100

        print(f"\nResultado: {calculo:.2f}% de etanol em relação à gasolina.")
        
        if calculo <= 70:
            print("✅ Compensa abastecer com **etanol**.")
        else:
            print("✅ Compensa abastecer com **gasolina**.")

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
