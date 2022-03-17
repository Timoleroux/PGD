from turtle import *
from random import randint, choice
import time

def grid():
    speed(0)
    pensize(2)
    pencolor("black")
    goto(0, -5)
    for i in range(5):
        circle(i)
    pencolor("gray")
    penup()
    goto(-500, -500)
    pendown()
    goto(-500, -500)
    goto(500, -500)
    goto(500, 500)
    goto(-500, 500)
    goto(-500, -500)

    for i in range(6):
        pendown()
        forward(1000)
        penup()
        goto(-500, i*100)

    for i in range(6):
        pendown()
        forward(1000)
        penup()
        goto(-500, i*(-100))

    goto(0, -500)
    right(90)

    for i in range(6):
        pendown()
        forward(1000)
        penup()
        goto(i*100, 500)

    for i in range(6):
        pendown()
        backward(1000)
        penup()
        goto(i*(-100), -500)


def walk():
    x_or_y = choice([True, False])
    if x_or_y:
        return [choice([-100,100]),0]
    else:
        return [0, choice([-100,100])]

def main():
    grid()
    succes = 0
    count = 0
    x = 0
    y = 0
    pencolor("red")
    for i in range(300_000):
        penup()
        goto(0, 0)
        pendown()
        x = 0
        y = 0
        for i in range(4):
            coor = walk()
            x += coor[0]
            y += coor[1]
            goto(int(x),int(y))
        if x == 0 and y == 0:
            succes += 1
        count += 1
    print(succes, count)

tic = time.perf_counter()
main()
toc = time.perf_counter()
# Print the Difference Minutes and Seconds
print(f"Build finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
# For additional Precision
print(f"Build finished in {toc - tic:0.4f} seconds")
done()