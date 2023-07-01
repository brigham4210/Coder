import data


def encode(s):
    s = str(s)

    for key, value in data.two.items():
        s = s.replace(key, value)

    for key, value in data.one.items():
        s = s.replace(key, value)

    return s
