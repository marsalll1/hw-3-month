import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "My first Flet app"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value="", size=20)

    def on_button_click(e):
        name = name_input.value.strip()
        current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            text_hello.value = f"{current_time} - Привет, {name}!"
            text_hello.color = ft.Colors.GREEN
        else:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED

        name_input.value = ""
        page.update()

    name_input = ft.TextField(
        label="Введите имя",
        on_submit=on_button_click
    )

    send_button = ft.ElevatedButton(
        text="SEND",
        icon=ft.Icons.SEND,
        on_click=on_button_click
    )

    page.add(text_hello, name_input, send_button)


ft.app(target=main)
