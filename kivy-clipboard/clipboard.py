from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""
#:import Clipboard kivy.core.clipboard.Clipboard
<MyGrid>:
    cols: 1
    BoxLayout:
        Button:
            text: 'Copy'
            on_release:
                Clipboard.copy(txtinput.text)
        Button:
            text: 'Paste'
            on_release:
                txtinput.text = Clipboard.paste()
    TextInput:
        id: txtinput
""")

class MyGrid(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()