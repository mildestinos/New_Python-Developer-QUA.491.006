'''
#TODO - Atividade: criar um programa que receba do usuário um numero inteiro e o programa cacular o valor da sequencia de fibonacci.
A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores.

Ela começa assim:
'''

def fibonacci(n):
    if n <= 0:  
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

