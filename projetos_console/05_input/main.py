# entrada de dados
nome = input('Informe seu nome: ')
Idade = int(input('Informe sua idade: '))
Altura = float(input('Informe sua altura em metros: ').replace(',', '.'))

# saída de dados
print(f'Seja bem-vindo ao curso de Python, {nome}!')
print(f'{nome}: {type(nome)}.')
print(f'Idade do usuário: {Idade}')
print(f'{Idade}: {type(Idade)}.')
print(f'{Altura}: {type(Altura)}')

