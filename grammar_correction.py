import flet as ft


def main(page: ft.Page):
    page.title = "Grammar Correction App"
    page.horizontal_alignment = "center"  # type: ignore
    page.theme_mode = "light"  # type: ignore
    page.window_max_width = 700
    page.window_max_height = 600
    page.window_width = 700
    page.window_height = 600
    # page.window_frameless = True

    logo = ft.Image("assets/logo.png", width=300)
    user_input = ft.TextField(
        hint_text="Enter any sentence here...",
        width=500,
        border_radius=30,
    )
    output_text = ft.Text("your response will be generated here...")

    output_container = ft.Container(
        content=output_text, margin=20, padding=20, bgcolor="#f2f2f2", border_radius=30
    )

    page.add(
        logo,
        user_input,
        ft.ElevatedButton("submit", on_click=print_result),
        output_container,
    )


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
