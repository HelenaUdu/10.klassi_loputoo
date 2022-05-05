
# lihtsalt vaatan kas saan siit teha midagi

from cgitb import text
from msilib.schema import CheckBox
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

list = []

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
# Päeva sisestamise koht
        self.add_widget(Label(text="Päev"))
        self.paev = TextInput(multiline=False)
        self.add_widget(self.paev)
# Kuu sisestamise koht
        self.add_widget(Label(text="Kuu"))
        self.kuu = TextInput(multiline=False)
        self.add_widget(self.kuu)
# Aasta sisestamise koht
        self.add_widget(Label(text="Aasta"))
        self.aasta = TextInput(multiline=False)
        self.add_widget(self.aasta)
# Nimi sisestamise koht
        self.add_widget(Label(text="Nimi"))
        self.nimi = TextInput(multiline=False)
        self.add_widget(self.nimi)
# Kirjeldus sisestamise koht
        self.add_widget(Label(text="Kirjeldus"))
        self.kirjeldus = TextInput()
        self.add_widget(self.kirjeldus)
#EMA checkbox

# Värvi valiku koht

# Lisa nupp
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

        




class TheLabApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    TheLabApp().run()


