from turtle import *

width(3)
speed(50)

def round_left(x):
    for i in range(x):
        left(90/x)
        forward(1)

for i in range(3):
    forward(100)
    round_left(5)
    forward(50)
    round_left(5)

forward(12)
right(90)

round_left(20)
forward(50)
round_left(20)
penup()
for i in range(20):
        right(90/20)
        backward(1)
backward(25)
right(90)
width(5)
forward(3)
pendown()
forward(60)
width(3)

right(90)
for i in range(25):
    left(i*0.05+3)
    forward(5)
for i in range(5):
    left(1)
    forward(5)
left(90)
forward(50)

done()