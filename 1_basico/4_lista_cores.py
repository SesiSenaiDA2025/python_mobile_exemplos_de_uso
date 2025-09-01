import flet as ft

def main(page: ft.Page):
    page.title="Seletor de Cores"
    page.padding=20

    # Container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY,
        width=300,
        height=100,
        border_radius=10, #Bordas arredondadas
        alignment=ft.alignment.center #Centraliza o texto dentro da caixa
    )

    def cor_selecionada(evento):
        # Função que é executada sempre que o usuário
        # selecionar uma cor

        # Pegando qual foi a cor escolhida
        cor_escolhida = evento.control.value

        # Dicionário com as cores disponíveis
        cores_disponiveis = {
            "Azul":ft.Colors.BLUE,
            "Verde":ft.Colors.GREEN,
            "Vermelho":ft.Colors.RED,
            "Roxo":ft.Colors.PURPLE,
            "Laranja":ft.Colors.ORANGE,
            "Rosa":ft.Colors.PINK
        }

        # Mudando a cor da caixa
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida} ✨"

        page.update()

    # Criando uma lista suspensa (dropdown) com as cores
    seletor_cor = ft.Dropdown (
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        # Função será executada quando o usuário
        # escolher uma cor
        on_change=cor_selecionada
    )

    # Adicionando elementos à página
    page.add(
         ft.Text("Seletor de cores mágico! ✨", size=22, weight=ft.FontWeight.BOLD),
         seletor_cor,
         caixa_colorida
    )

ft.app(target=main)