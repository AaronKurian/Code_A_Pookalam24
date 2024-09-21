import turtle
from turtle import *
import math

# Initialize turtle object
s = turtle.Turtle()

# Display "Happy Onam!" message
speed(0)
penup()
goto(-700, 320)
pendown()
color("#d00000")
write("Happy Onam!", font=("Courier", 50, "bold italic"))
hideturtle()

# Display name and class
speed(0)
penup()
goto(350, -300)
pendown()
color("#03071e")
write("- Aaron Kurian Abraham", font=("Times New Roman", 20))
penup()
goto(350, -350)
pendown()
write("- CS3A", font=("Times New Roman", 20))
hideturtle()

# Design the line pattern at the top
def designline():
    s.hideturtle()
    s.speed(0)
    s.penup()
    s.shapesize(stretch_wid=0.75, outline=None)  # Adjust size 
    s.goto(-700, 305)
    s.shape("circle")
    s.pendown()
    for i in range(42):
        s.color(["#D80A0A", "#B81A19"][i % 2])
        s.stamp()
        s.forward(10)
    s.penup()
    s.goto(0, 0)

# Circular Border design
def design():
    s.hideturtle()
    s.speed(0)
    s.goto(0, -392)
    s.shapesize(stretch_wid=1, outline=None)
    s.shape("circle")
    for i in range(190):
        s.circle(393, 360 / 190)
        s.color(["#008000", "#ffea00"][i % 2])
        s.stamp()
    s.goto(0, 0)

# Draw a filled circle
def circle(radius, color, fill_color):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.penup()
    s.goto(0, -radius)  
    s.pendown() 
    s.color(color, fill_color)
    s.begin_fill()
    s.circle(radius)
    s.end_fill()

# Create circular patterns with colored divisions
def circle_with_colored_divisions(radius, divisions, colors):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0) 
    s.penup()
    s.goto(0, -radius) 
    s.pendown()
    s.circle(radius)
    angle = 360 / divisions  
    for i in range(divisions):
        s.penup()
        s.goto(0, 0) 
        s.pendown()
        s.color(colors[i % len(colors)])
        s.begin_fill()
        s.setheading(90) 
        s.right(angle * i) 
        s.forward(radius)  
        s.left(90) 
        s.circle(radius, angle)  
        s.left(90)  
        s.forward(radius) 
        s.end_fill()

# Create a triangle pattern with a specific color
def triangle(len, clr):
    s.hideturtle()
    s.speed(0)
    s.color(clr)
    for i in range(36):
        s.begin_fill()
        s.forward(len / math.tan(math.pi / 3.6))
        s.left(130)
        s.forward(len / math.sin(math.pi / 3.6))
        s.left(100)
        s.forward(len / math.sin(math.pi / 3.6))
        s.left(130)
        s.forward(len / math.tan(math.pi / 3.6))
        s.end_fill()
        s.left(10)
        s.speed(0)
    s.left(5)

# Create a rectangle with a specific color and rotation angle
def rectangle1(x, y, width, height, color1, color2, angle=0):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.goto(x, y) 
    s.setheading(angle)
    s.pendown()
    s.fillcolor(color2) 
    s.begin_fill()
    s.left(90)
    s.forward(height)
    s.left(90)
    s.forward(width)
    s.left(90)
    s.forward(height)
    s.end_fill()

# Create a rectangle with a specific color and rotation angle
def rectangle2(x, y, width, height, color1, color2, angle=0):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.goto(x, y)
    s.setheading(angle)
    s.pendown()
    s.fillcolor(color2)
    s.begin_fill()
    s.left(90)
    s.forward(2)
    s.left(90)
    s.forward(width)
    s.left(90)
    s.forward(height)
    s.end_fill()

# Create a rectangle with a specific color and rotation angle
def rectangle3(x, y, width, height, color1, color2, angle=0):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.goto(x, y) 
    s.setheading(angle)  
    s.pendown()
    s.fillcolor(color2) 
    s.begin_fill() 
    s.left(90)
    s.forward(height)
    s.left(90)
    s.forward(width)
    s.left(105)
    s.forward(2)
    s.end_fill()

# Create a trapezium roof with a specific color
def trapeziumroof(points, color1, color2):
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.penup()
    s.pencolor(color1)
    s.pensize(3)
    s.goto(points[0])
    s.pendown()
    s.fillcolor(color2)
    s.begin_fill()
    for point in points[1:]:
        s.goto(point)
    s.goto(points[0])
    s.end_fill()

# Build MEC using rectangles and  trapeziumroof
def model():
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    for i in range(3):
        rectangle1(15, -20 + i * 10, 30, 10, "#8d6b48", "#e8c9ab")
        rectangle2(40, -5 + i * 10, 25, 10, "#8d6b48", "#e8c9ab", angle=15)
        rectangle3(-17, -20 + i * 10, 25, 10, "#8d6b48", "#e8c9ab", angle=-15)
    points1 = [(-18, 14), (15, 14), (6, 22), (-8, 22)]
    trapeziumroof(points1, "#8d6b48", "#e8c9ab")


### Calling all the drawing functions ###

designline()
# Drawing border design
design()
# Drawing circles and patterns
circle(385, "#6A040F", "#6A040F")
circle(370, "#9D0208", "#9D0208")
# Triangular patterns
triangle(360, "#DC2F02")
triangle(327, "#E85D04")
triangle(295, "#FAA307")
triangle(268, "#FFBA08")
triangle(245, "white")
triangle(225, "#7D82B8")
triangle(205, "#613F75")
triangle(185, "#03071e")
# Smaller circles with colored divisions
circle(167, "white", "#fff9ec")
circle(140, "black", "#2b2d42")
colors = ['#610b01', '#002107']  # 2 different colors
circle_with_colored_divisions(138, 8, colors)
colors = ['#E85D04', '#01330c']  # 2 different colors
circle_with_colored_divisions(118, 8, colors)
circle(98, "yellow", "yellow")
circle(78, "white", "white")
colors = ['#ffffff', '#ffba08', '#f48c06', '#dc2f02', '#d00000', '#9d0208']  # 6 different colors
circle_with_colored_divisions(70, 24, colors)
colors = ['#ffba08', '#f48c06', '#dc2f02', '#d00000', '#9d0208', '#ffffff']  # 6 different colors
circle_with_colored_divisions(60, 24, colors)
colors = ['#f48c06', '#dc2f02', '#d00000', '#9d0208', '#ffffff', '#ffba08']  # 6 different colors
circle_with_colored_divisions(50, 24, colors)
circle(44, "#004b23", "#004b23")
colors = ['#25a244', '#2dc653']  # 2 different colors
circle_with_colored_divisions(40, 12, colors)
# Building MEC at centre
model()
# Exit on click
turtle.Screen().exitonclick()