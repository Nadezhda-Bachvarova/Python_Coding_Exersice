class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.pi * (self.radius ** 2)
        return round (area, 2)

    def get_circumference(self):
        circumf = 2 * Circle.pi * self.radius
        return circumf


# Test Code:

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())


# Expected Output:

# 452.16
# 75.36

