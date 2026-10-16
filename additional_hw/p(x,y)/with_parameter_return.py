import random

count = 0

def p(x, y):
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
    return text, result

while count < 10:
    x = random.randint(1, 100)
    y = random.randint(0, 5)

    text, answer = p(x, y)

    print("p(" + str(x) + "," + str(y) + ") = " + text + " = " + str(answer))

    count += 1