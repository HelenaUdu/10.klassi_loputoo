
# lihtsalt vaatan kas saan siit teha midagi

from cgitb import text
from msilib.schema import CheckBox
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

list = []

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        """super(MyGrid, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 2
        self.row_force_default = True
        self.row_default_height = 40
        self.width = 20

        # Päeva sisestamise koht
        self.add_widget(Label(text="Päev", size_hint_y = None))
        self.paev = TextInput(multiline=False)
        self.add_widget(self.paev)

        # Kuu sisestamise koht
        self.add_widget(Label(text="Kuu", size_hint_y = None))
        self.kuu = TextInput(multiline=False)
        self.add_widget(self.kuu)

        # Aasta sisestamise koht
        self.add_widget(Label(text="Aasta", size_hint_y = None))
        self.aasta = TextInput(multiline=False)
        self.add_widget(self.aasta)

        # Nimi sisestamise koht
        self.add_widget(Label(text="Nimi", size_hint_x = None))
        self.nimi = TextInput(multiline=False)
        self.add_widget(self.nimi)

        # Kirjeldus sisestamise koht
        self.add_widget(Label(text="Kirjeldus", size_hint_x = None))
        self.kirjeldus = TextInput()
        self.add_widget(self.kirjeldus)"""


#EMA checkbox

# Värvi valiku koht

# Lisa nupp
"""
        self.lisa = Button(text="Lisa", font_size=32)
        self.lisa.bind(on_press=self.press()) 
        self.add_widget(self.lisa)


# Mõtle see osa välja    
    def press(self, instance):
        nimi = self.nimi.text
        kirjeldus = self.kirjeldus.text
        paev = self.paev.text
        kuu = self.kuu.text
        aasta = self.aasta.text

"""        


class MyApp(App):

    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()


