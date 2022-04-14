from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.core.window import Window

from kivy.utils import platform
if platform != 'android':
    Window.size = 300, 600

Builder.load_string(
    '''
#:import Clipboard kivy.core.clipboard.Clipboard
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>
    on_release: app.mostrar_nome(root)
    on_press: Clipboard.copy(root.text) #app.mostrar_nome(root)
    IconLeftWidget:
        icon: root.icon


<MinhaTela>


    MDBoxLayout:
        orientation: 'vertical'


        MDBoxLayout:
            adaptive_height: True

            

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Pesquisar'
                on_text: root.existe(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'


            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'


'''
)

names = ['Jesiel', 'Jheny', 'Geziele']


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class MinhaTela(Screen):

    def existe(self, text="", search=False):
        '''Constroi a lista'''

        def add_item(nome):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": 'linux',
                    "text": nome,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for nome in names:
            if search:
                if text in nome:
                    add_item(nome)
            else:
                add_item(nome)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = MinhaTela()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return self.screen

    def on_start(self):
        self.screen.existe()

    def mostrar_nome(self, nome):
        toast(f'{nome.text} copy to clipboard')


MainApp().run()