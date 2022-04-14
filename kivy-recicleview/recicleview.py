from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

from kivy.core.window import Window
from kivy.utils import platform
if platform == 'win':
    Window.size = 300, 600

Builder.load_string('''
<RV>:
    viewclass: 'MDRaisedButton'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        padding: [20,20]
        spacing: 20
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': f'Item {str(x)}'} for x in range(100)]


class TestApp(MDApp):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()