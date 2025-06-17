import math as m

#exibe o numero do pi
print(f'Numero do PI: "{m.pi}"')

#raiz quadrada
try:
    n = int(input(f"informe o numero inteiro: "))
    int(input(f"A raiz quadrada de {n} é {m.sqrt(n)}."))
except Exception as e:
            print(f"não foi possivel calcular. {e}.")        
             