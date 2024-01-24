class Reverse:
    def __init__(self, list):
        self.list = list

    def reverse(self):
        words = self.list.split()
        revWor = words[::-1]
        result = ' '.join(revWor)
        return result

text = "Jestem studentem. Jestem studentem."
result = Reverse(text).reverse()

print(f"Tekst wejściowy: {text}")
print(f"Tekst odwrócony: {result}")