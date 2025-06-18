"""
# TODO crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo
# NOTE - para interroper o programa, use  a teclada de atalho control-c

"""

import time
import os

while True:
    # Pega a hora atual
        os.system('cls' if os.name == 'nt' else 'clear')

        # Formata no estilo brasileiro
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)
