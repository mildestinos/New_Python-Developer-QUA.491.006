import os


while True:
    try:
        novo_texto = input("digite o texto:\n")
        nome_arquivo = input("informe o nome do arquivo (sem extensão): ").strip().lower()  
        with open (f"44_manipular_arquivos_03/{nome_arquivo}.txt", "w",encoding="utf-8") as f:
            f.write(novo_texto)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_arquivo}.txt gravado com sucesso.")

        while True:
            prosseguir = input("Deseja gravar novo arquivo? (s/n): ").strip().lower()
            if  prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("opção invalida.")

                continue

        match prosseguir:
            case "s":
                continue
            case "n":
                break
            
    except Exception as e:
        print(f"Não foi possível gravar arquivo.{e}.")