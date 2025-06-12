# Tratamento de exceção
try:
    n = int(input('Digite um número inteiro: '))
    print(f"Número informado: {n}.")
except ValueError:
    print("Ocorreu um erro: o valor informado não é um número inteiro.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("Programa encerrado com sucesso!😒.")
    