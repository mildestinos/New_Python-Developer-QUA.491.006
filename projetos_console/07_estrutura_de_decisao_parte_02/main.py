# declaração de variáveis
nome = input("informe seu nome:")
idade = int(input("informe sua idade:"))
altura = float(input("informe sua altura em metros: ").replace(",", "."))

# Estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome}, está autorizado a entrar.")
else:
    print(f"{nome}, não foi autorizado a entrar.")
