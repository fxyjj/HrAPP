import kivy
kivy.require('1.11.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.scrollview import ScrollView
from dbConn import *
from kivy.app import runTouchApp,stopTouchApp
from kivy.core.window import Window

cursor.execute("select * from PGMReq")

data = cursor.fetchall()

class scrollView():
    def scroll(self,data):
        layout=GridLayout(cols=1,spacing=1,size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'),minimum_width=layout.setter('width'))
        for i in range(0,len(data)):
            layout1 = GridLayout(cols=4,spacing=1,size_hint_y=None)
            layout1.add_widget(Label(text=data[i][0]))
            layout1.add_widget(Label(text=data[i][1]))
            layout1.add_widget(Label(text=data[i][2]))
            layout1.add_widget(Label(text=data[i][3]))
            # print(data[i][0],data[i][1],data[i][2])
            layout.add_widget(layout1)
        scrollpart = ScrollView(do_scroll_x=True,do_scroll_y=True )
        # print(Window.width,Window.height)
        colum = GridLayout(cols=4, spacing=1, size_hint=(.3, .3), pos_hint={'center_x': .1, 'center_y': .1})
        colum.add_widget(Label(text='Station', size_hint=(.2, .2), pos_hint={'center_x': .1, 'center_y': .1}))
        colum.add_widget(Label(text='Depart', size_hint=(.2, .2), pos_hint={'center_x': .1, 'center_y': .1}))
        colum.add_widget(Label(text='Program', size_hint=(.2, .2), pos_hint={'center_x': .1, 'center_y': .1}))
        colum.add_widget(Label(text='Req.', size_hint=(.2, .2), pos_hint={'center_x': .1, 'center_y': .1}))
        scrollpart.add_widget(layout)
        root = GridLayout(cols=1,size_hint=(0.8,0.8),size=(800,800),pos_hint ={'center_x': .65, 'center_y': .45})
        root.add_widget(colum)
        root.add_widget(scrollpart)
        return root

    def manuPage(self):
        layout=BoxLayout(orientation='vertical')
        layout.bind(minimum_height=layout.setter('height'))
        layout.add_widget(Button(text='课程-岗位',size=(20,10)))
        layout.add_widget(Button(text='test_btn2', size=(20, 10)))
        layout.add_widget(Button(text='test_btn3', size=(20, 10)))
        layout.add_widget(Button(text='test_btn4', size=(20, 10)))
        layout.add_widget(Button(text='test_btn5', size=(20, 10)))
        root = ScrollView(do_scroll_x=False,do_scroll_y=True,size_hint=(0.2,0.8),size=(80,800),pos_hint ={'center_x': .12, 'center_y': .45})
        root.add_widget(layout)
        return root


class header():
    def userInfor(self):
        return

    def operationBar(self):
        layout = FloatLayout(size=(800,800))
        station = Label(text='Station',size_hint=(.08,.05),pos_hint={'center_x':.25,'center_y':.8})
        def on_text(instance,value):
            print('the text: ',instance,'have ',value)
        stationInput = TextInput(multiline=False,size_hint=(.1,.05),pos_hint={'center_x':.35,'center_y':.8})
        stationInput.bind(text=on_text)
        depart = Label(text='Depart',size_hint=(.1,.1),pos_hint={'center_x':.45,'center_y':.8})
        departInput = TextInput(multiline=False,size_hint=(.1,.05),pos_hint={'center_x':.55,'center_y':.8})
        departInput.bind(text=on_text)
        program = Label(text='Program',size_hint=(.1,.05),pos_hint={'center_x':.65,'center_y':.8})
        programInput = TextInput(multiline=False,size_hint=(.1,.05),pos_hint={'center_x':.75,'center_y':.8})
        programInput.bind(text=on_text)
        find_btn = Button(text='查询',size_hint=(.1,.05),pos_hint={'center_x':.85,'center_y':.8})

        layout.add_widget(station)
        layout.add_widget(stationInput)
        layout.add_widget(depart)
        layout.add_widget(departInput)
        layout.add_widget(program)
        layout.add_widget(programInput)
        layout.add_widget(find_btn)

        return layout


