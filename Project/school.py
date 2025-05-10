import turtle

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)

def colour():
    colour = turtle.color(input("Enter the colour yourself. "))
    return colour

def fill_colour():
    fill_colour = turtle.fillcolor(input("Enter the colour that u wanna fill. "))
    return fill_colour

def thick_ness():
    thic_kness = turtle.

color = colour()
fill_color = fill_colour()

shape = input("Enter choice of the shape, triangle or square: ")
if shape == "triangle":
    triangle()

elif shape == "square":
    square()




