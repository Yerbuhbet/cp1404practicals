from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        names = ["Yermukhamet Akbet", "Shafa", "Aruzhan", "Julia", "Bota", "Dastan"]
        main_layout = BoxLayout(orientation='vertical')

        for name in names:
            self.create_label(name, main_layout)

        return main_layout

    def create_label(self, name, layout):
        label = Label(text=name, font_size=20)
        layout.add_widget(label)

if __name__ == '__main__':
    DynamicLabelsApp().run()
