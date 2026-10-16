# Week 07 — Arrays, strings, algorithms and sorting concepts

Source PDF pages 439–494. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 439

```text
010123138 
Computer Programming
```

## PDF page 440

```text
2
Check Attendance..
```

## PDF page 441

```text
3
Review
```

## PDF page 442

```text
4
Array of variables
a = [ 5, 9, 2 ]
# Python use "list" (similar but not the same as array)
# from this example: size or length is 3 
# index start from 0 (up to 2)
index
element
```

## PDF page 443

```text
5
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print( a[i] )     # print element at i
    i = i + 1
```

## PDF page 444

```text
6
Algorithms
- find max
- check array is sorted
- sort array?
- calculate factorial
```

## PDF page 445

```text
7
Factorial
- using loop
- using recursive function
  
see on pythontutor.com
```

## PDF page 446

```text
8
String
s = "Hello"  # string of characters
print(s)    # display string in text mode
```

## PDF page 447

```text
9
String
s = "Hello"  # similar to array of characters
i = 0
while(i < len(s)):
    print( s[i] )
    i = i + 1
# In Python, a character is a string of length one
# but not in Java or C
H
e
l
l
o
```

## PDF page 448

```text
10
Escape Characters
print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")
Hello
World
He said "Hello"
Python
Programming
```

## PDF page 449

```text
11
String Concatenation ( + )
s = "Hello"  
t = "Joe"
print( s + t )
```

## PDF page 450

```text
12
String Concatenation ( + )
s = "Hello"
t = ""     
i = 0
while(i < len(s)):
    t = t + str(i)
    i = i + 1
print( t )
01234
```

## PDF page 451

```text
13
String Concatenation ( + )
s = "Hello"
t = ""     
i = 0
while(i < len(s)):
    t = t + str(i) + "\t" + s[i] + "\n"
    i = i + 1
print( t )
0
H
1
e
2
l
3
l
4
o
```

## PDF page 452

```text
14
Display String (graphic-mode)
def draw():
    fill(0)
# text color
    textSize(100)  # text size :)
    text("ABC", mouseX, mouseY)
```

## PDF page 453

```text
15
Array is mutable
a = [ 5, 9, 2 ]
a[0] = 7
Can change element in array
```

## PDF page 454

```text
16
String is immutable
s = "Hello"
s[0] = "J"   # Error
# TypeError: 'str' object does not support item assignment
# Cannot change element in array
```

## PDF page 455

```text
17
Create a new string
s = "Hello"
s = "J" + s[4] + s[1]
# Assign it to the same variable   
# Similar to earlier example
# t = t + str(i) + "\t" + s[i] + "\n"
```

## PDF page 456

```text
18
String Method (Function)
s = "3"
print( s.isalnum() )
# See
# https://py.processing.org/reference/string
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# (not the main focus)
True
```

## PDF page 457

```text
19
Question?
```

## PDF page 458

```text
20
Review Questions
```

## PDF page 459

```text
21
...
```

## PDF page 460

```text
22
Volatile data
Variables, Array, String
- Temporary information stored in RAM
- Lost when program is closed
  or power is lost
```

## PDF page 461

```text
23
Non-Volatile data
File on Storage (e.g. HDD/SSD)
- Persists without power, can be reused later
- Slower read/write speed 
  (compared to RAM)
```

## PDF page 462

```text
24
File Types
- Text File (e.g. .txt, .csv, .json, .html)
  They are human-readable, stored as characters (string)
- Binary File (e.g. .jpg, .mp3, .exe)
  for program to read
```

## PDF page 463

```text
25
File Operations
# Open a text file for reading ("r")
file = open("example.txt", "r")
# later, try other file modes: r, w, a
```

## PDF page 464

```text
26
File Operations
# Open a text file for reading ("r")
file = open("example.txt", "r")
# Read the entire content and print it
content = file.read()  # call a method 
print( content )  # Content is a string
```

## PDF page 465

