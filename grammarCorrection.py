import flet as ft


def main(page: ft.Page):
    page.title = "Grammar Correction App"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_max_width = 700


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
