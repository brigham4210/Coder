from kivy.uix.label import Label
from kivy.uix.button import Button


def output_box():

    text = Label(
        text="What do you want to say?",
        font_size=30,
        color='#00FFCE'
    )
    text.size_hint = (0.9, 0.2)
    text.pos_hint = {"center_x": 0.5, "y": 0.5}
    copy_button = Button(
        text="copy",
        size_hint=(0.1, 0.1),
        background_color='#00FFCE'
    )

    return text
