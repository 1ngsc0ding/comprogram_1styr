# Week 05 — Lists, 2D lists, nested loops, parallel arrays, charts

Source PDF pages 284–373. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 284

```text
010123138 
Computer Programming
```

## PDF page 285

```text
2
Check Attendance..
```

## PDF page 286

```text
3
Review
```

## PDF page 287

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

## PDF page 288

```text
5
Function and Array
def print_all(a):
    i = 0  # index
    while ( i < len(a)):  # len(a) is length of a
        print( a[i] )     # print element at i
        i = i + 1
a = [ 5, 9, 2 ]
print_all(a)
```

## PDF page 289

```text
6
2D Array
# 1D array (list of elements)
a = [ 3, 8, 2 ]
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ] 
#          m[0]         m[1]         m[2]
```

## PDF page 290

```text
7
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ] 
print( m[0][0] )  # 5   use 2 indexes (row,col)
print( m[0][1] )  # 7
print( m[1][0] )  # 2
```

## PDF page 291

```text
8
2D Array
# 2D array (list of lists)
# use 2 indexes (row,col)
m[1][2] = 7
m[2][2] = 5
```

## PDF page 292

```text
9
Array of Arrays
def print_all(a):      # same as before (for 1D array)
    i = 0  # index
    while ( i < len(a)):  
        print( a[i] )
        i = i + 1
print_all( m[1] )  # send an array, m[1]
```

## PDF page 293

```text
10
Array of Arrays
# print every element
print_all( m[0] )
print_all( m[1] )
print_all( m[2] )
# need a loop?
```

## PDF page 294

```text
11
Array of Arrays
def print_2D(m):      
    i = 0  # index
    while ( i < len(m)):   # loop
        print_all( m[i] )  # another loop?
        i = i + 1
print_2D( m )  # send an array, m
```

## PDF page 295

```text
12
Nested Loop
def print_2Dn(m):      
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( m[i] )):   # nested loop
            print( m[i][j] )
            j = j + 1
        i = i + 1
```

## PDF page 296

```text
13
Sum
def sum_2Dn(m):
    sum = 0      
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( m[i] )):   # inner loop
            sum = sum + m[i][j]
            j = j + 1
        i = i + 1
    return sum
```

## PDF page 297

```text
14
Count
def count_2Dn(m , x):
    count = 0
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( m[i] )):   # inner loop
            if (m[i][j] == x):
                count = count + 1
            j = j + 1
        i = i + 1
    return count
```

## PDF page 298

```text
15
Matrix
A = [[1, 2],\
     [3, 4]]
B = [[5, 6],\
     [7, 8]]
# can use 2D array?
```

## PDF page 299

```text
16
Add 2 Matrices
def addm(A, B):
    result = []
    i = 0
    while i < len(A):  # loop every row
        row = []
        j = 0
        while j < len(A[i]): # loop every column
            row.append( A[i][j] + B[i][j] )
            j = j + 1
        result.append( row )
        i = i + 1
    return result
```

## PDF page 300

```text
17
A = [[1, 2],\
     [3, 4]]
B = [[5, 6],\
     [7, 8]]
print( addm(A, B) )
# Try and see on pythontutor.com
Add 2 Matrices
```

## PDF page 301

```text
18
Need a Volunteer
```

## PDF page 302

```text
19
Problem Solving
How to organise and reuse code?
```

## PDF page 303

```text
20
Problem Solving
 - variables (single, array)
 - functions (statements, conditionals, loops)
```

## PDF page 304

```text
21
Problem Solving
 - variables (single, array)
 - functions (statements, conditionals, loops)
      divide into several functions
       (draw_balloon(), draw_house() )
```

## PDF page 305

```text
22
Problem Solving
 - variables (single, array)
 - functions (statements, conditionals, loops)
      to draw ballon in another program
```

## PDF page 306

```text
23
Floating Balloon
# What data are needed
```

## PDF page 307

```text
24
Floating Balloon
# What data are needed
# x , y, size
```

## PDF page 308

```text
25
Floating Balloon
# What data are needed
# x , y, size
# how we store them
```

## PDF page 309

```text
26
Create a class
class Balloon: 
    ...
# to store data of a single balloon
```

## PDF page 310

```text
27
Create a class
class Balloon: # specify class name
    ...
```

## PDF page 311

```text
28
Create a class
class Balloon: # specify class name
    def __init__( ... ):  # specify constructor
        ...
# similar concept to a function
# to construct/create object (a single balloon)
```

## PDF page 312

```text
29
Create a class
class Balloon: # specify class name
    def __init__(self, x, y, r):  # specify constructor
        ...
# similar concept to a function
# to construct/create object (a single balloon)
# need x, y, r as parameter (skip self for now :)
```

## PDF page 313

