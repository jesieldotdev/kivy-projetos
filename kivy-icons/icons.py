from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.core.window import Window

from kivy.utils import platform
if platform == 'win':
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


<PreviousMDIcons>


    MDBoxLayout:
        orientation: 'vertical'


        MDBoxLayout:
            adaptive_height: True

            

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

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


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()

    def mostrar_nome(self, nome):
        toast(f'{nome.text} copy to clipboard')


MainApp().run()