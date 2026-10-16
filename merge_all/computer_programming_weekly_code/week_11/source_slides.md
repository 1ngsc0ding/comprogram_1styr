# Week 11 — Parameters, random values, animation and nested conditions

Source PDF pages 692–770. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 692

```text
3
Review
```

## PDF page 693

```text
4
Simple Output
size(500,500)
# draw balloon
ellipse(200,200,100,100)
line(200,250,200,400)
```

## PDF page 694

```text
5
Simple Output
size(500,500)
# draw balloon
ellipse(200,200,100,100)
line(200,250,200,400)
# draw another balloon 
ellipse(400,200,100,100) # change value of parameters/arguments
line(400,250,400,400)
```

## PDF page 695

```text
6
Use Variable
size(500,500)
x = 200 
y = 200
# draw balloon
ellipse(x, y, 100, 100)    
line(x, y+50, x, y+200)
x = x + 200   
# change value of variable
# draw another balloon 
ellipse(x, y, 100, 100)    
# same code?
line(x, y+50, x, y+200)
```

## PDF page 696

```text
7
Define draw_balloon()
def draw_balloon( ... ):
    ellipse(x, y, 100, 100) # same code inside the function
    line(x, y+50, x, y+200)
```

## PDF page 697

```text
8
Use Parameters
def draw_balloon( x, y ):
    ellipse(x, y, 100, 100) # same code inside the function
    line(x, y+50, x, y+200)
```

## PDF page 698

```text
9
When called, it will send arguments
def draw_balloon(x, y):
    ellipse(...)
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 699

```text
10
Copied to called function
def draw_balloon(x, y):
   x = 200 # similar result, as adding these two lines of code
   y = 200
    ellipse(...)
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 700

```text
11
Copied to called function
def draw_balloon(x, y):
   x = 200 # similar result , but do not write the code 
   y = 200
    ellipse(...)
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 701

```text
12
Parameters are local variables
def draw_balloon( x, y ):
    ellipse(x, y, 100, 100)
    line(x, y+50, x, y+200)
```

## PDF page 702

```text
13
Only 2 lines of code in draw_balloon()
def draw_balloon(x, y):
    ellipse(x, y, 100, 100)    
    line(x, y+50, x, y+200)
draw_balloon(200, 200)
```

## PDF page 703

```text
14
Call it twice, get 2 balloons : )
draw_balloon(200, 200)
draw_balloon(400, 200)
# only define a function  
   one time
```

## PDF page 704

```text
15
Use variables
# ...
draw_balloon(x, y)
draw_balloon(x, y)
```

## PDF page 705

```text
16
Use variables
x = 200
y = 200
draw_balloon(x, y)
draw_balloon(x, y)
# what will be shown?
```

## PDF page 706

```text
17
Use variables
x = 200
y = 200
draw_balloon(x, y)
x = x + 200          # must update value of x
draw_balloon(x, y)
# (to draw 2 balloons)
```

## PDF page 707

```text
18
Animation with a balloon
using 
●
setup()
●
draw()
●
global variable
```

## PDF page 708

```text
19
Global variable
def setup():
    size(500,500)
    
def draw():
    global x  
# where is it?
    draw_balloon(x, 200)
    x = x + 10
```

## PDF page 709

```text
20
Global variable
x = 200 
       # not inside a function
def setup():
    size(500,500)
    
def draw():
    global x
    draw_balloon( x , 200)
    x = x + 10
```

## PDF page 710

```text
21
Try with local variable
x = 200 
       # 2 variables named x
def setup():
    size(500,500)
    
def draw():
    x = 200
# local variable, inside a function
    draw_balloon( x , 200)
    x = x + 10
```

## PDF page 711

```text
22
Why does not work?
x = 200 
       # this x is global
def setup():
    size(500,500)
def draw():
    x = 200
# this x is local
    draw_balloon( x , 200)  
    x = x + 10
```

## PDF page 712

```text
23
Why does not work?
x = 200 
       # this x is global
def setup():
    size(500,500)
  
