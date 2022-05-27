

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

import json

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
    
    filename = 'myfile.json'

    def on_start(self): 
        self.read_data('firstelement')

    
    def on_stop(self):
        self.save_data()




    # kirjutab andmeid json faili, uuendab praeguse ajatelje nime
    def save_data(self):
        # print(self.root.ids.mytextinput.text)
        fhand = open(self.filename)
        data = json.load(fhand)
        event = self.root.ids.nimi.text
        print(self.currentevent)
        print(data)
        print(self.root.ids.varv.color)
        data[event] = data.pop(self.currentevent)

        data[event]['aasta'] = self.root.ids.aasta.text
        data[event]['ekr'] =  self.root.ids.ekr.active 
        data[event]['kuu'] = self.root.ids.kuu.text
        data[event]['paev'] = self.root.ids.paev.text
        data[event]['kirjeldus'] = self.root.ids.kirjeldus.text
        data[event]['varv'] = self.root.ids.varv.color
        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        self.currentevent = event


    # Loeb andmeid json failist
    def read_data(self, event):
        fhand = open(self.filename)
        data = json.load(fhand)
        if event == 'firstelement':
            for i in data:
                event = i
                break
        print(data)
        print(self.root.ids.varv.color)
        self.root.ids.nimi.text = event
        self.root.ids.aasta.text = data[event]['aasta']
        self.root.ids.ekr.active = data[event]['ekr']
        self.root.ids.kuu.text = data[event]['kuu']
        self.root.ids.paev.text = data[event]['paev']
        self.root.ids.kirjeldus.text = data[event]['kirjeldus']
        self.root.ids.varv.color = data[event]['varv']
        self.currentevent = event




if __name__ == '__main__':
    MyApp().run()