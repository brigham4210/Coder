from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from Encode import encode
from Decode import decode


class Coder(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.intro = Label(
            text="What do you want to say?",
            font_size=30,
            color='#00FFCE'
        )
        self.window.add_widget(self.intro)

        # text input widget
        self.words = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.words)

        # encode button widget
        self.encode_button = Button(
            text="Encode",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        self.encode_button.bind(on_press=self.encode_text)
        self.window.add_widget(self.encode_button)

        # decode button widget
        self.decode_button = Button(
            text="Decode",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        self.decode_button.bind(on_press=self.encode_text)
        self.window.add_widget(self.decode_button)

        return self.window

    def encode_text(self, instance):
        # encode label text
        self.intro.text = encode(self.words.text)

    def decode_text(self, instance):
        # decode label text
        self.intro.text = decode(self.words.text)

# run Say Hello App Calss
if __name__ == "__main__":
    Coder().run()
