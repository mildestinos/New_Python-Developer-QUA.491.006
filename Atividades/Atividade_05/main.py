import datetime
import os

# Recebe nome
nome = input("Digite seu nome: ")

# Recebe idade com validação
while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Por favor, digite um número válido para a idade.")

while True:
    # Menu
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n--- Filmes em cartaz 🐍 ---")
    print("1 - A Roda Quadrada (Livre)")
    print("2 - A Volta dos Que Não Foram (12 anos)")
    print("3 - Poeira em Alto Mar (14 anos)")
    print("4 - As Tranças do Rei Careca (16 anos)")
    print("5 - A Vingança do Peixe Frito (18 anos)")

    # Escolha da sala com validação
    try:
        sala = int(input("Escolha o número da sala: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número de 1 a 5.")
        input("Pressione Enter para continuar...")
        continue

    # Usa match para definir o filme e idade mínima
    match sala:
        case 1:
            filme = "A Roda Quadrada"
            idade_minima = 0
        case 2:
            filme = "A Volta dos Que Não Foram"
            idade_minima = 12
        case 3:
            filme = "Poeira em Alto Mar"
            idade_minima = 14
        case 4:
            filme = "As Tranças do Rei Careca"
            idade_minima = 16
        case 5:
            filme = "A Vingança do Peixe Frito"
            idade_minima = 18
        case _:
            print("Sala inexistente. Favor escolher outra sala.")
            input("Pressione Enter para continuar...")
            continue

    # Verifica se a pessoa pode assistir
    if idade >= idade_minima:
        print(f"\n✅ Você pode ver o filme '{filme}'.")
        agora = datetime.datetime.now()
        print("\n🎫 Ingresso")
        print("--------------")
        print("Nome:", nome)
        print(f"Filme: {filme} - Idade mínima: {idade_minima}")
        print("Sala:", sala)
        print("Data:", agora.strftime("%d/%m/%Y"))
        print("Hora:", agora.strftime("%H:%M:%S"))
        print("Bom filme! 🍿")
        print("-------------------")
        break
    else:
        print(f"\n❌ {nome}, você **não tem idade para ver o filme** '{filme}'.")
        input("Pressione Enter para escolher outro filme...")
