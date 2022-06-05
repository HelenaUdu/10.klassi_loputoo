from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
import json

# Widget - User interface building block, see mis kuvatakse
class MyGrid(Widget):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

    # paneb sündmused nuppudena ajatelje peale
    def update(self, showlast):
        self.children[0].children[0].clear_widgets() # kustutab telje pealt nupud ära

        # võtab myfile.jsonist kuupaevad(formaat aasta+kuu+päev nt 18840117) ja sordib need bubblesort algoritmiga
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
            ekr = data[event]['ekr']
            if ekr == True:
                kuupaev = -abs(kuupaev) 
            kuupaevad.append(kuupaev)
            evendinimed.append(evendinimi)
            varvid.append(varv)
        fhand.close()

        # lisanupp() funktsioon lisab nupu json faili lõppu, seega selle funktsiooni puhul ei ole vaja viimaseid vaadata
        if showlast == 'dontshowlast': # lisanupp() funktsioon lisab nupu json faili lõppu, seega selle funktsiooni puhul ei ole vaja viimaseid vaadata
            kuupaevad = kuupaevad[:-1]
            evendinimed = evendinimed[:-1]
            varvid = varvid[:-1]
        vastavus = {} # kuupäevale vastav evendi nimi ja selle värv
        for i in range(0, len(kuupaevad)):
            vastavus[kuupaevad[i]] = [evendinimed[i], varvid[i]]
            
        pikkus = len(kuupaevad)
        kuupaevad = bubblesort(kuupaevad, pikkus)
        y = Window.height/28*8
        x = 30
        # lisab nupud
        for i in range(0, pikkus):
            if kuupaevad[i] < 0:
                button = Button(text= f'\n\n{str(kuupaevad[i])[-2:]}/{str(kuupaevad[i])[-4:-2]}/{str(kuupaevad[i])[1:-4]}  eKr\n {vastavus[kuupaevad[i]][0]}',
                pos=(x, y), size=(20, 20), 
                background_color=vastavus[kuupaevad[i]][1])
            else:
                button = Button(text= f'\n\n{str(kuupaevad[i])[-2:]}/{str(kuupaevad[i])[-4:-2]}/{str(kuupaevad[i])[:-4]}  \n {vastavus[kuupaevad[i]][0]}', 
                pos=(x, y), size=(20, 20), 
                background_color=vastavus[kuupaevad[i]][1]) 
            x = Window.width/pikkus*(i+1)
            button.bind(on_press = lambda *args, i=i: self.on_buttonpress(vastavus[kuupaevad[i]][0]))
            self.ids.w_canvas.add_widget(button)
        
    def kustutanupp(self):
        myappinstance.kustuta_event_json_failist()
        self.update('showlast')

    # funktsioon mis käivitub, kui vajutad nuppu "Lisa"
    def lisanupp(self):
        # vaatab kas on teiste sündmustega on kooskõlas(ei ole sama nimega või sama kuupäevaga jne)
        if myappinstance.check_for_error() == True:
            return 
        myappinstance.lisa_event_json_faili() # funktsiooni nimi ütleb ära
        self.update('dontshowlast') # uuendab ajatelge 

    # käivitub, kui vajutada telje peal olevaid nuppe
    def on_buttonpress(self, eventname):
        if myappinstance.check_for_error() == True:
            return
        myappinstance.save_data()
        myappinstance.read_data(eventname) 
        self.update('showlast')
    

# jooksutab kogu programmi
class MyApp(App):
    # ehitab user interfacei
    def build(self):
        return MyGrid()

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        # programmi sulgedes tahtes käivitub on_request_close() funktsioon
        Window.bind(on_request_close=self.on_request_close) 
        
    filename = 'myfile.json' # json faili nimi

    # kui programm käivitub, siis seda koodi jooksutatakse esimesena
    def on_start(self): 
        self.read_data('lastevent')

    # kirjutab andmed json faili
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

    # loeb andmeid json failist, kuvab need üleval
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
    
    # checkib, et kuupäevad on õiged, kuupäevad ei kordu ja evendi nimed ei kordu
    # kui return False -> kõik korras
    # kui return True -> mingi jama, viskab errori akna ette
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
            popup = Popup(title='VIGA', content=Label(text='Sama nimega event on juba olemas!\nMuuda praeguse sündmuse kuupäev ära!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return True
        if self.piira_kuupaevad() == 'VIGA':
            return True
        else:
            self.save_data()
            return False

    # kui programmi tahetakse kinni panna, siis kas on erroreid
    # kui error on, siis ei lase programmi kinni panna
    def on_request_close(self, *largs, **kwargs):
        return self.check_for_error()

    # piirab kuude ja päevade sisestuse. Ei saa enam panna kuupäevade väljadessa tähti (nt: "200abcd") 
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
            popup = Popup(title='VIGA', content=Label(text='Kuu või päevaga on midagi valesti!\nKuu vahemikus 01-12, Päev vahekmikus 01-31'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'

        try:
            int(self.root.ids.aasta.text)
            int(self.root.ids.kuu.text)
            int(self.root.ids.paev.text)
        except ValueError:
            popup = Popup(title='VIGA', content=Label(text='Kuskil kuupäevades on tähed või Aasta lünk on tühi!\nVeateatest lahti saamiseks tee see korda!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'
        
        kuupaevad = []
        fhand = open(self.filename)
        data = json.load(fhand)

        for event in data:
            if event == 'template' or event == myappinstance.currentevent:
                continue
            kuupaev = int(data[event]['aasta'] + data[event]['kuu'] + data[event]['paev'])
            ekr = data[event]['ekr']
            if ekr == True:
                kuupaev = -abs(kuupaev)     
            kuupaevad.append(kuupaev)
        fhand.close()

        praeguseevendikuupaev = int(self.root.ids.aasta.text + self.root.ids.kuu.text + self.root.ids.paev.text)
        
        if self.root.ids.ekr.active == True and praeguseevendikuupaev > 0:
            praeguseevendikuupaev = -abs(praeguseevendikuupaev)
        if praeguseevendikuupaev in kuupaevad:
            popup = Popup(title='VIGA', content=Label(text='Samal kuupäeval on juba mõni muu sündmus!\nVeateatest lahti saamaiseks pead muutma\npraeguse sündmuse kuupäeva!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return 'VIGA'

    def kustuta_event_json_failist(self):
        evendid = []
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            evendid.append(event)
        if len(evendid) == 2:
            popup = Popup(title='VIGA', content=Label(text='See on su ainus sündmus, seda ei saa kusutada!'), size_hint=(None, None), size=(400, 400))
            popup.open()
            return
        data.pop(self.currentevent)
        fhand.close()
        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.read_data('lastevent')

    def lisa_event_json_faili(self):
        evendiloend = []
        self.save_data()
        fhand = open(self.filename)
        data = json.load(fhand)
        for event in data:
            evendiloend.append(event)
        event = 'uusevent' + str(len(evendiloend))
        if event in evendiloend:
            event = event + '(2nd)'
        data[event] = data['template']
        fhand.close()
        fhand = open(self.filename, 'w')
        json.dump(data, fhand, indent=2)
        fhand.close()
        self.read_data(event)


if __name__ == '__main__':
    myappinstance=MyApp()
    myappinstance.run()
