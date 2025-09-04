import flet as ft
from dataclasses import dataclass

# Classe Pessoa
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):
    # Propriedades da página
    page.title = "Dados do Usuário"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    nome_input = ft.TextField(label="Nome")
    idade_input = ft.TextField(label="Idade", suffix_text="anos")
    peso_input = ft.TextField(label="Peso", suffix_text="kg")
    salario_input = ft.TextField(label="Salário", prefix_text="R$")
    email_input = ft.TextField(label="E-mail")

    # Textos de saída
    saida_titulo = ft.Text(weight="bold")
    Nome = ft.Text()
    Idade = ft.Text()
    Peso = ft.Text()
    Salario = ft.Text()
    Email = ft.Text()

    # Função do botão
    def mostrar_dados(e):
        try:
            pessoa = Pessoa(
                nome=nome_input.value,
                idade=int(idade_input.value),
                peso=float(peso_input.value),
                salario=float(salario_input.value),
                email=email_input.value
            )

            saida_titulo.value = "Dados do usuário:"
            Nome.value = f"Nome: {pessoa.nome}"
            Idade.value = f"Idade: {pessoa.idade} anos"
            Peso.value = f"Peso: {pessoa.peso:.2f} kg"
            Salario.value = f"Salário: R$ {pessoa.salario:.2f}"
            Email.value = f"E-mail: {pessoa.email}"

            page.update()
        except ValueError:
            saida_titulo.value = "Erro: Verifique os campos numéricos!"
            Nome.value = Idade.value = Peso.value = Salario.value = Email.value = ""
            page.update()

    # Layout da página
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do Usuário", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        nome_input,
        idade_input,
        peso_input,
        salario_input,
        email_input,
        ft.ElevatedButton("Enviar", on_click=mostrar_dados),
        saida_titulo,
        Nome,
        Idade,
        Peso,
        Salario,
        Email,
    )

ft.app(main)
