import turtle
from turtle import *
import math
s = turtle.Turtle()



def draw_simple_circle(radius, color, fill_color):
    s = turtle.Turtle()
    s.speed(0)

    screen = turtle.Screen()
    screen.bgcolor("white")  # Optional: set background color

    s.penup()  # Lift the pen to move without drawing
    s.goto(0, -radius)  # Move to the center of the circle
    s.pendown()  # Put the pen down to start drawing

    s.color(color, fill_color)
    s.begin_fill()
    s.circle(radius)  # Draw the circle with the specified radius
    s.end_fill()
    s.speed(0)

def drawCircle(color,colorfill, radius):
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(12):
        s.circle(radius)
        s.left(30)
    s.end_fill()
    s.speed(0)

def drawCircle2(color,colorfill, radius):
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(12,0,-2):
        s.circle(radius)
        s.left(60)
    s.end_fill()
    s.speed(0)

def drawtriangle(color,colorfill, length):
 
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(8):
        s.left(15)
        s.forward(length)
        s.left(90)
        s.circle(length, 30)
        s.left(90)
        s.forward(length)
    s.end_fill()
    s.speed(0)


def square1(radius,colour):
    s.color('purple', 'purple')
    
    s.begin_fill()
    for i in range(30):
       

        if(i%4==0):
            s.color(colour, colour)
            s.begin_fill()
        else:
            s.color(colour, colour)
            s.begin_fill()
      
        s.left(12)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.end_fill()
    s.speed(0)    
def tripatt(len,clr):
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

'''def square2(radius,colour):
    s.color('purple', 'purple')
    
    s.begin_fill()
    for i in range(30):
       

        if(i%4==0):
            s.color(colour, colour)
            s.begin_fill()
        else:
            s.color(colour, colour)
            s.begin_fill()
      
        s.left(12)
        s.forward(radius+5)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius+5)
        s.left(90)
        s.end_fill()'''

s.speed(0)



def draw_circle_with_colored_divisions(radius, divisions, color1, color2):
    s = turtle.Turtle()
    s.speed(0)  # Fastest drawing speed

    # Draw the circle outline
    s.penup()
    s.goto(0, -radius)  # Move the turtle to the starting point of the circle
    s.pendown()
    s.circle(radius)

    # Draw and color the divisions
    angle = 360 / divisions  # Angle between each division line
    for i in range(divisions):
        s.penup()
        s.goto(0, 0)  # Move the turtle to the center of the circle
        s.pendown()
        
        # Set the fill color
        if i % 2 == 0:
            s.color(color1)
        else:
            s.color(color2)
        
        s.begin_fill()
        
        # Draw the sector
        s.setheading(90)  # Point the turtle upwards
        s.right(angle * i)  # Rotate the turtle to the correct angle
        s.forward(radius)  # Draw the line to the circumference
        s.left(90)  # Turn left to face the circle edge
        s.circle(radius, angle)  # Draw the arc of the sector
        s.left(90)  # Turn left to return to the center
        s.forward(radius)  # Complete the triangle to the center
        
        s.end_fill()


draw_simple_circle(410, "black", "#370617")
draw_simple_circle(390, "#6A040F", "#6A040F")
draw_simple_circle(370, "#9D0208", "#9D0208")
#drawCircle('black','red', 290)
#square1(270,'#DC2F02')
#square1(250,'#E85D04')
#square1(230,'#FAA307')
#square1(210,'#FFBA08')
#square1(190,'white')
#square1(170,'#7D82B8')
#square1(150,'#613F75')

#square1(130,'#03071e')


tripatt(360,"#DC2F02")
tripatt(327, "#E85D04")
tripatt(295,"#FAA307")
tripatt(268,"#FFBA08")
tripatt(245, "white")
tripatt(225,"#7D82B8")
tripatt(205,"#613F75")
tripatt(185,"#03071e")

draw_simple_circle(167, "white", "#fff9ec")
draw_simple_circle(140, "black", "#2b2d42")
draw_circle_with_colored_divisions(138, 8, '#610b01', '#002107')
draw_circle_with_colored_divisions(118, 8, '#E85D04', '#01330c')
draw_simple_circle(98, "yellow", "yellow")
draw_simple_circle(78, "white", "white")


turtle.Screen().exitonclick()