
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
from kivy.graphics import Line, Color, Rectangle
from kivy.core.window import Window

class MyGrid(Widget):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, mode='rgb')
            print(self.height)
        with self.canvas:
            self.line = Line(points=(0, Window.height/4, Window.width, Window.height/4))
        with self.canvas.after:
            pass
    """
    nimi = ObjectProperty(None)
    kirjeldus = ObjectProperty(None)
    aasta = ObjectProperty(None)
    kuu = ObjectProperty(None)
    paev = ObjectProperty(None)

    def lisanupp(self):
        pass
    """

class Telg():
    pass


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()