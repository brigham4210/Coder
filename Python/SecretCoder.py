from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from Logo import logo
from Output import output_box
from Copy import copy_button
from TextBox import textBox
from Encode import encode_button
from Decode import decode_button


class SecretCoder(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.body = FloatLayout()
        self.logo = logo
        self.intro = output_box
        self.copy = copy_button
        self.textBox = textBox
        self.encode = encode_button
        self.decode = decode_button

    def build(self):
        self.body.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.body.add_widget(self.logo)
        self.body.add_widget(self.intro)
        self.body.add_widget(self.copy)
        self.body.add_widget(self.textBox)
        self.body.add_widget(self.encode)
        self.body.add_widget(self.decode)

        return self.body


# run Class
if __name__ == "__main__":
    SecretCoder().run()
