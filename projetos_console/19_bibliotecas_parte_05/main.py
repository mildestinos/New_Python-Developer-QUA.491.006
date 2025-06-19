import datetime
from datetime import date
hora = datetime.datetime.now().strftime("%H:%M:%S")
hoje = date.today().strftime("%d/%m/%Y")
print(f"Data da execução: {hoje}.")
print(f"Hora da execução: {hora}.")

  