from flask import Flask, render_template, request

app = Flask(__name__)

data = {
    "one": {"a": "α", "b": "β", "c": "/", "d": "δ", "e": "ε", "f": "φ", "g": "γ", "h": "η", "i": "ι", "j": "=", "k": "κ",
            "l": "λ", "m": "μ", "n": "ν", "o": "ο", "p": "π", "q": "<", "r": "ρ", "s": "σ", "t": "τ", "u": "υ", "v": "ϋ",
            "w": "ω", "x": "ξ", "y": "ψ", "z": "ζ", " ": ":"},
    "two": {"th": "θ", "ae": "æ"}
}

one = data["one"]
two = data["two"]


def encode(s):
    s = str(s)
    for key, value in two.items():
        s = s.replace(key, value)
    for key, value in one.items():
        s = s.replace(key, value)
    return s


def decode(s):
    s = str(s)
    for key, value in two.items():
        s = s.replace(value, key)
    for key, value in one.items():
        s = s.replace(value, key)
    return s


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encode', methods=['POST'])
def encode_text():
    text_to_encode = request.form['text_to_encode']
    encoded_text = encode(text_to_encode)
    return render_template('index.html', output_text=encoded_text)


@app.route('/decode', methods=['POST'])
def decode_text():
    text_to_decode = request.form['text_to_decode']
    decoded_text = decode(text_to_decode)
    return render_template('index.html', output_text=decoded_text)


if __name__ == '__main__':
    app.run(debug=True)
