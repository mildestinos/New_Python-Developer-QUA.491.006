from deep_translator import GoogleTranslator
import os

# Função para limpar a tela
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")

    while True:
        try:
           
            print("1 - Traduzir texto para Português")
            print("2 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            match opcao:
                case "1":
                    texto = input("Digite o texto para traduzir: ")
                    traducao = tradutor.translate(texto)
                    print(f"\nTradução: {traducao}\n")
                    input("Pressione Enter para continuar...")

                case "2":
                    print("Saindo...")
                    break

                case _:
                    print("Opção inválida!")
                    input("Pressione Enter para tentar novamente...")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
