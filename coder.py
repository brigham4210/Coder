from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Body(FloatLayout):
    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}


data = {
    "one":
        {
            "a": "α",
            "b": "β",
            "c": "/",
            "d": "δ",
            "e": "ε",
            "f": "φ",
            "g": "γ",
            "h": "η",
            "i": "ι",
            "j": "=",
            "k": "κ",
            "l": "λ",
            "m": "μ",
            "n": "ν",
            "o": "ο",
            "p": "π",
            "q": "<",
            "r": "ρ",
            "s": "σ",
            "t": "τ",
            "u": "υ",
            "v": "ϋ",
            "w": "ω",
            "x": "ξ",
            "y": "ψ",
            "z": "ζ",
            " ": ":"
        },
    "two":
        {
            "th": "θ",
            "ae": "æ"
        }
}
one = data["one"]
two = data["two"]

output_box = Label(
    text="What do you want to say?",
    font_size=30,
    color='#00FFCE',
    size_hint=(0.9, 0.2),
    pos_hint={"center_x": 0.5, "y": 0.5}
)

textBox = TextInput(
    multiline=True,
    padding_y=(20, 20),
    size_hint=(0.9, 0.2),
    pos_hint={"center_x": 0.5, "center_y": 0.4}
)


class Logo(Image):
    def __init__(self, image, **kwargs):
        super(Logo, self).__init__(**kwargs)
        self.source = image
        self.size_hint = (.15, .15)
        self.pos_hint = {'center_x': .5, 'center_y': .8}


def copy(instance):
    Clipboard.copy(output_box.text)


copy_button = Button(
    text="copy",
    size_hint=(0.2, 0.05),
    pos_hint={"center_x": 0.5, "y": 0.65},
    background_color='#00FFCE'
)

copy_button.bind(on_press=copy)


def encode(s):
    s = str(s)

    for key, value in two.items():
        s = s.replace(key, value)

    for key, value in one.items():
        s = s.replace(key, value)

    return s


def encode_text(instance):
    # encode label text
    output_box.text = encode(textBox.text)


encode_button = Button(
    text="Encode",
    size_hint=(0.45, 0.2),
    pos_hint={"x": 0.05, "y": 0.05},
    bold=True,
    background_color='#00FFCE'
)

encode_button.bind(on_press=encode_text)


def decode(s):
    s = str(s)

    for key, value in two.items():
        s = s.replace(value, key)

    for key, value in one.items():
        s = s.replace(value, key)

    return s


def decode_text(instance):
    # encode label text
    output_box.text = decode(textBox.text)


decode_button = Button(
    text="Decode",
    size_hint=(0.45, 0.2),
    pos_hint={"x": 0.5, "y": 0.05},
    bold=True,
    background_color='#00FFCE'
)

decode_button.bind(on_press=decode_text)


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


if __name__ == "__main__":
    SecretCoder("").run()
