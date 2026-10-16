# Week 12 — Programming fundamentals, drawing, function calls and labs

Source PDF pages 771–863. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 771

```text
3
Review
```

## PDF page 772

```text
4
Start from Output ?
Input  
→Process  Output
→
```

## PDF page 773

```text
5
Start from Output
print("Hello, World") 
●
To check that installed program works correctly
●
also verify that it can follow instruction 
and give feedback   Hello, World
Hello, World
```

## PDF page 774

```text
6
Simple Output
size(500,500)
line(250,250,0,0) 
line(250,250,500,0) 
line(250,250,250,500)
```

## PDF page 775

```text
7
Different code, same Output
size(500,500)
line(250,250,250,500) # |
line(250,250,500,0) # /
line(250,250,0,0) # \
size(500,500)
line(250,250,500,0) # /
line(250,250,250,500) # |
line(250,250,0,0) # \
```

## PDF page 776

```text
8
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300)
```

## PDF page 777

```text
9
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300)
```

## PDF page 778

```text
10
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter N
```

## PDF page 779

```text
11
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter H
```

## PDF page 780

```text
12
Use Variables
size(500,500)
x = 200 # upper left x
y = 100 # upper left y
line(x, y, x, y+200)
line(x+100, y, x+100, y+200)
# to draw letter H
```

## PDF page 781

```text
13
Use Variables
size(500,500)
x = 200 # upper left x
y = 100 # upper left y
line(x, y, x, y+200)
line(x+100, y, x+100, y+200)
middle = y + 100
line(x,middle,x+100,middle)
```

## PDF page 782

```text
14
Built-in Function
# Python Mode for Processing
●
line()
●
ellipse()
# Python
●
print()
```

## PDF page 783

```text
15
Question?
```

## PDF page 784

```text
16
Lab1 submission
check that you submitted 
the correct URL
:)
```

## PDF page 785

```text
17
Review Questions
```

## PDF page 786

```text
18
...
```

## PDF page 787

```text
19
draw Ball
# Python Mode for Processing
●
line()
●
ellipse()
ellipse(200,200,100,100)
```

## PDF page 788

```text
20
draw Balloon
ellipse(200,200,100,100)
line(200,250,200,400)
```

## PDF page 789

```text
21
Define draw_balloon()
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
```

## PDF page 790

```text
22
Define draw_balloon()
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
# user-defined function
```

## PDF page 791

```text
23
Define draw_balloon()
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
# user-defined function
# not built-in (built-eng :)
```

## PDF page 792

```text
24
Run the code
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
# will draw a ballon?
```

## PDF page 793

```text
25
Run the code
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
# nothing?
```

## PDF page 794

```text
26
Must call the function
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
# how?
```

## PDF page 795

```text
27
Call its name
def draw_balloon():
    ellipse(200,200,100,100)
    line(200,250,200,400)
draw_balloon()
# its name followed by ()
```

## PDF page 796

```text
28
Add parameter
def draw_balloon(x, y):
    ellipse(...)
    line(...)
draw_balloon(200, 200)
```

## PDF page 797

```text
29
When called, it will send arguments
def draw_balloon(x, y):
    ellipse(...)
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 798

```text
30
Back to called function
def draw_balloon(x, y):
   x = 200 # similar result
   y = 200
    ellipse(...)
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 799

```text
31
Back to called function
def draw_balloon(x, y):
   x = 200 # similar result
   y = 200
    ellipse(...) # ?
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 800

```text
32
Back to called function
def draw_balloon(x, y):
   x = 200 # similar result
   y = 200
    ellipse(x, y, 100, 100) 
 # use the sent argument
    line(...)
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 801

```text
33
Back to called function
def draw_balloon(x, y):
   x = 200 # similar result
   y = 200
    ellipse(x, y, 100, 100)    
    line(x, y+50, x, y+200)
 # here also
draw_balloon(200, 200)
# the values will be copied
```

## PDF page 802

```text
34
Call it twice
draw_balloon(200, 200)
draw_balloon(400, 200)
# What will be shown?
```

## PDF page 803

