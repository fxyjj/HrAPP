import kivy
kivy.require('1.11.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.scrollview import ScrollView
from dbConn import *
from kivy.app import runTouchApp
from kivy.core.window import Window


class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # self.cols = 2
        text = 'username'
        self.add_widget(Label(text=text,size_hint=(.2,.2),pos_hint={'center_x': .1, 'center_y': .9}))
        self.username = TextInput(multiline=False,size_hint=(.1,.1),pos_hint={'center_x': .2, 'center_y': .9})
        self.add_widget(self.username)
        self.add_widget(Label(text='password',size_hint=(.2,.2),pos_hint={'center_x': .1, 'center_y': .7}))
        self.password = TextInput(password=True, multiline=False,size_hint=(.1,.1),pos_hint={'center_x': .2, 'center_y': .7})
        self.add_widget(self.password)
        # self.layout = GridLayout(cols=3,spacing=10,size_hint_y=None)
        # self.layout.bind(minimum_height=self.layout.setter('height'))
        # for i in range(0,len(data)):
        #     self.layout1 = GridLayout(cols=3,spacing=10,size_hint_y=None)
        #     self.layout1.add_widget(Label(text=data[i][0],size_hint=(.2,.2)))
        #     self.layout1.add_widget(Label(text=data[i][1],size_hint=(.2,.2)))
        #     self.layout1.add_widget(Label(text=data[i][2],size_hint=(.2,.2)))
        #
        #     print(data[i][0],data[i][1],data[i][2])
        #     self.layout.add_widget(self.layout1)
        # self.scroll = ScrollView(do_scroll_x=False,do_scroll_y=True,size_hint=(1,None),size=(5,5))
        # self.scroll.add_widget(self.layout)
        # self.add_widget(self.scroll)
        self.add_widget(scrollView.scroll(self))
        colum = GridLayout(cols=3, spacing=1,size_hint=(.3,.3),pos_hint={'center_x': .7, 'center_y': .9})
        colum.add_widget(Label(text='Name', size_hint=(.2, .2), pos_hint={'center_x': .7, 'center_y': .8}))
        colum.add_widget(Label(text='Station', size_hint=(.2, .2), pos_hint={'center_x': .8, 'center_y': .8}))
        colum.add_widget(Label(text='Depart', size_hint=(.2, .2), pos_hint={'center_x': .9, 'center_y': .8}))
        self.add_widget(colum)




class scrollView():
    def scroll(self):
        layout=GridLayout(cols=1,spacing=1,size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(0,len(data)):
            layout1 = GridLayout(cols=3,spacing=1,size_hint_y=None)
            layout1.add_widget(Label(text=data[i][0]))
            layout1.add_widget(Label(text=data[i][1]))
            layout1.add_widget(Label(text=data[i][2]))
            print(data[i][0],data[i][1],data[i][2])
            layout.add_widget(layout1)
        root = ScrollView(do_scroll_x=False,do_scroll_y=True,size_hint=(0.3,0.5),size=(500,800),pos_hint ={'center_x': .7, 'center_y': .6} )
        print(Window.width,Window.height)
        root.add_widget(layout)

        return root

class HrAPP(App):

    def build(self):

       return LoginScreen()


if __name__ == '__main__':
    # runTouchApp(scrollView().scroll())
    HrAPP().run()