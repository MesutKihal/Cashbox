import flet as ft


def main(page: ft.Page):
    page.window_full_screen = True
    page.theme_mode = ft.ThemeMode.LIGHT
    entry = ft.TextField(label="Scan Qr Code to search", expand=9)
    
    header = ft.NavigationBar(
        selected_index = 0,
        destinations = [
            ft.NavigationBarDestination(label="Cash Regsiter", icon=ft.Icons.KEYBOARD_ROUNDED),
            ft.NavigationBarDestination(label="Inventory", icon=ft.Icons.INVENTORY),
            ft.NavigationBarDestination(label="Cashbox", icon=ft.Icons.ATTACH_MONEY_OUTLINED),
            ft.NavigationBarDestination(label="Settings", icon=ft.Icons.SETTINGS_OUTLINED),
        ]
    )
    body = ft.Container(
        content=ft.Row(
        controls = [
            entry,
            ft.Container(
                    content=ft.Icon(ft.Icons.SEARCH),
                    expand=1,
                )
        ]
    ))
    page.add(
    
        header,
        body
    )
    


ft.run(main)
