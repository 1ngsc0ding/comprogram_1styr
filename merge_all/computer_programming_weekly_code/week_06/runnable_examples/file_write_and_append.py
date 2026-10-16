# Create, overwrite, append, and read a text file
from pathlib import Path

path = Path("notes.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Computer Programming\n")
with path.open("a", encoding="utf-8") as file:
    file.write("File operations\n")
with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
