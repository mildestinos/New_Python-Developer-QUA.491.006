# declaração de variáveis
Aluno = input("Informe o nome do aluno: ")
Media = float(input("Informe a média do aluno: ").replace(",", "."))

# estrutura de decisão
if 0 <= Media <= 10:
    if Media >= 7:
        print(f"{Aluno} está aprovado.")
    elif Media >= 5:
        print(f"{Aluno} está em recuperação.")
    else:
        print(f"{Aluno} está reprovado.")
else:
    print("Nota inválida.")
