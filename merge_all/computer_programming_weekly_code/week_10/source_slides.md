# Week 10 — Functions with return values and distance

Source PDF pages 639–691. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 639

```text
010123138 
Computer Programming
```

## PDF page 640

```text
2
Check Attendance..
```

## PDF page 641

```text
3
Review
```

## PDF page 642

```text
4
Simple conditional statement (if)
def draw():   
    global x
    draw_balloon(x, 200)
    x = x + 10
    if x > 500:
        x = 100
```

## PDF page 643

```text
5
Function with return value
def draw():
    x = random(100,400) # assign it to a variable
    y = random(150,350) # (store it) , not print/show
    draw_circle(x,y, random(3,30) )  
# send it to another function :)
```

## PDF page 644

```text
6
User defined Function with return value
def cal_distance(x1, y1, x2, y2):
    diffx = abs( x1-x2 )
    diffy = abs( y1-y2 )
    result = sqrt( diffx*diffx + diffy*diffy )
    return result
# Tell the function to return the value of result
# and exit the function
```

## PDF page 645

```text
7
Show distance using a line
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    line(x,200, x + d, 200)
```

## PDF page 646

```text
8
Draw on the same side as the 
mouse
def draw():
    ...
    draw_balloon(x, 200, 50)
    d = cal_distance(x, 200, mouseX, mouseY)
    
    if mouseX > x:
        line(x,200, x + d, 200)
    else:
        line(x,200, x - d, 200)
```

## PDF page 647

```text
9
Is x positive?
if (x > 0): 
    print("x is positive") 
 
if (x < 0):
    print("x is negative") 
 
if (x == 0):
    print("x is zero")
```

## PDF page 648

```text
10
Nested conditional statement
Similar idea to parenthesis ()
 x = (a + b)
 y = ( (i + j) * ( i - a) / 5 )
```

## PDF page 649

```text
11
Nested conditional statement
if (x > 0): 
    print("x is positive") 
else: 
    if (x < 0):
        print("x is negative") 
    else:
        print("x is zero")
```

## PDF page 650

```text
12
Nested conditional statement
if (x > 0): 
    print("x is positive") 
else: 
    if (x < 0):
        print("x is negative") 
    #else:  
        print("x is zero") 
# same result?
# draw flowchart?
# try and see on pythontutor.com
```

## PDF page 651

```text
13
Nested conditional statement
if (x > 0): 
    print("x is positive") 
else: 
    if (x < 0):
        print("x is negative") 
    #else:  
    print("x is zero") 
# same result?
# draw flowchart?
# try and see on pythontutor.com
```

## PDF page 652

```text
14
Question?
```

## PDF page 653

```text
15
Review Questions
```

## PDF page 654

```text
16
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

## PDF page 655

```text
17
Assessment
Lecture 10% consists of
- After class quizzes (individual)
- Task 1 (group work)
- Task 2 (group work)
(maybe adjusted)
```

## PDF page 656

```text
18
Assessment
Lecture 10% consists of
- Task 1 (group work)
   - find exercises (coding 
question) and write solution
   - create quizzes (google form)
w1 for group 1, w2 for group 2, ...
```

## PDF page 657

```text
19
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

## PDF page 658

```text
20
Ideas for A1
Animation & Interactive program
- Help to prepare for midterm exam : maths,    
     physics, english
- What you like or interested
Objective: Review programming fundamentals 
(variable, function, conditional, loop, array)
```

## PDF page 659

```text
21
...
```

## PDF page 660

```text
22
Variable
n = 5
print(n)
n = n - 1
print(n)
```

## PDF page 661

```text
23
Variable
n = 5
print(n)
n = n - 1
print(n)
# draw flowchart
```

## PDF page 662

```text
24
Variable
n = 5
print(n)
n = n - 1
print(n)
n = n - 1
print(n)
n = n - 1
print(n)
n = n - 1  # แปรเปลี่ยนไป
print(n)   # ผลลัพท์เปลี่ยนไป
```

## PDF page 663

```text
25
Conditional
n = 5
if (n > 0):
    print(n)
    n = n - 1
# draw flowchart
```

## PDF page 664

```text
26
Conditional
n = 5
if (n > 0):
    print(n)
    n = n - 1
if (n > 0):
    print(n)
    n = n - 1
```

## PDF page 665

