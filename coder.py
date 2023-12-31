from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from Code.Logo import Logo
from Code.Copy import copy_button
from Code.TextBox import textBox
from Code.Encode import encode_button
from Code.Decode import decode_button
from Code.OutputBox import output_box


class Body(FloatLayout):
    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}


class SecretCoder(App):
    def __init__(self, image, **kwargs):
        super().__init__(**kwargs)
        self.body = Body()
        self.logo = Logo(image)
        self.intro = output_box
        self.copy = copy_button
        self.textBox = textBox
        self.encode = encode_button
        self.decode = decode_button

    def build(self):
        self.body.add_widget(self.logo)
        self.body.add_widget(self.intro)
        self.body.add_widget(self.copy)
        self.body.add_widget(self.textBox)
        self.body.add_widget(self.encode)
        self.body.add_widget(self.decode)

        return self.body


