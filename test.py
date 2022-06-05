from cgitb import text
from msilib.schema import CheckBox
from tabnanny import check
from idna import check_initial_combiner
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
from kivy.uix.popup import Popup
import json


class MyGrid(Widget):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

    def lisanupp(self):
        if myappinstance.check_for_error() == True:
            return
        myappinstance.lisa_event_json_faili()
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
        kuupaevad = []
        evendinimed = []
        varvid = []
        fhand = open(MyApp.filename)
        data = json.load(fhand)
        for event in data:
            if event == 'template':
                continue
            evendinimi = event
            varv = data[event]['varv'][0], data[event]['varv'][1], data[event]['varv'][2], data[event]['varv'][3]            
            kuupaev = int(data[event]['aasta'] + data[event]['kuu'] + data[event]['paev'])
            kuupaevad.append(kuupaev)
            evendinimed.append(evendinimi)
            varvid.append(varv)
        fhand.close()
        kuupaevad = kuupaevad[:-1]
        evendinimed = evendinimed[:-1]
        varvid = varvid[:-1]
        vastavus = {}

        # Muudetud osa algab siit -----------------------------------------------------------------
        for i in range(0, len(kuupaevad)):
            vastavus[kuupaevad[i-1]] = [evendinimed[i-1], varvid[i-1]]
        pikkus = len(kuupaevad)
        kuupaevad = bubblesort(kuupaevad, pikkus)
        y = Window.height/4*1
        if len(kuupaevad) == 1:
            x = Window.width/2
            button = Button(text= '\n' + str(kuupaevad[0]) + '\n' + vastavus[kuupaevad[0]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[0]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=0: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)
        
        elif len(kuupaevad) == 2:
            x = Window.width/2 - Window.width/4
            button = Button(text= '\n' + str(kuupaevad[0]) + '\n' + vastavus[kuupaevad[0]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[0]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=0: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)

            x = Window.width/2 + Window.width/4
            button = Button(text= '\n' + str(kuupaevad[1]) + '\n' + vastavus[kuupaevad[1]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[1]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=1: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)

        elif len(kuupaevad) == 3:
            x = Window.width/2
            button = Button(text= '\n' + str(kuupaevad[0]) + '\n' + vastavus[kuupaevad[0]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[0]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=0: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)

            x = Window.width/2 + Window.width/5
            button = Button(text= '\n' + str(kuupaevad[1]) + '\n' + vastavus[kuupaevad[1]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[1]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=1: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)

            x = Window.width/2 - Window.width/5
            button = Button(text= '\n' + str(kuupaevad[2]) + '\n' + vastavus[kuupaevad[2]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[2]][1]) #the text on the button
            button.bind(on_press = lambda *args, i=2: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)
        

        else:
            for i in range(0, pikkus):
                x = (Window.width)/pikkus*(i) + 50
                button = Button(text= '\n' + str(kuupaevad[i]) + '\n' + vastavus[kuupaevad[i]][0], pos=(x, y), size=("20dp", "20dp"), background_color=vastavus[kuupaevad[i]][1]) #the text on the button
                button.bind(on_press = lambda *args, i=i: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
                self.ids.w_canvas.add_widget(button) #added to the grid
        
        # Muudetud osa lõppeb siit -----------------------------------------------------------------
        
    def on_buttonpress(self, eventname):
        if myappinstance.check_for_error() == True:
            return
        myappinstance.save_data()
        myappinstance.read_data(eventname)
    

class MyApp(App):
    def build(self):
        return MyGrid()

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        Window.bind(on_request_close=self.on_request_close)
        


    filename = 'myfile.json'

    # kui programm käivitub, seda koodi jooksutatakse
    def on_start(self): 
        self.read_data('lastevent')
    
    # checkib, et kuupäevad on õiged ja evendi nimed ei korduks
    # kui return False -> kõik korras
    # kui return True -> mingi jama, errori akna ette
    def check_for_error(self):
        evendid = []
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            if event == 'template' or event == myappinstance.currentevent:
                continue
            evendid.append(event)
        fhand.close()
        praeguneevent = self.root.ids.nimi.text
        if praeguneevent in evendid:
            popup = Popup(title='VIGA', content=Label(text='Sama nimega event on olemas juba'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return True
        if self.piira_kuupaevad() == 'VIGA':
            return True
        else:
            self.save_data()
            return False

        

    # kui programmi tahetakse kinni panna, siis checkib errorite jäoks
    # kui error on, siis ei lase kinni panna programmi
    def on_request_close(self, *largs, **kwargs):
        return self.check_for_error()

    # piirab kuude ja päevade sisestuse. Ei saa enam panna kuupäevade väljadessa tähti (nt: "200abcd") - siis viskab errori
    def piira_kuupaevad(self):
        lubatudpaevad = []
        lubatudkuud = []
        for num in range(1, 32):
            if num < 10:
                lubatudpaevad.append('0' + str(num))
                lubatudkuud.append('0' + str(num))
            elif num < 13:
                lubatudkuud.append(str(num))
                lubatudpaevad.append(str(num))
            elif num >= 11:
                lubatudpaevad.append(str(num))

        if self.root.ids.kuu.text not in lubatudkuud or self.root.ids.paev.text not in lubatudpaevad:
            popup = Popup(title='VIGA', content=Label(text='Kuu või päevaga on midagi valesti!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'

        try:
            int(self.root.ids.aasta.text)
            int(self.root.ids.kuu.text)
            int(self.root.ids.paev.text)
        except ValueError:
            popup = Popup(title='VIGA', content=Label(text='Kuskil kuupäevades on ka tähed!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'
        
        kuupaevad = []
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            if event == 'template' or event == myappinstance.currentevent:
                continue
            kuupaev = int(data[event]['aasta'] + data[event]['kuu'] + data[event]['paev'])
            kuupaevad.append(kuupaev)
        fhand.close()
        praeguseevendikuupaev = int(self.root.ids.aasta.text + self.root.ids.kuu.text + self.root.ids.paev.text)
        if praeguseevendikuupaev in kuupaevad:
            popup = Popup(title='VIGA', content=Label(text='Samal kuupäeval on juba mõni muu sündmus!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'




    # kustutab praeguse evendi
    def kustuta_event(self):
        evendid = []
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            evendid.append(event)
        if len(evendid) == 2:
            popup = Popup(title='VIGA', content=Label(text='See on su ainus sündmus, ära seda kustuta!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        data.pop(self.currentevent)
        fhand.close()
        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.read_data('lastevent')

    # lisab uue eventi
    # võtab myfile.jsonist kuupaevad(formaat aasta+kuu+päev nt 18840117) ja sordib need bubblesort algoritmiga
    # Teised andmed nimi, kirjeldus jne võiksid olla listis, mille sees on dictionaryd või teised listid, leppime tunnis kokku
    def lisa_event_json_faili(self):
        evendiloend = []
        kuupaevad = []
        self.save_data()
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            evendiloend.append(event)
            kuupaev = int(data[event]['aasta'] + data[event]['kuu'] + data[event]['paev'])
            kuupaevad.append(kuupaev)
        event = 'uusevent' + str(len(evendiloend))
        data[event] = data['template']
        fhand.close()

        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        fhand.close()
        
        self.read_data(event)


    # kirjutab andmeid json faili, uuendab praeguse ajatelje nime
    def save_data(self):
        fhand = open(self.filename)
        data = json.load(fhand)
        event = App.get_running_app().root.ids.nimi.text
        data[event] = data.pop(self.currentevent)
        data[event]['aasta'] = self.root.ids.aasta.text
        data[event]['ekr'] =  self.root.ids.ekr.active 
        data[event]['kuu'] = self.root.ids.kuu.text
        data[event]['paev'] = self.root.ids.paev.text
        data[event]['kirjeldus'] = self.root.ids.kirjeldus.text
        data[event]['varv'] = self.root.ids.varv.color
        fhand = open(self.filename, 'w')
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
        self.root.ids.nimi.text = event
        self.root.ids.aasta.text = data[event]['aasta']
        self.root.ids.ekr.active = data[event]['ekr']
        self.root.ids.kuu.text = data[event]['kuu']
        self.root.ids.paev.text = data[event]['paev']
        self.root.ids.kirjeldus.text = data[event]['kirjeldus']
        self.root.ids.varv.color = data[event]['varv']
        self.currentevent = event


if __name__ == '__main__':
    myappinstance=MyApp()
    myappinstance.run()