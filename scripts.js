const encodingMap = {
    "one": {
        "a": "α", "b": "β", "c": "/", "d": "δ", "e": "ε", "f": "φ", "g": "γ", "h": "η", "i": "ι", "j": "=", "k": "κ",
        "l": "λ", "m": "μ", "n": "ν", "o": "ο", "p": "π", "q": "<", "r": "ρ", "s": "σ", "t": "τ", "u": "υ", "v": "ϋ",
        "w": "ω", "x": "ξ", "y": "ψ", "z": "ζ", " ": ":"
    },
    "two": { "th": "θ", "ae": "æ" }
};

function encode(s) {
    s = s.toLowerCase();
    for (const [key, value] of Object.entries(encodingMap.two)) {
        s = s.replaceAll(key, value);
    }
    for (const [key, value] of Object.entries(encodingMap.one)) {
        s = s.replaceAll(key, value);
    }
    return s;
}

function decode(s) {
    for (const [key, value] of Object.entries(encodingMap.two)) {
        s = s.replaceAll(value, key);
    }
    for (const [key, value] of Object.entries(encodingMap.one)) {
        s = s.replaceAll(value, key);
    }
    return s;
}

function encodeText() {
    let inputText = document.getElementById("text_to_encode").value.trim();
    if (inputText === "") return;
    let result = encode(inputText);
    displayResult(result);
}

function decodeText() {
    let inputText = document.getElementById("text_to_decode").value.trim();
    if (inputText === "") return;
    let result = decode(inputText);
    displayResult(result);
}

function displayResult(text) {
    document.getElementById("output").innerText = text;
    document.getElementById("result-container").style.display = "block";
}

function copyText() {
    let outputText = document.getElementById('output').innerText;
    navigator.clipboard.writeText(outputText).then(() => {
        let notification = document.getElementById('notification');
        notification.innerText = 'Copied to clipboard!';
        notification.style.display = 'block';

        setTimeout(() => {
            notification.style.display = 'none';
        }, 1500);
    });
}
