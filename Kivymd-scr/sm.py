from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file("sm.kv")

# Declare both screens
class MenuScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class TestApp(MDApp):
	
	def chamada(self):
	   sm = ScreenManager()
	   sm.switch_to(MDScreen(title="menu"))

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        
        # Create the screen manager
        sm = ScreenManager()
 
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
       

        return sm
    

if __name__ == '__main__':
    TestApp().run()