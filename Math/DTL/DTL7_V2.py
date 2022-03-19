import turtle as t
import random as rd
import time

def grid():
    t.speed(0)
    t.pensize(2)
    t.color("gray")
    t.shape("circle")
    
    t.penup()
    t.goto(-500, -500)
    t.pendown()

    
    for i in range(5):
        t.setheading(0)
        t.forward(1000)
        t.goto(t.xcor(), t.ycor() + 100)
        t.backward(1000)
        t.goto(t.xcor(), t.ycor() + 100)
    
    t.forward(1000)
    for i in range(5):
        t.setheading(270)
        t.forward(1000)
        t.goto(t.xcor() - 100, t.ycor())
        t.backward(1000)
        t.goto(t.xcor() - 100, t.ycor())
    t.forward(1000)

def walk():
    coord = [0, 0]
    t.speed(5)
    t.color("red")
    t.penup()
    t.hideturtle()
    t.goto(0, 0)
    t.showturtle()
    t.pendown()

    for i in range(4):
        choice = rd.choice(["i", "j", "-i", "-j"])
        if choice == "i":
            coord[0] += 100
            t.goto(coord[0], coord[1])
        elif choice == "j":
            coord[1] += 100
            t.goto(coord[0], coord[1])
        elif choice == "-i":
            coord[0] -= 100
            t.goto(coord[0], coord[1])
        elif choice == "-j":
            coord[1] -= 100
            t.goto(coord[0], coord[1])
    return coord

def main(N):
    succes = 0
    count = 0
    grid()

    for i in range(int(N)):
        if walk() == [0, 0]:
            succes += 1
        count += 1

    print(f"Le robot est revenu {succes} fois à sa position initiale avec {count} essais.")
    t.done()

main(50)