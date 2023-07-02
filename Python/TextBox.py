from kivy.uix.textinput import TextInput


textBox = TextInput(
    multiline=True,
    padding_y=(20, 20),
    size_hint=(0.9, 0.2),
    pos_hint={"center_x": 0.5, "center_y": 0.4}
)
