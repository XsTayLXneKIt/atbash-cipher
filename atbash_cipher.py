def encode(plain_text):
    plain_text = plain_text.lower().replace(" ", "")
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            cipher_text += chr(ord("a") + (25 - (ord(char) - ord("a"))))
        elif char.isdigit():
            cipher_text += char
    return " ".join([cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)])

def decode(cipher_text):
    cipher_text = cipher_text.lower().replace(" ", "")
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            plain_text += chr(ord("a") + (25 - (ord(char) - ord("a"))))
        else:
            plain_text += char
    return plain_text