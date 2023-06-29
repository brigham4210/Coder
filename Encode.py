def encode(s):
    s = str(s)
    o = ""
    for c in s:
        
        if c =="a":
            c = "✡"
        elif c == "b":
            c = "♪"
        elif c == "c":
            c = "ϟ"
        elif c == "d":
            c = "δ"
        elif c == "e":
            c = "⚘"
        elif c == "f":
            c = "φ"
        elif c == "g":
            c = "γ"
        elif c == "h":
            c = "η"
        elif c == "i":
            c = "ι"
        elif c == "j":
            c = "⚸"
        elif c == "k":
            c = "♕"
        elif c == "l":
            c = "λ"
        elif c == "m":
            c = "μ"
        elif c == "n":
            c = "ν"
        elif c == "o":
            c = "卍"
        elif c == "p":
            c = "π"
        elif c == "q":
            c = "ϙ"
        elif c == "r":
            c = "ρ"
        elif c == "s":
            c = "σ"
        elif c == "t":
            c = "☣"
        elif c == "u":
            c = "υ"
        elif c == "v":
            c = "ϋ"
        elif c == "w":
            c = "ω"
        elif c == "x":
            c = "ξ"
        elif c == "y":
            c = "ψ"
        elif c == "z":
            c = "ζ"
        elif c == " ":
            c = "⚭"
        
        o += c

    return o

print(encode("I am a boss."))
