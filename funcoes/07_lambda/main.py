import os

# função normal

#def somar(x,y):
    #result = x + y
    #return result


#usando lambda
somar = lambda x, y: x + y  # função lambda para somar dois números 
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # função lambda para limpar a tela

#algoritimo principal

if __name__ == "__main__":
    try:
        x = int(input("informe o valor de x: "))
        y = int(input("informe o valor de y: "))
        result = somar (x,y)
        
        limpar()
        print(f"A resultado da soma é: {result}.")
    except Exception as e:
        print(f"Não foi possível somar: {e}")  


        
