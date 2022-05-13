
from cgitb import text
from msilib.schema import CheckBox
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.stacklayout import StackLayout


class MyGrid(Widget):
    """
    nimi = ObjectProperty(None)
    kirjeldus = ObjectProperty(None)
    aasta = ObjectProperty(None)
    kuu = ObjectProperty(None)
    paev = ObjectProperty(None)

    def lisanupp(self):
        pass
"""

class Telg(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()