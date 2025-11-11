"""
GUI program that has a list of names (strings)
and dynamically creates a separate Label for each one.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

BACKGROUND_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app dynamically creates labels for names"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Button(text=name)
            temp_label.background_color = BACKGROUND_COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
