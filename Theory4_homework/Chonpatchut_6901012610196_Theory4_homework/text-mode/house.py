house = [
    "|||||",
    "|   |",
    "|   |",
    "|||||",
    "^   ^",
    " ^ ^ ",
    "  ^  ",
]

# Reverse the stored layers so the house is printed from top to bottom.
for layer in reversed(house):
    print(layer)
