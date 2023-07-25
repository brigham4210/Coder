from kivy.uix.image import Image


class Logo(Image):
    def __init__(self, image, **kwargs):
        super(Logo, self).__init__(**kwargs)
        self.source = image
        self.size_hint = (.15, .15)
        self.pos_hint = {'center_x': .5, 'center_y': .8}