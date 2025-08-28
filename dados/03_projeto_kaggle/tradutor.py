import nbformat
from deep_translator import GoogleTranslator
import os

# Caminho do notebook original (relativo)
notebook_path = "03_projeto_kaggle/serial-murder-analysis.ipynb"

# Obter pasta do arquivo original
folder_path = os.path.dirname(notebook_path)

# Nome do arquivo traduzido
output_filename = "serial-murder-analysis-traduzido.ipynb"

# Caminho completo para salvar o arquivo traduzido na mesma pasta
output_path = os.path.join(folder_path, output_filename)

# Carregar notebook
nb = nbformat.read(open(notebook_path, encoding="utf-8"), as_version=4)

# Traduzir células markdown
for cell in nb.cells:
    if cell.cell_type == "markdown":
        try:
            cell.source = GoogleTranslator(source='en', target='pt').translate(cell.source)
        except Exception as e:
            print(f"Erro ao traduzir célula: {e}")

# Salvar notebook traduzido
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook traduzido salvo em: {output_path}")
