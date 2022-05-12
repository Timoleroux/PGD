def deuxEntiers() :
    x = 0
    y = 36

    for i in range(36):
        y -= 1
        x += 1

        if y - x == 8 and x + y == 36:
            print("Pour deux entiers : x =", x, "et y =", y)

def deuxAutreEntiers() :
    x = -5000
    y = -5007

    for i in range(10000):
        y += 1
        x += 1

        if (x-y == 7 or y-x == 7) and ( y*y - x*x == 21 or x*x - y*y == 21):
            print("Pour deux autre entiers : x =", x, "et y =", y)