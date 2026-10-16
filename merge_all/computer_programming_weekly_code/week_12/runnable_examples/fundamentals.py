# Week 12: input/output, variables, functions and conditions
def draw_coordinates(x, y):
    # Console equivalent: report the coordinates that a drawing call would use.
    print(f"Balloon centre=({x}, {y}), ellipse=({x}, {y}, 100, 100)")
    print(f"String line from ({x}, {y + 50}) to ({x}, {y + 200})")

def show_area(width, height):
    area = width * height
    print(f"The result area is {area} (in square meter)")
    return area

def main():
    print("Hello, World")
    x = 200
    y = 100
    draw_coordinates(x, y)
    draw_coordinates(400, 200)
    width = 5
    height = 8
    show_area(width, height)

if __name__ == "__main__":
    main()
