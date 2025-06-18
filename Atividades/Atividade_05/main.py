import datetime
import os

# Recebe nome e idade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n--- Filmes em cartaz ---")
    print("1 - A Roda Quadrada (Livre)")
    print("2 - A Volta dos Que Não Foram (12 anos)")
    print("3 - Poeira em Alto Mar (14 anos)")
    print("4 - As Tranças do Rei Careca (16 anos)")
    print("5 - A Vingança do Peixe Frito (18 anos)")

    sala = int(input("Escolha o número da sala: "))

    # 👌Usa match para escolher o filme e a classificação
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
            print("Sala inválida. Tente novamente.")
            continue

    # Verifica se pode assistir
    if idade >= idade_minima:
        agora = datetime.datetime.now()
        print("\n🎫 Ingresso")
        print("--------------")
        print("Nome:", nome)
        print("Filme:", filme)
        print("Sala:", sala)
        print("Data:", agora.strftime("%d/%m/%Y"))
        print("Hora:", agora.strftime("%H:%M:%S"))
        print("Bom filme! 🍿")
        print("-------------------")
        break
    else:
        print("Você não tem idade suficiente para ver esse filme. Escolha outro.")
