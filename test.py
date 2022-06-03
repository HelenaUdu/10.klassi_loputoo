"""
[] restrictida textinput väljad(numbrid vahemikus 1-12 kuul, päevadel 1-31, aastal number)




"""







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
        self.input_filter = 'int'

    def lisanupp(self):
        # Paneme pärast need lisanupp ja lisa_event kokku
        # võtab myfile.jsonist kuupaevad(formaat aasta+kuu+päev nt 18840117) ja sordib need bubblesort algoritmiga
        # Teised andmed nimi, kirjeldus jne võiksid olla listis, mille sees on dictionaryd või teised listid, leppime tunnis kokku
        def bubblesort(järjend, pikkus):
            for i in range(pikkus):
                for j in range(pikkus -1):
                    if järjend[j] > järjend[j+1]:
                        järjend[j], järjend[j+1] = järjend[j+1], järjend[j]
            return järjend
        kuupaevad = [18840117, 20050111, 20200409]
        pikkus = len(kuupaevad)
        bubblesort(kuupaevad, pikkus)
        n = 1 # mitmes event on ajateljel
        for i in kuupaevad:
            x = self.left/pikkus*n
            y = self.center_y/2*3
            button = Button(pos =(x, y), size =(30, 30)) # Praegu on size suvakas ja buttonite variablei jaoks tuleb mingi nimetamis süsteem välja mõelda
            # self.ids[sõnastik[nimi]] = button
            n += 1
            


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
        MyGrid().lisanupp()


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