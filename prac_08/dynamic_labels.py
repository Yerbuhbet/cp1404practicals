from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        names = ["Yermukhamet Akbet", "Shafa", "Aruzhan", "Julia", "Bota", "Dastan"]
        main_layout = BoxLayout(orientation='vertical')

        for name in names:
            label = Label(text=name, font_size=20)
            main_layout.add_widget(label)

        return main_layout

if __name__ == '__main__':
    DynamicLabelsApp().run()
