from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from Encode import encode
from Decode import decode


class Coder(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.body = GridLayout()
        self.foot = GridLayout()
        self.box = BoxLayout()
        self.copy_box = FloatLayout()
        # label widget
        self.intro = Label(
            text="What do you want to say?",
            font_size=30,
            color='#00FFCE'
        )
        # text input widget
        self.words = TextInput(
            multiline=True,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        # copy button widget
        self.copy_button = Button(
            text="copy",
            size_hint=(0.1, 0.1),
            background_color='#00FFCE'
        )
        # encode button widget
        self.encode_button = Button(
            text="Encode",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        # decode button widget
        self.decode_button = Button(
            text="Decode",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FFCE'
        )

    def build(self):
        # returns a window object with all it's widgets

        self.body.cols = 1
        self.body.size_hint = (0.6, 0.7)
        self.body.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.foot.cols = 2
        self.foot.size_hint = (0.6, 0.7)
        self.foot.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.body.add_widget(Image(source="Pics/logo.png"))

        # Box widget
        self.box.cols = 2
        self.box.add_widget(self.intro)
        self.copy_button.size_hint = (0.2, 0.5)
        self.copy_button.pos_hint = {"x": 0.8, "y": 0.25}
        self.copy_box.add_widget(self.copy_button)
        self.box.add_widget(self.copy_box)
        self.body.add_widget(self.box)

        self.body.add_widget(self.words)

        self.encode_button.bind(on_press=self.encode_text)
        self.foot.add_widget(self.encode_button)

        self.decode_button.bind(on_press=self.decode_text)
        self.foot.add_widget(self.decode_button)
        self.body.add_widget(self.foot)

        return self.body

    def encode_text(self, instance):
        # encode label text
        self.intro.text = encode(self.words.text)

    def decode_text(self, instance):
        # decode label text
        self.intro.text = decode(self.words.text)


# run Class
if __name__ == "__main__":
    Coder().run()
