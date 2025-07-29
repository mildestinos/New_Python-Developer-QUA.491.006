#funções
import os

def area_quadrado(l):
    a = 1**2 
    return a

def area_retangulo(b, h):
    a = b * h 
    return a    

def area_triangulo(b, h):
    a = (b * h) / 2
    return a

def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado
    os.system("cls" if os.name == "nt" else "clear")