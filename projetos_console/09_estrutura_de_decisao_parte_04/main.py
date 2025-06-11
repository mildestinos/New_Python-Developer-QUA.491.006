# declaração de variáveis
Aluno = input("Informe seu nome: ")
Idade = int(input("Informe sua idade: "))

# ternário
result = "é maior de idade." if Idade >=18 else " é menor de idade."

#Saída
print(f"{Aluno} {result}")
