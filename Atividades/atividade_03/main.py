import os
import math

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=== MENU ===")
    print("1 - Calcular área do círculo")
    print("2 - Calcular circunferência")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        raio = float(input("Digite o raio do círculo: "))
        area = math.pi * raio ** 2
        print(f"A área do círculo é: {area:.2f}")
    elif escolha == "2":
        raio = float(input("Digite o raio do círculo: "))
        circunferencia = 2 * math.pi * raio
        print(f"A circunferência é: {circunferencia:.2f}")
    elif escolha == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")

    input("\nPressione Enter para continuar...")
