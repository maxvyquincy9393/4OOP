class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"

V1 = Vector(1,2)
V2 = Vector(3,4)
v3 = V1 + V2
print(v3)

