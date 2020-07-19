import kivy
kivy.require('1.11.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.scrollview import ScrollView
from dbConn import *
from kivy.app import runTouchApp
from kivy.core.window import Window

layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))  # ******必须指定..................
print(layout.setter('height'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)
