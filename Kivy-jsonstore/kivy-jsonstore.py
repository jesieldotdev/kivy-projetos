from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore

kv = Builder.load_string("""
BoxLayout:
	Label:
		text: "Teste"
		id: lbl

""")

store = JsonStore('hello.json')

# put some values
store.put('tito', name='Mathieu', age=30)
store.put('tshirtman', name='Gabriel', age=27)
store.put('Ziel', name='Jesiel', age=21)

# get from a key
#print('tito is', store.get('tito'))

# or guess the key/entry for a part of the key
#key, tshirtman = store.find(name='Gabriel')
#print('tshirtman is', tshirtman)

for item in res:
    #print("Nome=", str(item))
    print('Nome: ', str(item[1]['name']))
    print("Idade: ", str(item[1]['age']))
    
class MyApp(App):
		def func(self):
			pass
			
		def mostrar(self):
			pass
		

		def build(self):
			return kv
		
		
MyApp().run()