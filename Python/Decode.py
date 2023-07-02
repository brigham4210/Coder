from data import one, two
from Output import output_box
from TextBox import textBox
from kivy.uix.button import Button


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
