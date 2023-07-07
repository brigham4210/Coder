from Python.Data import one, two
from Python.OutputBox import output_box
from Python.TextBox import textBox
from kivy.uix.button import Button


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
