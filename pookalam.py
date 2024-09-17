import turtle
from turtle import *
import math
s = turtle.Turtle()

#happy onam
penup()
goto(-700,320)
pendown()
color("red")
write("Happy Onam!",font=("Times New Roman",50,"bold"))

#submitted by
color("#6c55ed")
penup()
goto(350,-300)
pendown()
color("#03071e")
write("- Aaron Kurian Abraham",font=("Times New Roman",20)) #"italic"))
penup()
goto(350,-350)
pendown()
write("- CS3A",font=("Times New Roman",20))#, "italic"))



def designline():
    s.penup()
    s.shapesize(stretch_wid=0.75, outline=None)  # Adjust size here (e.g., 2 times the default size)
    # Circular ring pattern - on outside circle
    s.goto(-700,305)
    s.shape("circle")
    s.pendown()
    for i in range(42):
        
        s.color(["#D80A0A","#B81A19"][i%2])
        s.stamp()
        s.forward(10)
    s.penup()
    s.goto(0,0)
designline()


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

######
def draw_rectangle1(x, y, width, height, color1,color2, angle=0):
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.speed(0)
    s.goto(x, y)  # Go to starting position (x, y)
    s.setheading(angle)  # Set the angle of the turtle
    s.pendown()  # Start drawing
    s.fillcolor(color2)  # Set the fill color
    s.begin_fill()  # Begin filling the shape

    # Draw top side
    s.left(90)
    s.forward(height)
    s.left(90)
    
    # Draw right side
    s.forward(width)
    s.left(90)
    
    # Draw the second top side
    s.forward(height)
    #s.left(90)
    
    # Draw left side and lift pen to leave bottom invisible
    #s.forward(height)
    
    s.end_fill()  # End filling the shape
   
# Set turtle speed and pensize for clarity

def draw_rectangle2(x, y, width, height, color1,color2, angle=0):
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.speed(0)
    s.goto(x, y)  # Go to starting position (x, y)
    s.setheading(angle)  # Set the angle of the turtle
    s.pendown()  # Start drawing
    s.fillcolor(color2)  # Set the fill color
    s.begin_fill()  # Begin filling the shape

    # Draw top side
    s.left(90)
    s.forward(2)
    s.left(90)
    
    # Draw right side
    s.forward(width)
    s.left(90)
    
    # Draw the second top side
    s.forward(height)
   
    s.end_fill()

def draw_rectangle3(x, y, width, height, color1,color2, angle=0):
    s.speed(0)
    s.pencolor(color1)
    s.pensize(3)
    s.penup()
    s.goto(x, y)  # Go to starting position (x, y)
    s.setheading(angle)  # Set the angle of the turtle
    s.pendown()  # Start drawing
    s.fillcolor(color2)  # Set the fill color
    s.begin_fill()  # Begin filling the shape

    # Draw top side
    s.left(90)
    s.forward(height)
    s.left(90)
    
    # Draw right side
    s.forward(width)
    s.left(105)
   
    # Draw the second top side
    s.forward(2)
    #s.left(90)
    s.end_fill()


''' s.fillcolor(color)
    s.begin_fill()
    for _ in range(2):
        s.forward(width)
        s.left(90)
        s.forward(height)
        s.left(90)
    s.end_fill()'''

def draw_polygon(points, color1,color2):
    s.penup()
    s.pencolor(color1)
    s.goto(points[0])
    s.pendown()
    s.fillcolor(color2)
    s.begin_fill()
    for point in points[1:]:
        s.goto(point)
    s.goto(points[0])
    s.end_fill()

def mec():
    # Create the turtle object
    global s
    s = turtle.Turtle()
    s.speed(0)  # Set the fastest drawing speed

    # Draw the rectangles (representing the bars)
    for i in range(3):
        draw_rectangle1(15, -20 + i * 10, 30, 10, "#8d6b48","#e8c9ab")
        draw_rectangle2(40, -5 + i * 10, 25, 10, "#8d6b48","#e8c9ab", angle=15)
        draw_rectangle3(-17, -20 + i * 10, 25, 10, "#8d6b48","#e8c9ab", angle=-15)

    # Draw the first polygon (trapezoid-like shape)

    points1 = [(-18, 14), (15, 14), (8, 22), (-8, 22)]
    draw_polygon(points1, "#8d6b48","#e8c9ab")

    # Draw the second polygon (smaller trapezoid-like shape)
    '''points2 = [(0, 17), (25, 17), (29, 22), (3, 22)]
    draw_polygon(points2, "tomato")'''

    # Finish the drawing
   # turtle.done()


#####

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


def draw_circle_with_colored_divisions1(radius, divisions, colors):
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
        
        # Set the fill color from the list of 6 colors
        s.color(colors[i % len(colors)])
        
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

# Set up parameters


colors = ['#ffffff', '#ffba08', '#f48c06', '#dc2f02', '#d00000', '#9d0208']  # 6 different colors



def design():
    
    # Circular ring pattern - on outside circle
    s.goto(0,-392)
    s.shapesize(stretch_wid=1, outline=None)
    s.shape("circle")
    for i in range(190):
        s.circle(393,360/190)
        s.color(["#008000","#ffea00"][i%2])
        s.stamp()
    s.goto(0,0)

design()



#draw_simple_circle(413, "#008000", "#008000")
#draw_simple_circle(398, "#ffea00", "#ffea00")
draw_simple_circle(385, "#6A040F", "#6A040F")
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


draw_circle_with_colored_divisions1(70, 24, colors)
colors = ['#ffba08', '#f48c06', '#dc2f02', '#d00000', '#9d0208','#ffffff']  # 6 different colors
draw_circle_with_colored_divisions1(60, 24, colors)
colors = ['#f48c06', '#dc2f02', '#d00000', '#9d0208','#ffffff','#ffba08' ]  # 6 different colors
draw_circle_with_colored_divisions1(50, 24, colors)
draw_simple_circle(40, "white", "white")
colors = ['#38b000', '#70e000']# '#dc2f02', '#d00000', '#9d0208']  # 6 different colors
draw_circle_with_colored_divisions1(40, 12, colors)
# Run the mec() function
mec()

turtle.Screen().exitonclick()