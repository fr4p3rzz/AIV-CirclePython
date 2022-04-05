import numpy as np
import matplotlib.pyplot as plt
import uuid

figure, axes = plt.subplots()
axes.set_aspect(1)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Computed circles')

class Circle:
    def __init__(self, is_radius, value):
        self._id = str(uuid.uuid4())

        if is_radius:
            self._radius = value
            self._diameter = value * 2
        else:
            self._radius = value / 2
            self._diameter = value 

        print(f"Created circle with ID: {self._id} and radius: {self._radius}.")

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(True, self._radius + other._radius)
    
    def __lt__(self, other):
        return self._radius < other._radius
    
    def __eq__(self, other):
        return self._radius == other._radius
    
    def __gt__(self, other):
        return self._radius > other._radius
    
    def area(self):
        return np.pi * (self._radius ** 2)

    def show_circle(self):
        theta = np.linspace(0, 2*np.pi, 100)
        a = self._radius*np.cos(theta)
        b = self._radius*np.sin(theta)
        axes.plot(a, b)

    def compare_dimension(self, other):
        if self > other:
            return f"Circle {self._id} is bigger than circle {other._id}."
        elif self == other:
            return f"Circles are equal"
        else:
            return f"Circle {self._id} is smaller than circle {other._id}."


C = Circle(True, 5)
B = Circle(True, 8)
A = B + C 
area = C.area()
print(area)
C.compare_dimension(B)
B.compare_dimension(A)

C.show_circle()
B.show_circle()

plt.show()