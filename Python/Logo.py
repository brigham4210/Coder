from kivy.uix.image import Image


def logo():
    pic = Image(
        source="../Pics/logo.png"
    )
    pic.size_hint = (.2, .2)
    pic.pos_hint = {'center_x': .5, 'center_y': .8}

    return pic
