import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def function_name1(self, e): # se è invocata da un bottone, bisogna mettere e
        if txt_in1 == "" or txt_in1 is None: # verifiche sulla correttezza dell'input 1
            self._view.create_alert(f"Attenzione, inserire un valore!!!")
            self._view.update_alert()
            return

        try:
            txt_in_int1 = int(txt_in1)
        except:
            self._view.create_alert(f"Attenzione, inserire un valore intero!!!")
            self._view.update_alert()
            return

        # operazioni della funzione 1

        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi:{}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{}"))
        self._view.update_page()

    def function_name2(self, e):
        # verifiche sulla correttezza dell'input 2
        # operazioni della funzione 2

    def fill_DD(self, myValues):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.istanza1, on_click=self.read_DD_value), myValues)) # map cicla su myValues e applica la funzione lambda
        self._view._ddLun.options = myValuesDD

    def read_DD_value(self, e): # salva tutto l'oggetto in un'istanza di self
        self.dd_value = e.control.data