```text
35
Call it twice, get 2 balloons : )
draw_balloon(200, 200)
draw_balloon(400, 200)
```

## PDF page 804

```text
36
Call it twice, get 2 balloons : )
draw_balloon(200, 200)
draw_balloon(400, 200)
# only define a function  
   one time
```

## PDF page 805

```text
37
Animation with a balloon?
```

## PDF page 806

```text
38
Special functions in Processing
def setup():  # will be called 1 time
    size(500,500)
```

## PDF page 807

```text
39
Special functions in Processing
def setup():  # will be called 1 time
    size(500,500)
def draw():   # will be called repeatedly
    # can we proof that?
```

## PDF page 808

```text
40
Special functions in Processing
def setup():  # will be called 1 time
    size(500,500)
def draw():   # will be called repeatedly
    draw_ballon(200,200)
# does not work
```

## PDF page 809

```text
41
Special functions in Processing
def setup():  # will be called 1 time
    size(500,500)
def draw():   # will be called repeatedly
    global x
    draw_balloon(x, 200)
    x = x + 10
# still does not work?
```

## PDF page 810

```text
42
Simple conditional statement (if)
def draw():   # will be called repeatedly
    global x
    draw_balloon(x, 200)
    x = x + 10
    if x > 500:
        x = 100
```

## PDF page 811

```text
43
Global variables
# user-defined
x = 100
def draw():   # will be called repeatedly
    global x
    draw_balloon(x, 200)
    x = x + 10
    if x > 500:
        x = 100
```

## PDF page 812

```text
44
Global variables
x =100
def draw():   # will be called repeatedly
    global x
    draw_balloon(x, 200)
    x = x + 10
    if x > width: # built-in
        x = 100
```

## PDF page 813

```text
45
Global variables
x =100
def draw():   # will be called repeatedly
    global x
    draw_balloon(x, mouseY) # built-in
    x = x + 10
    if x > width: 
        x = 100
```

## PDF page 814

```text
46
...
```

## PDF page 815

```text
47
Text Mode
def show_info():
    print("This program will calculate area of a land")
    print("given width and length")
    print()
    print("created by <student name>")
show_info()
```

## PDF page 816

```text
48
Text Mode
def show_area( area ):
    print("The result area is", area, "(in square meter)")
show_area(100)
```

## PDF page 817

```text
49
To Try (and fix errors : )
show_info()  # showInfo() just explains what this program does
width = get_width()   # get width from user
length = get_length()  # get length from user
area = cal_area(width, length)  # calculate result
show_area(area)       # show result
show_area_in_SqWa(area)
```

## PDF page 818

```text
50
Lab2
```

## PDF page 819

```text
010123102 
Programming Fundamentals
```

## PDF page 820

```text
Hello and Welcome to KMUTNB
```

## PDF page 821

```text
Welcome to Computer Engineering
```

## PDF page 822

```text
4
What is "Engineering"?
```

## PDF page 823

```text
5
What is "Engineering"?
```

## PDF page 824

```text
6
What is "Computer" ?
```

## PDF page 825

```text
7
What is "Computer" ?
?
```

## PDF page 826

```text
8
Check Attendance..
●Need a volunteer
(youtuber?)
```

## PDF page 827

```text
9
Check Attendance..
●
To enter your counted number 
in google form
https://docs.google.com/forms/d/e/
1FAIpQLSdDTX0gqlpnfjRQ5j5kFaWiJevYc
7QujzeZdoD5ndBdv0RbEA/viewform?
usp=header
```

## PDF page 828

```text
10
What is "Programming" ?
```

## PDF page 829

```text
11
What is "Programming" ?
print("Hello, World") ?
```

## PDF page 830

```text
12
Why "Programming" ?
```

## PDF page 831

```text
13
How "Programming"?
```

## PDF page 832

```text
14
Start from Output ?
Input  
→Process  Output
→
```

## PDF page 833

```text
15
Start from Output
print("Hello, World")
```

## PDF page 834

```text
16
Start from Output
print("Hello, World") 
●
To check that installed program works correctly
●
also verify that it can follow instruction 
and give feedback   Hello, World
Hello, World
```

## PDF page 835