```text
30
Create a class
class Balloon: # specify class name
    def __init__(self, x, y, r):  # specify constructor
        self.x = x
        self.y = y
        self.r = r
# similar concept to a function
# to construct/create object (a single balloon)
# create its attributes (x, y, r) from parameters
```

## PDF page 314

```text
31
Create Object
b = Balloon(400, 600, 50)
# this will call its constructor
# In Python __init__() will be called
# A Class is a template/blueprint of an object
```

## PDF page 315

```text
32
Create Object
b = Balloon(400, 600, 50)
# this will call its constructor
# In Python __init__() will be called
# A Class is a template/blueprint of an object
```

## PDF page 316

```text
33
May print it?
b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
    print(b)
```

## PDF page 317

```text
34
May print it?
b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
    print(b)
# graphic mode - should draw on screen :)
```

## PDF page 318

```text
35
...
```

## PDF page 319

```text
36
Add a method to a class
class Balloon: # specify class name
    def __init__(self, x, y, r):  # specify constructor
        ...
    def show(self):  # it will show/draw balloon 
        ...
# similar concept to a function
# self -> itself     (many languages use "this")
# using its own data/attributes (x, y, r)
```

## PDF page 320

```text
37
Add a method to a class
class Balloon: # specify class name
    def __init__(self, x, y, r):  # specify constructor
        ...
    def show(self):
        line(self.x, self.y, self.x, self.y + 100)
        ellipse(self.x, self.y, self.r, self.r)
# it will show/draw balloon 
# using its own data/attributes (self.x, self.y, self.r)
```

## PDF page 321

```text
38
Assign/Use attributes
class Balloon: # specify class name
    def __init__(self, x, y, r):  # specify constructor
        self.x = x
        self.y = y
        self.r = r
    ...
# show() will show/draw balloon 
# using its own data/attributes (self.x, self.y, self.r) 
# assign when created an object, constructor is called
```

## PDF page 322

```text
39
Call a method
b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
    b.show()
# graphic mode - should draw on screen :)
```

## PDF page 323

```text
40
...
```

## PDF page 324

```text
41
Add another method
    def move(self):
        if self.y > width / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4
# only 1 parameter, "self"
```

## PDF page 325

```text
42
Call move() to animate
def draw():
    background(255)
    b.show()
    b.move()
```

## PDF page 326

```text
43
Call move() to animate
def draw():
    background(255)
    b.show()
    b.move()
# do not need to change its data (attributes)?
# only call its methods
```

## PDF page 327

```text
44
...
```

## PDF page 328

```text
45
Array of objects
balloons = []  # create an empty array
def setup():
    size(1000, 1000)
    ...
```

## PDF page 329

```text
46
Array of objects
def setup():
    size(1000, 1000)
    x_coords = [100, 200, 400, 500, 600]
    y_coords = [900, 850, 600, 700, 950]
    
    i = 0
    while i < len(x_coords):
        balloons.append(Balloon(x_coords[i], y_coords[i], 50))
        i = i + 1
```

## PDF page 330

```text
47
Array of objects
def draw():
    background(255)
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        i = i + 1
```

## PDF page 331

```text
48
...
```

## PDF page 332

```text
49
Floating Cloud
# What data are needed
# x , y, size
# To try
```

## PDF page 333

```text
50
Class
What you are interested in
- Attributes (Data/state)
- Methods (Behaviour/action/calculation/function)
```

## PDF page 334

```text
51
Big Picture
Consists of many item/entity/คน/สัตว์/สิ่งของ
- Balloon
- Cloud
- Cat, Dog, House, Tree, ...
```

## PDF page 335

```text
52
Big Picture
Consists of many item/entity/คน/สัตว์/สิ่งของ
- Balloon
- Cloud
- Cat, Dog, House, Tree, Car, Bike, ...
Solve the problem, and reuse later?
```

## PDF page 336

```text
53
...
```

## PDF page 337

```text
54
Python Built-in Classes
- int, float, bool, complex
- list, str, set, dict
- file (file-like objects)
(try then find more)
```

## PDF page 338

```text
55
Class File in Python
For reading and writing text file
```

## PDF page 339

```text
56
Class File in Python
f = open("output.txt", "w")   # open ﬁle for writing
```

## PDF page 340

```text
57
Class File in Python
f = open("output.txt", "w")   # open ﬁle
f.write( "Hello, everybody" ) # call method write()
```

## PDF page 341

```text
58
Class File in Python
f = open("output.txt", "w")   # open ﬁle
f.write( "Hello, everybody" ) # call method write()
# f is an object
# write( ) is a method
```

## PDF page 342

```text
59
Class File in Python
f = open("output.txt", "w")   # open ﬁle
f.write( "Hello, everybody" ) # call method write()
f.close()
# close( ) is a method
# do not forget to close the file after writing
```

## PDF page 343

```text
60
Class File in Python
f = open("output.txt", "w")   # open ﬁle
f.write( "Hello, everybody" ) # call method write()
f.close()
# different from print() ?
```

