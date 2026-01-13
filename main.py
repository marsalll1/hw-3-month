# pip install flet[all]
import flet as ft 

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    greeting_text = ft.Text('История приветствий:')

    text_hello = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = None

            greeting_history.append(name)
            greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED

    def delete_last(_):
        if greeting_history:
            greeting_history.pop()
            if greeting_history:
                greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
            else:
                greeting_text.value = 'История пуста!'
        else:
            greeting_text.value = 'История пуста!'

    elevated_button = ft.ElevatedButton(
        'SEND',
        icon=ft.Icons.SEND,
        on_click=on_button_click
    )

    delete_last_button = ft.ElevatedButton(
        'Удалить последнее',
        icon=ft.Icons.REMOVE,
        on_click=delete_last
    )

    name_input = ft.TextField(
        label='Введите имя',
        on_submit=on_button_click,
        expand=True
    )

    main_object = ft.Row([
        name_input,
        elevated_button,
        delete_last_button
    ])

    text_row = ft.Row(
        [text_hello],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(text_row, main_object, greeting_text)

ft.app(target=main)
