import math

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return math.pi*self.r**2
    
    def circumference(self):
        return 2*math.pi*self.r
    
    def length(self):
        return 2*math.pi*self.r
    
r = 3
circle = Circle(r)

print(f"Pole: {circle.area():.2f}")
print(f"Długość okręgu: {circle.length():.2f}")
print(f"Obwód koła: {circle.circumference():.2f}")