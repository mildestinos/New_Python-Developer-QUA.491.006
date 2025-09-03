import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro app flet"
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Row([
                    ft.Text("Ola mundo flet python!!!🐍"),
                    ft.Text("😋💀➡️🐍"),
                ])
            ),
            expand=True,
        )
    )

ft.app(main)
