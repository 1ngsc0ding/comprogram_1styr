# Week 10: functions that return values
from math import sqrt

def calculate_distance(x1, y1, x2, y2):
    difference_x = x1 - x2
    difference_y = y1 - y2
    return sqrt(difference_x * difference_x + difference_y * difference_y)

if __name__ == "__main__":
    first = (100, 200)
    second = (mouse_x, mouse_y) if False else (160, 240)  # sample point in console mode
    distance = calculate_distance(first[0], first[1], second[0], second[1])
    print(f"Distance between {first} and {second}: {distance:.2f}")
