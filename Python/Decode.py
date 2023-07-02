from data import one, two


def decode(s):
    s = str(s)

    for key, value in two.items():
        s = s.replace(value, key)

    for key, value in one.items():
        s = s.replace(value, key)

    return s
