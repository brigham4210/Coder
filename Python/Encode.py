from data import one, two


def encode(s):
    s = str(s)

    for key, value in two.items():
        s = s.replace(key, value)

    for key, value in one.items():
        s = s.replace(key, value)

    return s
