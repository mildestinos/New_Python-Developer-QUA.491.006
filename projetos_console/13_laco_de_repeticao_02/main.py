while True:
    print(f"{'-'*20} MENU {'-'*20}")
    print("0 - Encerrar o programa")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir") 
    operador = input("Informe a operação desejada: ")

    match operador:
        case "0":
            print("Programa encerrado")
            break

        case "1":
            try:
                x = float(input("Informe o valor de x: ").replace(",", "."))
                y = float(input("Informe o valor de y: ").replace(",", "."))
                print(f"{x} + {y} = {x + y}")
            except Exception as e:
                print(f"Não foi possível somar. {e}.")
            finally:
                continue

        case "2":
            try:
                x = float(input("Informe o valor de x: ").replace(",", "."))
                y = float(input("Informe o valor de y: ").replace(",", "."))
                print(f"{x} - {y} = {x - y}")
            except Exception as e:
                print(f"Não foi possível subtrair. {e}.")
            finally:
                continue

        case "3":
            try:
                x = float(input("Informe o valor de x: ").replace(",", "."))
                y = float(input("Informe o valor de y: ").replace(",", "."))
                print(f"{x} * {y} = {x * y}")
            except Exception as e:
                print(f"Não foi possível multiplicar. {e}.")
            finally:
                continue

        case "4":
            try:
                x = float(input("Informe o valor de x: ").replace(",", "."))
                y = float(input("Informe o valor de y: ").replace(",", "."))
                print(f"{x} / {y} = {x/y}")
            except Exception as e:
                print(f"Não foi possível dividir. {e}.")
            finally:
                continue

        case _:
            print("Operação inválida. ")