# They are not the same x
def draw():
    x = 200
# this x is local
    draw_balloon( x , 200)  
    x = x + 10
```

## PDF page 713

```text
24
Why does not work?
x = 200 
       
def setup():
    size(500,500)
    
def draw():
    x = 200
# no animation?
    draw_balloon( x , 200)
# same value of x
    x = x + 10
# every time draw() is called
```

## PDF page 714

```text
25
Why does not work?
x = 200 
       
def setup():
    size(500,500)
    
def draw():
    x = 200
    draw_balloon(200, 200)
# similar result?
    x = x + 10
```

## PDF page 715

```text
26
Simple conditional statement (if)
def draw():   
    global x
    draw_balloon(x, 200)
    x = x + 10
    if x > 500:
        x = 100
```

## PDF page 716

```text
27
Global variables
x = 100 # user defined
def draw():
    global x
    draw_balloon(x, 200)
    ...
```

## PDF page 717

```text
28
Global variables
def draw():
    global x
    draw_balloon(x, mouseY) 
# built-in
    x = x + 10
    if x > width: 
 
# built-in
        x = 100
```

## PDF page 718

```text
29
Question?
```

## PDF page 719

```text
30
Review Questions
```

## PDF page 720

```text
31
Another user defined Function
draw_balloon()
```

## PDF page 721

```text
32
User defined Function
def draw_circle(x, y, r):  # using radius?
    ...
```

## PDF page 722

```text
33
User defined Function
def draw_circle(x, y, r):
    ellipse(x,y, r*2, r*2)  
    # call built-in function, ellipse()
    # with appropriate parameters
    # effectively drawing a circle with radius r
```

## PDF page 723

```text
34
Use it in our function 
def draw_balloon(x, y):
    ellipse(x, y, 100, 100)    # replace it? 
    line(x, y+50, x, y+200)
```

## PDF page 724

```text
35
Use it in our function 
def draw_balloon(x, y):
    draw_circle(x,y, 50)
   # easier to understand?
    line(x, y+50, x, y+200)
```

## PDF page 725

```text
36
Use it in another function 
def draw_balloon(x, y):
    # ellipse(x, y, 100, 100)    # replace it 
    draw_circle(x,y, 50)
   # easier to understand?
    line(x, y+50, x, y+200)
```

## PDF page 726

```text
37
To try and use it in other functions
draw_bike()
draw_donut()
draw_target() # bullseye
draw_snowman()
draw_ladybug()
draw_smiley_face()
...
```

## PDF page 727

```text
38
```

## PDF page 728

```text
39
Built-in Function
# Python Mode for Processing
●
line()
●
ellipse()
●
background()
# Python
●
print()
```

## PDF page 729

```text
40
Built-in Function
# Python Mode for Processing
●
line(5, 5, 5, 5)
●
ellipse(9, 9, 9 ,9)
●
background(11)
# Python
●
print("Hello")
# Output according to parameters
```

## PDF page 730

```text
41
random()
# Python Mode for Processing
●
random()
# Generates a random number 
# and return a value according to parameters
```

## PDF page 731

```text
42
random( )
    x = random(100,400)
# The function will return a value between 100 and 400
# and the return value will be assigned to x
```

## PDF page 732

```text
43
random( )
def draw():
    x = random(100,400) # random value of x
    y = random(150,350) # random value of y
```

## PDF page 733

```text
44
random( )
def draw():
    x = random(100,400) # random value of x
    y = random(150,350) # random value of y
    draw_circle(x,y,30)
```

## PDF page 734

```text
45
Raining?
def draw():
    x = random(100,400)
    y = random(150,350)
    draw_circle(x,y,30)
# Very fast, set frame rate by using frameRate(5)
# in setup()
```

## PDF page 735

```text
46
Function with return value
def draw():
    x = random(100,400) # assign it to a variable
    y = random(150,350) # (store it) , not print/show
    draw_circle(x,y, 30 )