```text
27
Conditional
n = 5
if (n > 0):
    print(n)
    n = n - 1
if (n > 0):
    print(n)
    n = n - 1
if (n > 0):
    print(n)
    n = n - 1
if (n > 0):
    print(n)
    n = n - 1
if (n > 0):
    print(n)
    n = n - 1
```

## PDF page 666

```text
28
Conditional
...
if (n > 0):
    print(n)
    n = n - 1
# more ?
if (n > 0):
    print("Yes, the condition is true")
    print(n)
    n = n - 1
else:
    print("Sorry, the condition is false")
```

## PDF page 667

```text
29
Conditional
...
# more ?
if (n > 0):
    print("Yes, the condition is true")
    print(n)
    n = n - 1
else:
    print("Sorry, the condition is false")
if (n > 0):
    print("Yes, the condition is true")
    print(n)
    n = n - 1
else:
    print("Sorry, the condition is false")
```

## PDF page 668

```text
30
Repeated statements
n = 5
if (n > 0):
    print(n)
    n = n - 1
...
if (n > 0):
    print(n)
    n = n - 1
```

## PDF page 669

```text
31
while statements
n = 5
while (n > 0):
    print(n)
    n = n - 1
```

## PDF page 670

```text
32
while statements
n = 5
while (n > 0):
    print(n)
    n = n - 1
# draw flowchart
```

## PDF page 671

```text
33
while statements
n = 5
# initialise
while (n > 0):  # condition
    print(n)
    n = n - 1   # update
# draw flowchart
```

## PDF page 672

```text
34
Infinite Loop
n = 5
# initialise
while (n > 0):  # condition
    print(n)
    # n = n - 1   # do not forget to update
```

## PDF page 673

```text
35
...
```

## PDF page 674

```text
36
Sum
sum from 1 to n
1+2+3+...
draw flowchart
sum = 0  # start
```

## PDF page 675

```text
37
Random (Text-mode)
import random
x = random.randint(-5, 5)
print(x)
if x < 0:
    print("x is negative")
else:
    print("x is not negative")
```

## PDF page 676

```text
38
Loop until
input/random and sum, until -1 is entered
draw flowchart
```

## PDF page 677

```text
39
Password
# input password (not show it)
import getpass
user_password = getpass.getpass("Enter your password: ")
if user_password == "secret123":
    print("Access granted :)")
else:
    print("Access denied!")
```

## PDF page 678

```text
40
Password
# add loop to limit number of tries
count = 0    # start
```

## PDF page 679

```text
41
House
print house, start with floor and wall,then roof?
  ^ 
 ^ ^
^   ^
|||||
|   |
|   |
|||||
```

## PDF page 680

```text
42
print_line()
def print_line(n):
    
    while (n > 0):
        print("*",end="")    # do not add a newline
        n = n - 1
    print()
  # add a newline
```

## PDF page 681

```text
43
...
```

## PDF page 682

```text
44
Loop : Fixed number
def draw_ladder(x,y,s):
```

## PDF page 683

```text
45
Change to vertical lines
draw_vertical_lines(int x1,int y1,int x2,int y2):
    int space = abs(x1-x2)/5
    while (x1 < x2):
        ...
```

## PDF page 684

```text
46
Change to vertical lines
draw_vertical_lines(int x1,int y1,int x2,int y2):
    int space = abs(x1-x2)/5
    while (x1 < x2):
        line(x1,y1 - 50, x1, y1 + 50)
        x1 = x1 + space
```

## PDF page 685

```text
47
Loop : Fixed number
def draw_rain_drops(n):
    i = 0;
    while (i < n):         
# draw n rain drops
        x = random(100,400)
        y = random(150,350)
        r = random(3,30)
        draw_circle(x,y,r)
        i = i + 1
```

## PDF page 686

```text
48
Loop : Until specified sum/volume
def draw_rain_drops_until(volume):
    sum = 0
    while (sum < volume):
        ... 
        # sum = sum + r; // simplified calculation for volume?
```

## PDF page 687

```text
49
Loop : Until specified condition
def draw_rain_drops_until_r_below(int value):
    r_flag = True; 
// use of flag
            
    while (r_flag){
        int x = (int) random(100,400)
                 int y = (int) random(150,350)
                 int r = (int) random(3,30)
        draw_circle(x,y,r)
        if ( r < value ):
            r_flag = False
```

## PDF page 688

```text
50
...
```

## PDF page 689

```text
51
Lab 4
```

## PDF page 690

```text
010123102 
Programming Fundamentals
```

## PDF page 691

```text
2
Check Attendance..
```

