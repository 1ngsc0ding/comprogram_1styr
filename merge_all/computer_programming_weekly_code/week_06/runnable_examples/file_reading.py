# Week 06: read a text file line by line
from pathlib import Path

path = Path("example.txt")
# Create a sample file so this example runs immediately.
if not path.exists():
    path.write_text("12\n7\n5\n", encoding="utf-8")

with path.open("r", encoding="utf-8") as file:
    content = file.read()
print("Whole file:")
print(content, end="")

print("\nNumbers:")
values = []
with path.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            values.append(int(line))
print(values)
print("Sum:", sum(values))
