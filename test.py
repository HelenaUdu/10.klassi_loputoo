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
from kivy.graphics import Line, Color
from kivy.core.window import Window
import json

import json

class MyGrid(Widget):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
    
    def piira_kuupaev(self):
        pass
        self.input_filter = 'int'
    
    def pressed(self, instance):
            print("pressed")

    def lisanupp(self):
        # Paneme pärast need lisanupp ja lisa_event kokku
        # võtab myfile.jsonist kuupaevad(formaat aasta+kuu+päev nt 18840117) ja sordib need bubblesort algoritmiga
        # Teised andmed nimi, kirjeldus jne võiksid olla listis, mille sees on dictionaryd või teised listid, leppime tunnis kokku
        self.children[0].children[0].clear_widgets()
        def bubblesort(järjend, pikkus):
            for i in range(pikkus):
                for j in range(pikkus -1):
                    if järjend[j] > järjend[j+1]:
                        järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
            return järjend
        kuupaevad = [18840117, 20050111, 20200409]
        nimi = "Tere"
        pikkus = len(kuupaevad)
        kuupaevad = bubblesort(kuupaevad, pikkus)
        y = Window.height/28*8
        x = 30
        for i in range(0, pikkus):
            
            button = Button(text=str(kuupaevad[i-1]), pos=(x, y), size=(20, 20)) #the text on the button
            x = Window.width/pikkus*(i+1)
            self.ids.w_canvas.add_widget(button) #added to the grid
        

class MyApp(App):
    def build(self):
        return MyGrid()
    
    filename = 'myfile.json'
    n = 1 

    def on_start(self): 
        self.read_data('lastevent')

    
    def on_stop(self):
        self.save_data()

    # kustutab praeguse evendi
    def kustuta_event(self):
        fhand = open(self.filename)
        data = json.load(fhand)
        data.pop(self.currentevent)
        fhand.close()
        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.read_data('lastevent')

    # lisab uue eventi
    def lisa_event(self):
        self.save_data()
        fhand = open(self.filename)
        data = json.load(fhand)
        event = 'template' + str(self.n)
        self.n += 1
        data[event] = data['template']
        fhand.close()
        fhand = open(self.filename, 'w')
        print(data)
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.read_data(event)


    # kirjutab andmeid json faili, uuendab praeguse ajatelje nime
    def save_data(self):
        fhand = open(self.filename)
        data = json.load(fhand)
        event = self.root.ids.nimi.text
        # print(self.currentevent)
        # print(data)
        # print(self.root.ids.varv.color)

        data[event] = data.pop(self.currentevent)

        data[event]['aasta'] = self.root.ids.aasta.text
        data[event]['ekr'] =  self.root.ids.ekr.active 
        data[event]['kuu'] = self.root.ids.kuu.text
        data[event]['paev'] = self.root.ids.paev.text
        data[event]['kirjeldus'] = self.root.ids.kirjeldus.text
        data[event]['varv'] = self.root.ids.varv.color
        # print(data)
        fhand = open(self.filename, 'w')
        # print(data)
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.currentevent = event



    # Loeb andmeid json failist
    def read_data(self, event):
        fhand = open(self.filename)
        data = json.load(fhand)
        if event == 'lastevent':
            for i in data:
                event = i

        # print(data)

        # print(self.root.ids.varv.color)
        self.root.ids.nimi.text = event
        self.root.ids.aasta.text = data[event]['aasta']
        self.root.ids.ekr.active = data[event]['ekr']
        self.root.ids.kuu.text = data[event]['kuu']
        self.root.ids.paev.text = data[event]['paev']
        self.root.ids.kirjeldus.text = data[event]['kirjeldus']
        self.root.ids.varv.color = data[event]['varv']
        self.currentevent = event
        # print(self.currentevent)


if __name__ == '__main__':
    MyApp().run()