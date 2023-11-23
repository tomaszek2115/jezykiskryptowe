def ceasar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


print(ceasar_cipher("jade noca przez warszawe slucham edyty bartosiewicz warszawe", 1))