```text
17
Change the String
print("Hello, KMUTNB")
Hello, ... ?
```

## PDF page 836

```text
18
Change the String
print("Hello, KMUTNB")
●
Put what you want it to say inside   "  "
(quotation marks)
Hello, KMUTNB
```

## PDF page 837

```text
19
Do not like Text-mode ?
print("Hello, KMUTNB") 
# display characters only
Hello, KMUTNB
```

## PDF page 838

```text
20
How about Graphic-mode ?
https://processing.org
Processing is a flexible software 
sketchbook and a language for 
learning how to code.
To use:Python Mode for Processing
(more in lab1)
```

## PDF page 839

```text
21
Python Mode for Processing
https://py.processing.org
Write Python code to draw : )
    # --- Draw the head (large yellow 
circle) ---
    fill(YELLOW)
    stroke(BLACK)
    strokeWeight(2)
    circle(width / 2, height / 2, 200) # 
Center the head
    # --- Draw the left eye ---
    # White part of the eye
    fill(WHITE)
    stroke(BLACK)
    strokeWeight(2)
    circle(width / 2 - 80, height / 2 - 
50, 30)
```

## PDF page 840

```text
22
Simple Output
size(500,500)
line(0,0,250,250)
```

## PDF page 841

```text
23
Simple Output
size(500,500)
line(0,0,250,250)
```

## PDF page 842

```text
24
Simple Output
size(500,500)
line(0,0,250,250) 
line(250,250,250,500)
line(250,250,500,0)
```

## PDF page 843

```text
25
Simple Output
size(500,500)
line(0,0,250,250) 
line(250,250,250,500)
line(250,250,500,0)
```

## PDF page 844

```text
26
Different code, same Output
size(500,500)
line(250,250,250,500) # |
line(250,250,500,0) # /
line(0,0,250,250) # \
size(500,500)
line(250,250,500,0) # /
line(250,250,250,500) # |
line(0,0,250,250) # \
```

## PDF page 845

```text
27
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300)
```

## PDF page 846

```text
28
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300)
```

## PDF page 847

```text
29
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter N
```

## PDF page 848

```text
30
Simple Calculation
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter H
```

## PDF page 849

```text
31
Use Variables
size(500,500)
x = 200 # upper left x
y = 100 # upper left y
line(x, y, x, y+200)
line(x+100, y, x+100, y+200)
# to draw letter H
```

## PDF page 850

```text
32
Use Variables
size(500,500)
x = 200 # upper left x
y = 100 # upper left y
line(x, y, x, y+200)
line(x+100, y, x+100, y+200)
middle = y + 100
line(x,middle,x+100,middle)
```

## PDF page 851

```text
33
Use Variables
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter N
```

## PDF page 852

```text
34
Use Variables
size(500,500)
line(200,100,200,300)
line(300,100,300,300) 
# to draw letter U
```

## PDF page 853

```text
35
Try it online
# Goto https://trinket.io/processing
from processing import *
def setup():
    line(50,20,50,80)
    line(70,20,70,80)
    line(90,20,90,80)
run()
# need to modify the code
```

## PDF page 854

```text
36
Have you Scratched ?
# Goto https://scratch.mit.edu/
# no code
# drag and drop
```

## PDF page 855

```text
37
Can you C ?
#include <stdio.h>
int main() {
    printf("Hello, World");
}
```

## PDF page 856

```text
38
Break
```

## PDF page 857

```text
39
Lab
●2 hours weekly lab
●Dividing students into 2 
groups (odd/even counted number?)
●One group in the morning 
(9-11 am)
●Another group in the 
afternoon (1-3 pm)
●Lab is on level 3
(below this lecture room?)
```

## PDF page 858

```text
40
Lab1
●To be posted on google 
classroom
```

## PDF page 859

```text
41
Quick Quiz : )
```

## PDF page 860

```text
42
?
print("KMUT" + "NB")
```

## PDF page 861

```text
43
?
print("1" + "2")
```

## PDF page 862

```text
44
?
print(1 + 2)
```

## PDF page 863

```text
45
Review Questions
Later this week, check 
google classroom
class code: fzwp25m3
```

