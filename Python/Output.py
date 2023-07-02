from kivy.uix.label import Label


output_box = Label(
    text="What do you want to say?",
    font_size=30,
    color='#00FFCE',
    size_hint=(0.9, 0.2),
    pos_hint={"center_x": 0.5, "y": 0.5}
)
