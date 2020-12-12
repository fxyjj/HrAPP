from test import *
from kivy.uix.splitter import Splitter
from kivy.config import Config
from kivy.core.window import Window
from kivy.animation import Animation
import cProfile
from kivy.uix.screenmanager import ScreenManager, Screen
Config.set('graphics','resizable',1)
Window.size=(400,200)


status = 0

class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        login_btn = Button(text='登陆',font_size=36,size=(20,10),size_hint=(.2, .2), pos_hint={'center_x': .5, 'center_y': .3})

        def gotoNextPage(instance):
            print('jack <%s>' % instance.text)
            print('username: %s' % self.username.text)
            print('password: %s' % self.password.text)
            cursor.execute("select password from user_infor where username = %s",self.username.text)
            data = cursor.fetchall()
            if len(data) == 0 :
                print('no such username,please type in right username')
            else:
                if len(data) != 0 and data[0][0] != self.password.text:
                    print(data[0],self.password.text)
                    print('wrong password!')
                else:
                    status = 1
                    mainPage.gotoNext(self)

        login_btn.bind(on_press=gotoNextPage)
        self.add_widget(login_btn)
        self.add_widget(Label(text='username', size_hint=(.2, .2), pos_hint={'center_x': .3, 'center_y': .7}))
        self.username = TextInput(multiline=False, size_hint=(.3, .13), pos_hint={'center_x': .55, 'center_y': .7})
        self.add_widget(self.username)
        self.add_widget(Label(text='password', size_hint=(.2, .2), pos_hint={'center_x': .3, 'center_y': .55}))
        self.password = TextInput(password=True, multiline=False, size_hint=(.3, .13),
                                  pos_hint={'center_x': .55, 'center_y': .55})
        self.add_widget(self.password)

class mainPage(AnchorLayout):
    def __init__(self, **kwargs):
        super(mainPage, self).__init__(**kwargs)
        self.add_widget(LoginScreen())
    def gotoNext(self):
        self.clear_widgets()
        Window.size = (1200, 800)
        # anim = Animation(x=50)
        # lab = Label(text='this is second page')
        # anim.start(lab)
        # self.add_widget(lab)

        self.add_widget(scrollView.manuPage(self))
        headpage = header.operationBar(self)
        # splitter = Splitter(sizable_from='top')
        # splitter.add_widget(headpage)
        # splitter.min_size = 100
        # splitter.max_size = 250
        self.add_widget(headpage)
        self.add_widget(scrollView.scroll(self, data))
        # print(headpage.children[0].text)
        # print(headpage.children[1].text)
        # print(headpage.children[2].text)
        # print(headpage.children[3].text)
        # print(headpage.children[4].text)
        # print(headpage.children[5].text)



        def getData(instance):
                cursor.execute(
                    "select * from PGMReq where Station like '%%%s%%' and Depart like '%%%s%%' and Program like '%%%s%%'" % (
                    headpage.children[5].text, headpage.children[3].text, headpage.children[1].text))

                data = cursor.fetchall()
                print(data)
                self.remove_widget(self.children[0])
                self.add_widget(scrollView.scroll(self, data))
            # return page
            # print('2')
            # return 2

        headpage.children[0].bind(on_press=getData)
        # self.add_widget(scroll)
class login(App):
    def build(self):
        self.icon = ''
        return mainPage()
login().run()