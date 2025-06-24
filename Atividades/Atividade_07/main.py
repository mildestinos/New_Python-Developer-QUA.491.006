"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa

# NOTE - a lista deve começar vazia. Exemplo: lista = []

"""
lista = []

while True:
    print("\n--- menu 🐍 ---")
    print("1 - Cadastre novo nome na lista")
    print("2 - Liste todos os nomes na lista")  
    print("3- Pesquise por um nome na lista")
    print("5- Altere um nome na lista")
    print("6- Exclua um nome na lista")
    print("0- Sair do programa")   

opcao = input("Escolha uma opção: ").strip

if opcao == "1":
        nome = input("Digite o nome para cadastrar: ").strip()
        lista.append(nome)
        print("Nome cadastrado com sucesso!")

if opcao == "2":
        print("nomes cadastraNomes ==nome = input("Digite o nome para cadastrar: ").strip()
        lista.append(nome)
        print("Nome cadastrado com sucesso!")







# Recebe nome
nome= input("Informe o nomer: ").title().strip()

# Recebe idade com validação
while True:
    try:
        nome = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("nome não existe.")

while True:
    # Menu
    os.system('cls' if os.name == 'nt' else 'clear')
 
   

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

