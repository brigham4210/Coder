from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

from Output import output_box


def copy(instance):
    Clipboard.copy(output_box.text)


copy_button = Button(
    text="copy",
    size_hint=(0.2, 0.05),
    pos_hint={"center_x": 0.5, "y": 0.65},
    background_color='#00FFCE'
)

copy_button.bind(on_press=copy)
