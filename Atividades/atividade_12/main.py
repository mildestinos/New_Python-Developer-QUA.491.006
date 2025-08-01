'''
# TODO - atividade: criar um programa que calcule a área e a
circunferência de um circulo


'''
import os


limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')  

calcular_area = lambda r: 3.14 * (r ** 2)
calcular_circunferencia = lambda r: 2 * 3.14 * r

raio = float(input('Informe o raio do círculo: '))
area = calcular_area(raio)
circunferencia = calcular_circunferencia(raio)
#limpar 
limpar()
print(f'A área do círculo é: {area:.2f}')
print(f'A circunferência do círculo é: {circunferencia:.2f}')







