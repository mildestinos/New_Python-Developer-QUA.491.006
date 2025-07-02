try:
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print("\nConteúdo atual do arquivo:")
    print(texto)
    
    novo_texto = input("\nDigite o novo texto para substituir o conteúdo:\n")
    
    confirmar = input("Deseja realmente sobrescrever o arquivo? (s/n): ").strip().lower()
    if confirmar == 's':
        with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(novo_texto)
        print("Arquivo atualizado com sucesso!")
    else:
        print("Operação cancelada. Arquivo não foi alterado.")
        
except FileNotFoundError:
    print(f"Arquivo '{arquivo}.txt' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
