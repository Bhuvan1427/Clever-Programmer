import turtle
import random
t = turtle.Turtle()
t.pencolor("white")
t.pensize(10)
wn = turtle.Screen()
wn.title("Find the shape ")
wn.bgcolor("Blue")


t.hideturtle()

def one():
    variable=1
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Line", align="center", font=("Alergian", 24, "normal"))

def two():
    variable=2
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Line", align="center", font=("Alergian", 24, "normal"))

def three():
    variable=3
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Triangle", align="center", font=("Alergian", 24, "normal"))

def four():
    variable=4
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Square", align="center", font=("Alergian", 24, "normal"))

def five():
    variable=5
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Pentagon'", align="center", font=("Alergian", 24, "normal"))

def six():
    variable=6
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Hexagon", align="center", font=("Alergian", 24, "normal"))

def seven():
    variable=7
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Heptagon", align="center", font=("Alergian", 24, "normal"))

def eight():
    variable=8
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 260)
    t.write("Octagon", align="center", font=("Alergian", 24, "normal"))

def nine():
    variable=9
    for count in range(variable):
        t.forward(100)
        t.left(360/variable)
    t.speed(0)
    t.shape("square")
    t.color("white")
    t.penup()

    t.goto(0, 290)
    t.write("Nonagon", align="center", font=("Alergian", 24, "normal"))

wn.onkeypress(one,"1")
wn.onkeypress(two,"2")
wn.onkeypress(three,"3")
wn.onkeypress(four,"4")
wn.onkeypress(five,"5")
wn.onkeypress(six,"6")
wn.onkeypress(seven,"7")
wn.onkeypress(eight,"8")
wn.onkeypress(nine,"9")
wn.listen()
turtle.done()