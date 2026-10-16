import random

count = 0

def p():
    x = random.randint(1, 100)
    y = random.randint(0, 5)

    result = 1
    text = ""
    i = 0
    if y == 0:
        text = "1"
    else:
        while i < y:
            result = result * x
            if i == 0:
                text = str(x)
            else:
                text = text + "*" + str(x)
            i += 1

    print("p(" + str(x) + "," + str(y) + ") = " + text + " = " + str(result))

while count < 10:
    p()
    count += 1