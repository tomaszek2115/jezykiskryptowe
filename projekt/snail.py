# Biblioteka PIL umozliwia tworzenie rysunkow

import datetime
from PIL import Image, ImageDraw

# Klasa snail

class Snail:

    # Konstruktor obiektu

    def __init__(self, n):
        self.n = n # Atrybut n
        self.segment_length = 50 # Jednostka dlugosci n
        self.eye_radius = 5
        self.anthenas_radius = 2 + self.n
        self.image = Image.new("RGB", (250 + n * 150, 250 + n * 150), "white") # Utworzenie rysunku
        self.draw = ImageDraw.Draw(self.image) # Metoda rysujaca
        self.position_x = (50 + self.n * 50) # Aktualna pozycja "rysowania"
        self.position_y = (50 + self.n * 50)

    # Metoda rysujaca muszle
    
    def drawShell(self):
        prev_x = self.position_x # Zmienne pozycji poczatkowej linii
        prev_y = self.position_y 
        next_x = prev_x # Zmienne pozycji koncowej linii
        next_y = prev_y
        for _ in range(self.n): # Petla rysujaca muszle
            next_x += self.segment_length # Do koncowej wspolrzednej x dodajemy dlugosc segmentu
            self.draw.line([prev_x, prev_y, next_x, prev_y], fill = "black", width = 3) # Rysowanie linii
            prev_x = next_x # Aktualizacja wspolrzednej x
            next_y -= self.segment_length # Aktualizacja wspolrzednej y
            self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3) # Rysowanie linii
            self.segment_length += 50
            next_x -= self.segment_length
            prev_y = next_y
            self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
            prev_x = next_x
            next_y += self.segment_length
            self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
            prev_y = next_y
            self.segment_length += 50
        next_x += self.segment_length - 50
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        prev_x = next_x
        self.position_x = prev_x
        self.position_y = prev_y

    # Metoda rysujaca glowe 
    
    def drawHead(self):
        prev_x = self.position_x
        prev_y = self.position_y
        next_x = prev_x + self.segment_length / 2
        next_y = prev_y
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        prev_x = next_x
        next_y -= 50
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        prev_y = next_y
        next_x -= self.segment_length / 2
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        self.position_x = prev_x
        self.position_y = prev_y

    # Metoda rysujaca oczy
        
    def drawEyes(self):
        center_x = self.position_x - self.segment_length / 6
        center_y = self.position_y + 50 / 3
        self.draw.ellipse((center_x - self.eye_radius, center_y - self.eye_radius, center_x + self.eye_radius, center_y + self.eye_radius), outline="black", width=3)
        center_x -= self.segment_length / 6
        self.draw.ellipse((center_x - self.eye_radius, center_y - self.eye_radius, center_x + self.eye_radius, center_y + self.eye_radius), outline="black", width=3)

    def drawAnthenas(self):
        prev_x = self.position_x - self.segment_length / 6
        prev_y = self.position_y
        next_x = prev_x
        next_y = prev_y - ((self.segment_length - 100) / 2)
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        next_y -= self.anthenas_radius
        self.draw.ellipse((next_x - self.anthenas_radius, next_y - self.anthenas_radius, next_x + self.anthenas_radius, next_y + self.anthenas_radius), outline="black", width=3)
        prev_x -= self.segment_length / 6
        next_y += self.anthenas_radius
        next_x = prev_x
        self.draw.line([prev_x, prev_y, next_x, next_y], fill = "black", width = 3)
        next_y -= self.anthenas_radius
        self.draw.ellipse((next_x - self.anthenas_radius, next_y - self.anthenas_radius, next_x + self.anthenas_radius, next_y + self.anthenas_radius), outline="black", width=3)

    def drawSmile(self):
        center_x, center_y = self.position_x - self.segment_length / 4, self.position_y + 35
        for x in range(-int((self.segment_length / 12)), int(self.segment_length / 12)):
            a = 0.077222605 * (0.647478803 ** self.n)
            y = int(a * x ** 2)
            if y < 10:
                self.draw.point((center_x + x, center_y - y), fill = "black") 

    def drawSnail(self):
        self.drawShell()
        self.drawHead()
        self.drawEyes()
        self.drawSmile()
        self.drawAnthenas()
        timestamp = datetime.datetime.now().strftime("%Y%d%m%H%M%S")
        image_path = f"output/image_{timestamp}.png"
        self.image.save(image_path)
        image_path = f"backup/image_{timestamp}.png"
        self.image.save(image_path)
        image_path = f"image_{timestamp}.png"
        try:
            with open("image_names.txt", "a") as file:
                 file.write(image_path + '\n')
        except FileNotFoundError:
            print("error")
        except ValueError:
            print("error")
            n = None

try:
    with open("input.txt", "r") as file:
        lines = file.readlines()
        if lines:
            n = int(lines[-1])
        else:
            print("Error: File is empty")
            n = None
except FileNotFoundError:
    print("Error: FileNotFoundError")
except ValueError:
    print("Error: ValueError")
    n = None


if n is not None:
    snaily = Snail(n)
    snaily.drawSnail()