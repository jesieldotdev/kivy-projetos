from kivymd.app import MDApp
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivymd.uix.label import MDLabel

kv = Builder.load_file("platform.kv")

class Tela(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	device = f'Você esta em um dispositivo {platform}'
		
		
		
	def on_start(self):
		pass
		#self.ids.add_widget(MDLabel(text='teste'))

class MyApp(MDApp):
		def build(self):
			return Tela()
			data = [{text: "MDFLATBUTTON",}]
			
			for key, values in data:
				print(key, values)
			self.ids.container.add_widget(MDLabel(text= 'j'))
		#self.root.ids.add_widget(button)
			
		def callback_1(self):
			toast()
		
		def callback_2(self):
			toast('menu')
			
		
			
		
		
		
MyApp().run()
