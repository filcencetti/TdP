import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = page_title
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        # title
        self._title = ft.Text(page_title, color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self._textfield = ft.TextField(label= text_field_name )
        self._btn = ft.ElevatedButton(text= button_txt,
                                              on_click=self._controller.controller_function_name1) # funzione senza parentesi
        row1 = ft.Row([
            ft.Container(None, width=250),
            ft.Container(self._textfield, width=250),
            ft.Container(self._btn, width=250)
        ], alignment=ft.MainAxisAlignment.CENTER)

        #ROW2
        self._dd = ft.Dropdown(label= dropdown_name )
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        row2 = ft.Row([
            ft.Container(None, width=250),
            ft.Container(self._dd, width=250),
            ft.Container(self.txt_result, width=250)
        ], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2) # == self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
