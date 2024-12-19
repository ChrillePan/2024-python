#! /usr/bin/ python3

#List for my values
radius_values = [2,5,7,9,11,13]

def circumference(radius_values):
  pi = 3.14159 
  circumferenceValue = pi * radius_values * 2
  return circumferenceValue

def printCircumference(radius_values):
  myCircumference = circumference(radius_values)
  print (f"Circumference of a circle with a radius of {radius_values:3} is {myCircumference:.2f}")

#New Way

for r in radius_values:
    printCircumference(r)
