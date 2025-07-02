try:
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(f"Texto Gravado:\n{texto}")

    novo_texto = input ("Digite o novo texto:\n")
    nova_gravacao = f"{texto}\n{novo_texto}"    

    with open (f"{arquivo}.txt","w",encoding="utf-8") as f:
        f.write(nova_gravacao)
    print("Gravação feira com sucesso.")

    with open (f"{arquivo}.txt","r",encoding="utf-8") as f:
        texto_final = f.read()

    print(f"Texto final: {texto_final}")
except Exception as e:
    print(f"não foi possível atualizar o conteúdo: {e}")