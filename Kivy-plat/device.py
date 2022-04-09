from kivymd.app import MDApp
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivymd.uix.screen import MDScreen

# Menu
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.



from kivy.utils import platform
if platform == 'win':
    Window.size = 300, 600



device_list =  {
	'item1' : {'codenome':'win', 'nome': 'Windows', 'icon': 'microsoft-windows'}, 
	'item2': {'codenome': 'android', 'nome': 'Android', 'icon': 'android'}, 
	'item3': {'codenome': 'linux', 'nome': 'Linux', 'icon': 'linux'},
	}

for key in device_list:
	nome = device_list[key].get("nome")
	codenome = device_list[key].get("codenome")
	icon = device_list[key].get("icon")
	# platform = 'linux'
	if platform == codenome:
		device = f'Você esta em um dispositivo {nome}'
		icone = icon
		print(type(icone))



kv = Builder.load_file("device.kv")

class Item(OneLineAvatarIconListItem):
	left_icon = StringProperty()
	right_text = StringProperty('')

# Declare both screens
class InicioScreen(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# self.ids.texto.text='Deu certo'
		self.ids.bt.icon= icone


class InfoScreen(MDScreen):
    pass

class Scr(ScreenManager):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Create the screen manager
		# sm = ScreenManager()
		self.add_widget(InicioScreen(name='inicio'))
		self.add_widget(InfoScreen(name='info'))
		self.transition=WipeTransition()



	

class MyApp(MDApp):

	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Blue"


			
		
		lista = {'nome':'Info', 'icon': 'information-outline'}, {'nome':'Sair', 'icon': 'exit-to-app'}
		menu_items = [{ "right_text": str(key.get('nome')) ,"left_icon": str(key.get('icon')),"viewclass": "Item" , "on_release": lambda x=(str(key.get('nome'))): self.menu_chamada(x),} for key in lista]
		self.menu = MDDropdownMenu(items=menu_items, width_mult=4)

		return Scr()

	

		
	# Menu da Direita
	def callback_2(self, button):
		self.menu.caller = button
		self.menu.open()
		# print('Callback2')
	

	# Botões do menu
	def menu_chamada(self, text_item):

		self.menu.dismiss()
		# Snackbar(text=text_item).open()
		if text_item == 'Sair':
			self.stop()

		if text_item == 'Info':
			# Scr().abrir()
			self.root.current = 'info'

	def voltar(self):
		self.root.current = 'inicio'

	# def on_start(self):
	# 	InicioScreen().ids.ico.icon = 'linux'

	def abrir(self):
		Snackbar(text=device).open()
	



if __name__ == '__main__':
    MyApp().run()