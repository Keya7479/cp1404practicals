"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class MilesKmConverterApp(App):
    """MilesKmConverterApp is a Kivy App for squaring a number."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_kms.kv')
        return self.root

    def handle_increment(self, text, increment):
        """Increment miles number."""
        miles = increment + convert_to_number(text)
        self.root.ids.input_number.text = str(miles)

    def handle_conversion(self, text):
        """Handle conversion of miles to kms."""
        miles = convert_to_number(text)
        self.root.ids.output_label.text = str(miles * CONVERSION_FACTOR)


def convert_to_number(text):
    """Convert text to a float, return 0 as default for invalid text."""
    try:
        return float(text)
    except ValueError:
        return 0.0


MilesKmConverterApp().run()
