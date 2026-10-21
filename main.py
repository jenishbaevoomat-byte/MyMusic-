from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

Window.clearcolor = (0.07, 0.07, 0.07, 1)


class MusicApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=16, spacing=12)
        root.add_widget(Label(text="Home", font_size="26sp",
                              size_hint_y=None, height=60))
        grid = GridLayout(cols=2, spacing=12)
        for i in range(1, 7):
            grid.add_widget(Button(text=f"Album {i}",
                                   background_normal="",
                                   background_color=(0.2, 0.2, 0.25, 1)))
        root.add_widget(grid)
        return root


MusicApp().run()
