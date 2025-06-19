'''
# TODO - Atividade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calendario do ano informado pelo usuário.

#NOTE - qualquer anos depois de 1900
#NOTE - Usu a biblioteca 'caledar'

'''

import calendar

ano = 2025

# Gera o calendário completo como uma string
calendario_completo = calendar.calendar(ano)
print(calendario_completo)