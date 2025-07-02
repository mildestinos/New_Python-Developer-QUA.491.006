#importações

import os

#entrada de dado

while True:
    # usuário informa o nome do arquivo
    arquivo = input("informe  o nome do arquivo:").strip().lower()

    #abre o arquivo

    with open (f"{arquivo}.txt","r",encoding="utf-8") as f:
        arquivo_aberto = f.read()
        os.system("cls" if os.name == "nt" else "clear")

#mostrar  os dados dos arquivos
print(aruivo_aberto)