```text
27
File Operations
# Open a text file for reading ("r")
file = open("example.txt", "r")
# Read the entire content and print it
content = file.read()  # call a method 
print( content )  # Content is a string
# Always close the file when finished
file.close()
```

## PDF page 466

```text
28
with statement
with open("example.txt", "r") as file:
    content = file.read()
    print( content )
# Recommended Way
# The file will be automatically closed
```

## PDF page 467

```text
29
a variable named f
with open("example.txt", "r") as f:
    content = f.read()
    print( content )
# use file to make it clear
```

## PDF page 468

```text
30
Read a line
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
```

## PDF page 469

```text
31
Print a line
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    print( line )
 # print it
```

## PDF page 470

```text
32
Read more lines?
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    print( line )
 # print it
     ...
```

## PDF page 471

```text
33
while the line is not empty
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    while line :
        print( line )
 # print it
        ...
```

## PDF page 472

```text
34
while the line is not empty
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    while line :
        print( line )
 # print it
        line = f.readline() # read the next line
```

## PDF page 473

```text
35
while the line is not empty
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    while line :
        print( line )
 # print it
        line = f.readline() # read the next line
# Loop condition :  line is not empty 
                   
# not the end of file (EOF)
```

## PDF page 474

```text
36
...
```

## PDF page 475

```text
37
for (each) loop
with open("example.txt", "r") as file:
    for line in file:    # for each line in file
```

## PDF page 476

```text
38
for (each) loop
with open("example.txt", "r") as file:
    for line in file:    # for each line in file
        print( line )    # print it
```

## PDF page 477

```text
39
Print line-by-line
with open("example.txt", "r") as file:
    for line in file:    # for each line in file
        print( line )    # print it
# Loop condition ?
```

## PDF page 478

```text
40
Process line-by-line
a = [] # start from empty list
with open("example.txt", "r") as file:
    for line in file:
        ...
        a.append( num )
# [5, 2, 7]
        
5
2
7
```

## PDF page 479

```text
41
Process line-by-line
a = [] # start from empty list
with open("example.txt", "r") as file:
    for line in file:
        num = int( line )  # convert to int
        a.append( num )
# [5, 2, 7]
        
5
2
7
```

## PDF page 480

```text
42
Process line-by-line
a = [] # start from empty list
with open("example.txt", "r") as file:
    for line in file:
        num = int( line )  # convert to int
        a.append( num )
print( a )  # result array (read values from file)
# [5, 2, 7]
        
5
2
7
```

## PDF page 481

```text
43
Process line-by-line
- Find max/min/avg value in file
        
  # need to create array?
5
2
7
12
4
9
```

## PDF page 482

```text
44
Process a line
a = [] # start from empty list
with open("example.txt", "r") as file:
    for line in file:
        # process and append to array
# string exercise?
# [5, 2, 7]
        
5,2,7
```

## PDF page 483

```text
45
Process a line
- Find a word in file
# string exercise?
```

## PDF page 484

```text
46
...
```

## PDF page 485

```text
47
Write to file
with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")
# similar to print()?
```

## PDF page 486

```text
48
Write to file
with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")
# similar to print()?
# must add newline (\n) manually
```

## PDF page 487

```text
49
Append to file
with open("output.txt", "a") as file:
    file.write("ECE\n")
    file.write("KMUTNB\n")
# add to the end of file
```

## PDF page 488

```text
50
Write values of Array
with open("output.txt", "w") as file:
    ...
# exercise
```

## PDF page 489

```text
51
...
```

## PDF page 490

```text
52
File not found
with open("example.txt", "r") as file:
    for line in file:
        print(line)
FileNotFoundError: No such file or directory: 'example.txt'
```

## PDF page 491

```text
53
Try and catch exception
try:
    with open("example.txt", "r") as f:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error: example.txt is not found")
```

## PDF page 492

```text
54
Invalid data from file
- String processing?
  isalpha(), isdigit(), is..?
```

## PDF page 493

```text
55
...
```

## PDF page 494

```text
56
A1
Save/load A1 data from file
```

