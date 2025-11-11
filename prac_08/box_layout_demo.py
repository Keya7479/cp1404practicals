"""
Prac 08
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - greeting Kivy app """

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handler for pressing greet button"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_all(self):
        """Clear input_name and output_text"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
