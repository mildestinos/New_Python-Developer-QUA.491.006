#importar módulo

import modulo as m


#algoritimo princial
if __name__ == "__main__":
    while True:
        print("1 - Calcular Quadrado.")
        print("2 - Calcular Retangulo.")
        print("3 - Calcular triangulo.")
        print("4 - Sair do programa.")  
        opcao = input("Escolha uma opção: ").strip()     
        m.limpar_tela()
        
        match opcao:
            case "1":
                try:
                    lado = int(input("Informe o lado quadrado: "))
                    a = m.area_quadrado(lado)
                    print(f"A área do quadrado é: {a}")
                except Exception as e:  
                    print(f"Erro: {e}")
                finally:
                    continue                    

                
            case "2":
                try:
                    base = int(input("Informe a base do retângulo: "))
                    altura = int(input("Informe a altura do retângulo: "))
                    a = m.area_retangulo(base, altura)
                    print(f"A área do retângulo é: {a}")
                except Exception as e:  
                    print(f"Erro: {e}")
                finally:
                    continue

             
            case "3":
                try:
                    base = int(input("Informe a base do triângulo: "))
                    altura = int(input("Informe a altura do triângulo: "))
                    a = m.area_triangulo(base, altura)
                    print(f"A área do triângulo é: {a}")                    

                except Exception as e:  
                    print(f"Erro: {e}")
                finally:
                    continue                 
            case "4":
                print("programa encerrado.")
                break

            case _:
                print("Opção inválida. Tente novamente.")
