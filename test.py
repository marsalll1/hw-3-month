from datetime import date
import flet as ft

def main(page: ft.Page):
    page.title = "Приветствия"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []
    favorite_names = []

    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            greeting_history = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        greeting_history = []

    text_hello = ft.Text("Hello world")
    greeting_text = ft.Text("История приветствий:\n" + "\n".join(greeting_history))
    favorite_text = ft.Text("Любимые имена:")

    name_input = ft.TextField(label="Введите имя", expand=True)

    def save_history():
        with open("history.txt", "w", encoding="utf-8") as f:
            for name in greeting_history:
                f.write(name + "\n")

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            text_hello.value = f"Hello {name}"
            text_hello.color = None
            name_input.value = None

            greeting_history.append(name)
            greeting_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            save_history()
        else:
            text_hello.value = "Введите корректное имя"
            text_hello.color = ft.Colors.RED

        page.update()

    def add_to_favorites(_):
        if greeting_history:
            last_name = greeting_history[-1]
            if last_name not in favorite_names:
                favorite_names.append(last_name)
                favorite_text.value = "Любимые имена:\n" + "\n".join(favorite_names)
                page.update()

    def clear_history(_):
        greeting_history.clear()
        greeting_text.value = "История приветствий:"
        save_history()
        page.update()

    send_button = ft.ElevatedButton("SEND", on_click=on_button_click)
    fav_button = ft.ElevatedButton("Добавить в избранное", on_click=add_to_favorites)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    page.add(
        ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, send_button, clear_button]),
        greeting_text,
        fav_button,
        favorite_text
    )

ft.app(target=main)
