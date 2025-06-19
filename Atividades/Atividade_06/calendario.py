import pandas as pd

# Gera um intervalo de datas
inicio = "2025-01-01"
fim = "2025-12-31"
datas = pd(start=inicio, end=fim, freq='D')

# Cria a tabela de datas
tabela_datas = calendar.DataFrame({
    "Data": datas,
    "Ano": datas.year,
    "Mês": datas.month,
    "Nome_Mês": datas.strftime("%B"),       # Janeiro, Fevereiro, ...
    "Mês_Ano": datas.strftime("%m/%Y"),
    "Dia": datas.day,
    "Dia_Semana": datas.weekday + 1,        # 1 = Segunda, 7 = Domingo
    "Nome_Dia_Semana": datas.strftime("%A"),
    "Trimestre": datas.quarter,
    "É_Fim_de_Semana": datas.weekday >= 5   # Sábado (5) ou Domingo (6)
})

# Mostrar as primeiras linhas
print(tabela_datas.head())
