# dynamic_labels.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        return BoxLayout(orientation='vertical')

if __name__ == '__main__':
    DynamicLabelsApp().run()
