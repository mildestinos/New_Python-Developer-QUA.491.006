import modulo as mo

if __name__ == '__main__':
    while True:
        try:
            print('1 - Calculadora Fibonacci.')
            print('2 - Perguntar Adei.')
            
            opcao = input('Escolha uma opção: ').strip()

            match opcao:
                case '1':
                    n = int(input('Digite um número inteiro positivo: '))
                    print(f'O {n}º termo da sequência de Fibonacci é {mo.fibonacci(n)}')
                case '2':
                    print('Saindo do programa...')
                    break
                case _:
                    print('Opção inválida. Tente novamente.')
        except Exception as e:
            print(f'Erro: {e}')
