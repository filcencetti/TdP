import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def function_name1(self, e):
        if txt_in1 == "" or txt_in1 is None:
            self._view.create_alert(f"Attenzione, inserire un valore!!!")
            self._view.update_page()
            return

        try:
            txt_in_int1 = int(txt_in1)
        except:
            self._view.create_alert(f"Attenzione, inserire un valore intero!!!")
            self._view.update_page()
            return

        # ordinare un dizionario in base ai valori
        dic = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi:{}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{}"))
        self._view.update_page()


    def fill_DD(self, myValues):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.istanza1, on_click=self.read_DD_value), myValues))
        self._view._dd.options = myValuesDD

    def read_DD_value(self, e):
        self._view._dd.value = e.control.data