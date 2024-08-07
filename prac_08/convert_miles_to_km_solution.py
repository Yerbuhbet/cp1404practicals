"""
Estimated time: 45 minutes
Actual time: 40 minutes
Pseudocode:
MILES_TO_KM = 1.60934
class MilesConverterApp(App)
    function build(self)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    function handle_calculate(self)
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    function handle_increment(self, change)
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    function get_valid_input(self)
        try
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError
            return 0
"""

from kivy.app import App, Builder

__author__ = 'Lindsay Ward'
__changes_by__ = 'Yerbuhbet'

MILES_TO_KM = 1.60934 # Conversion factor for miles to kilometers.


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km_solution.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        value = self.get_validated_miles() + change # Increment or decrement the input miles value.
        self.root.ids.input_miles.text = str(value) # Update the input miles field
        self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
