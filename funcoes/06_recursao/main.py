import modulo as mo

if __name__ == '__main__':
    while True:
        try:
            print('1 - Calculadora de Fatorial')
            print('2 - Sair do programa.')
            opcao = input('Escolha uma opção: ').strip()
            match opcao:
                case '1':
                    n = int(input('Digite um número inteiro positivo: '))
                    print(f'O fatorial de {n} é {mo.fatorial(n)}')
                case '2':
                    print('Saindo do programa...')
                    break
                case _:
                    print('Opção inválida. Tente novamente.')
                    continue
            
        except Exception as e:
            print(f'Erro: {e}.')
            continue