# Your name: Sreeram Panicker
# Your student id: 52604809
# Your email:psreeram@umich.edu
# List who you worked with on this homework: Ashwin Surapaneni

# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_circle(turtle, xpos, ypos, radius, color):
    
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)

    """

    Write a function to draw a circle on the screen using the specified parameters.
    
    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the circle
    :param ypos: The Y-axis coordinate for the starting point of the circle
    :param radius: The radius of the circle
    :param color: The line color and fill color to use for the circle
    """


def draw_rectangle(turtle, xpos, ypos, width, height, color):
    
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    for i in range(2):
        turtle.color(color)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    """
    Write a function to draw a shape of your choice.
    You must use a loop when drawing your shape.
    Rename the function (the SHAPE part) to match the shape you drew.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the shape
    :param ypos: The Y-axis coordinate for the starting point of the shape
    :param width: The width of the shape
    :param height: The height of the shape
    :param color: The line color and fill color to use for the shape
    """
 


def draw_triangle(turtle, xpos, ypos, width, height, color):
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    for i in range(3):
        turtle.color(color)
        turtle.forward(width)
        turtle.left(120)
    
    """
    Write a function to draw a shape of your choice.
    You do not have to use a loop to draw this shape, but you may if you wish.
    This shape should be different from the shape you drew in the previous
    function. Rename the function (the SHAPE2 part) to match the shape you drew.

    :param turtle: An instance of the Turtle class
    :param xpos: The X-axis coordinate for the starting point of the shape
    :param ypos: The Y-axis coordinate for the starting point of the shape
    :param width: The width of the shape
    :param height: The height of the shape
    :param color: The line color and fill color to use for the shape
    """
    

# Feel free to create other shapes using more functions like draw_SHAPE3, draw_SHAPE4, etc. 


def draw_face(turtle):
    draw_circle(turtle,0,0,100,"blue")
    draw_rectangle(turtle,25,125,5,7,"green")
    draw_rectangle(turtle,-25,125,5,7,"red")
    draw_triangle(turtle,0,80,15,10,"blue")
    draw_rectangle(turtle,-20,20,40,20,"blue")
    draw_rectangle(turtle,-75,200,125,75,"black")
    draw_triangle(turtle,-125,300,30,30,"black")
    
    
    """
    Write a function to create a face by calling draw_circle,
    draw_SHAPE, draw_SHAPE2 and any other functions (at least once each).

    Feel free to modify the arguments of this function as you like,
    but you should pass in the turtle object at the very least.

    Extra credit for using additional functions to add accessories to the face
    like a hat, bow, or tie. You can also earn extra credit for signing your 
    art with your initials in block letters.
    """

   


def main():
    space = Screen()
    turtle = Turtle()
    draw_face(turtle)
    turtle.getscreen().exitonclick()
    
    """
    Write a function that will be called when you run this program
    from the terminal.

    Make sure to create a Screen object, a Turtle object,
    and call draw_face.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting untill you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color. You can also call the .color() method on your Turtle
    instance if you want to change its color.
    """

 


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
