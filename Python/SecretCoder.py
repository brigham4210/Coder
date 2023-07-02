from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from Logo import logo
from Output import output_box


class SecretCoder(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.body = FloatLayout()
        self.logo = logo()
        self.intro = output_box()

    def build(self):
        self.body.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.body.add_widget(self.logo)
        self.body.add_widget(self.intro)

        return self.body


# run Class
if __name__ == "__main__":
    SecretCoder().run()
