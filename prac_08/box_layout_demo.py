"""
Pseudocode:
class BoxLayoutDemo(App)
    function build(self)
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    function handle_greet(self)
        self.root.ids.output_label.text = display self.root.ids.input_name.text

    function clear_text(self)
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_text(self):
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