## PDF page 344

```text
61
File name and Path
path is a string that spectify location of a ﬁle or
directory
e.g.
    c:\doc.txt
    c:\windows
    d:\home\example\
```

## PDF page 345

```text
62
Current working directory
# Where your program is running
```

## PDF page 346

```text
63
Current working directory
# Where your program is running
import os
print( os.getcwd( ) ) 
# cwd - current working directory
```

## PDF page 347

```text
64
Change directory
import os
print( os.chdir( "c:\\home" ) )  # may need escape \
```

## PDF page 348

```text
65
Change directory
import os
print( os.chdir( "c:\\home" ) )  # may need escape \ 
print( os.getcwd( ) ) # cwd will change to c:\home
```

## PDF page 349

```text
66
List directory
import os
print( os.getcwd( ) ) 
print( os.listdir( ) ) # list of ﬁles and directories in cwd
e.g.
   ['example.txt', 'program', 'doc', 'lab.py']
```

## PDF page 350

```text
67
Boolean functions
import os
print( os.path.exists("sample") ) # the path exists ?
```

## PDF page 351

```text
68
Boolean functions
import os
print( os.path.exists("sample") ) # the path exists ?
print( os.path.isﬁle("sample") ) # is it a ﬁle?
print( os.path.isdir("sample") ) # is it a directory?
```

## PDF page 352

```text
69
File Size
import os
ﬁle_size = os.path.getsize( "output.txt" )
```

## PDF page 353

```text
70
File Size
import os
ﬁle_size = os.path.getsize( "output.txt" )
print( "File Size is :", ﬁle_size, "bytes" )
```

## PDF page 354

```text
71
Abstaction
Hide complex implementation details
- how the operating system represents files
- how filesystem metadata is accessed
- how paths are handled
  Works other Operating Systems?
```

## PDF page 355

```text
72
Abstaction
Hide complex implementation details
- how the operating system represents files
- how filesystem metadata is accessed
- how paths are handled
  Compare to using a TV remote / drive a car
```

## PDF page 356

```text
73
Encapsulation
Hide data, and only allow to access via methods
```

## PDF page 357

```text
74
Encapsulation
Hide data, and only allow to access via methods
  Should not access Balloon x,y positions directly?
```

## PDF page 358

```text
75
Encapsulation
Hide data, and only allow to access via methods
  Should not access Balloon x,y positions directly?
  use move() , show()
```

## PDF page 359

```text
76
...
```

## PDF page 360

```text
77
Create your own
- my_complex
(from array/list?)
```

## PDF page 361

```text
78
Create your own
- my_complex, my_set
(from array/list?)
```

## PDF page 362

```text
79
...
```

## PDF page 363

```text
80
Prepare Python Library
- Turtle
- Tkinter
- Matplotlib
```

## PDF page 364

```text
81
Try sample code
import turtle
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
turtle.done()
```

## PDF page 365

```text
82
Try sample code
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_oval(200, 50, 400, 250, fill="orange")
canvas.create_line(300, 250, 300, 450)
root.mainloop()
```

## PDF page 366

```text
83
Try sample code
import matplotlib.pyplot as plt
# 4 weeks × 7 days
temperatures = [
    [30, 31, 32, 30, 30, 31, 33],  # Week 1
    [29, 30, 31, 32, 31, 30, 29],  # Week 2
    [31, 32, 33, 34, 32, 31, 30],  # Week 3
    [30, 29, 30, 30, 29, 30, 32]   # Week 4
]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for week in temperatures:
    plt.plot(days, week)
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.title("Temperature for 4 Weeks")
plt.legend(["Week 1", "Week 2", "Week 3", "Week 4"])
plt.show()
```

## PDF page 367

```text
84
...
```

## PDF page 368

```text
85
Assessment
Lecture 10%
Lab
 
10%
A1
10%
A2
10%
Midterm 30%
Final
30%
(maybe adjusted)
```

## PDF page 369

```text
86
Assessment
Lecture 10% consists of
- After class quizzes (individual)
- Task 1 (group work)
- Task 2 (group work)
```

## PDF page 370

```text
87
Assessment
Lecture 10% consists of
- Task 1 (group work)
   - find exercises (coding 
question) and write solution
   - create quizzes (google form)
w1 for group 1, w2 for group 2, ...
```

## PDF page 371

```text
88
Assessment
Lecture 10% consists of
- Task 2 (group work)
   - find 5 example classes from 
other textbooks in the library
     (may not in Python)
```

## PDF page 372

```text
89
Assessment
Lecture 10% consists of
- Task 2 (group work)
   - find 5 example classes from 
other textbooks in the library
     (may not in Python)
   - note their attributes and 
methods 
(create slides and submit by Friday, and every 
member prepare to present next week)
```

## PDF page 373

```text
90
...
```