```

## PDF page 736

```text
47
Function with return value
def draw():
    x = random(100,400) # assign it to a variable
    y = random(150,350) # (store it) , not print/show
    draw_circle(x,y, random(3,30) )  
# send it to another function :)
```

## PDF page 737

```text
48
...
```

## PDF page 738

```text
49
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    
# To calculate the distance between 2 points
# and return the result
# x1: The x-coordinate of the first point.
    # y1: The y-coordinate of the first point.
    # x2: The x-coordinate of the second point.
    # y2: The y-coordinate of the second point.
```

## PDF page 739

```text
50
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
# calculates the absolute difference 
#   between the x-coordinates of the two points
```

## PDF page 740

```text
51
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
# calculates the absolute difference 
#   between the x-coordinates of the two points
# abs() is a built-in function that returns 
# the absolute value of a number (makes it positive)
```

## PDF page 741

```text
52
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
    diffy = abs( y1-y2 )
# Similarly, calculates the absolute difference 
# between the y-coordinates
```

## PDF page 742

```text
53
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
    diffy = abs( y1-y2 )
    result = sqrt( diffx*diffx + diffy*diffy )
# Calculates the result
# using Pythagorean theorem : )
```

## PDF page 743

```text
54
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
    diffy = abs( y1-y2 )
    result = sqrt( diffx*diffx + diffy*diffy )
    return result
# Tell the function to return the value of result
# and exit the function
```

## PDF page 744

```text
55
Cal distance to mouse position
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
```

## PDF page 745

```text
56
Show distance using a line
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    line(x,200, x + d, 200)
```

## PDF page 746

```text
57
...
```

## PDF page 747

```text
58
Draw on the same side as the mouse
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    ?
```

## PDF page 748

```text
59
Draw on the same side as the mouse
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    if mouseX > x:
        line(x,200, x + d, 200)
    ?
```

## PDF page 749

```text
60
Draw on the same side as the mouse
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    if mouseX > x:
        line(x,200, x + d, 200)
    else:
        line(x,200, x - d, 200)
```

## PDF page 750

```text
61
Never draw on both sides?
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    if mouseX > x:
        line(x,200, x + d, 200)
    else:
        line(x,200, x - d, 200)
```

## PDF page 751

```text
62
Draw Flowchart?
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    if mouseX > x:
        line(x,200, x + d, 200)
    else:
        line(x,200, x - d, 200)
```

## PDF page 752

```text
63
...
```

## PDF page 753

```text
64
Is x positive?
```

## PDF page 754

```text
65
Is x negative?
```

## PDF page 755

```text
66
Is x zero?
```

## PDF page 756

```text
67
Draw Flowchart?
```

## PDF page 757

```text
68
Different Flowchart but the same result?
```

## PDF page 758

```text
69
...
```

## PDF page 759

```text
70
Nested conditional statement
```

## PDF page 760

```text
71
Nested conditional statement
Similar idea to parenthesis ()
```

## PDF page 761

```text
72
Nested conditional statement
Similar idea to parenthesis ()
 x = (a + b)
 y = ( (i + j) * ( i - a) / 5 )
```

## PDF page 762

```text
73
...
```

## PDF page 763

```text
74
To Try (and fix errors : )
show_info()  # showInfo() just explains what this program does
width = get_width()   # get width from user
length = get_length()  # get length from user
area = cal_area(width, length)  # calculate result
show_area(area)       # show result
show_area_in_SqWa(area)
```

## PDF page 764

```text
75
Lab 3
```

## PDF page 765

```text
76
...
```

## PDF page 766

```text
77
Ideas for A1
Animation & Interactive program
- Help to prepare for midterm exam : maths,    
     physics, english
```

## PDF page 767

```text
78
Ideas for A1
Animation & Interactive program
- Help to prepare for midterm exam : maths,    
     physics, english
- What you like or interested
Objective: Review programming fundamentals 
(variable, function, conditional, loop, array)
```

## PDF page 768

```text
79
...
```

## PDF page 769

```text
010123102 
Programming Fundamentals
```

## PDF page 770

```text
2
Check Attendance..
```

