#! /usr/bin/ python3

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        pi = 3.14159
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        print(f"Circumference of a circle with a radius of {self.radius:3} is {myCircumference:.2f}")

#New Way
#List for my values
radius = [Circle(2),Circle(5),Circle(7)]

for r in radius:
    r.printCircumference()
