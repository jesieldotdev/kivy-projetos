from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App, Builder

Builder.load_file("back.kv")

class Home(Screen):
    pass
class User(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class Test(App):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.previous_screen = "" 

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Test().run()