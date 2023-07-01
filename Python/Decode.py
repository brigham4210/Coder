import data


def decode(s):
    s = str(s)

    for key, value in data.two.items():
        s = s.replace(value, key)

    for key, value in data.one.items():
        s = s.replace(value, key)

    return s
