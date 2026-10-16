# Week 09 — Conditionals, while loops and accumulation

Source PDF pages 564–638. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 564

```text
010123138 
Computer Programming
```

## PDF page 565

```text
2
Check Attendance..
```

## PDF page 566

```text
3
Review
```

## PDF page 567

```text
4
Is x positive?
if (x > 0): 
    print("x is positive") 
 
if (x < 0):
    print("x is negative") 
 
if (x == 0):
    print("x is zero")
```

## PDF page 568

```text
5
Nested conditional statement
if (x > 0): 
    print("x is positive") 
else: 
    if (x < 0):
        print("x is negative") 
    else:
        print("x is zero")
```

## PDF page 569

```text
6
while statements
n = 5
while (n > 0):
    print(n)
    n = n - 1
# draw flowchart
```

## PDF page 570

```text
7
while statements
n = 5
# initialise
while (n > 0):  # condition
    print(n)
    n = n - 1   # update
# draw flowchart
```

## PDF page 571

```text
8
Infinite Loop
n = 5
# initialise
while (n > 0):  # condition
    print(n)
    # n = n - 1   # do not forget to update
```

## PDF page 572

```text
9
Sum from 1 to n
n = 5
sum = 0
count = 1
while count <= n:
    sum = sum + count
    count = count + 1
print("Sum =", sum)
```

## PDF page 573

```text
10
Define a function
def sum_1_to_n( n ):
    sum = 0
    count = 1
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum
```

## PDF page 574

```text
11
Call the function
n = 5
print("Sum from 1 to",n,"=", sum_1_to_n( n ))
n = 10
print("Sum from 1 to",n,"=", sum_1_to_n( n ))
```

## PDF page 575

```text
12
define main()
# do not need global variables
# try and see on pythontutor.com
def main():
    n = 5
    print("Sum from 1 to",n,"=", sum_1_to_n( n ))
    n = 10
    print("Sum from 1 to",n,"=", sum_1_to_n( n ))
if __name__ == "__main__":
    main()
```

## PDF page 576

```text
13
Loop : Fixed number
def draw_ladder(x,y,s):
```

## PDF page 577

```text
14
Change to vertical lines
draw_vertical_lines(int x1,int y1,int x2,int y2):
    int space = abs(x1-x2)/5
    while (x1 < x2):
        line(x1,y1 - 50, x1, y1 + 50)
        x1 = x1 + space
```

## PDF page 578

```text
15
Change to vertical lines
draw_vertical_lines(int x1,int y1,int x2,int y2):
    int space = abs(x1-x2)/5  # integer division?
    while (x1 < x2):
        line(x1,y1 - 50, x1, y1 + 50)
        x1 = x1 + space
```

## PDF page 579

```text
16
Change to vertical lines
draw_vertical_lines(int x1,int y1,int x2,int y2):
    int space = abs(x1-x2)/5  # integer division in many programming lanagues
    while (x1 < x2):
        line(x1,y1 - 50, x1, y1 + 50)
        x1 = x1 + space
# if space is zero?
```

## PDF page 580

```text
17
Loop : Fixed number
def draw_rain_drops(n):
    i = 0;
    while (i < n):         # draw n rain drops
        x = random(100,400)
        y = random(150,350)
        r = random(3,30)
        draw_circle(x,y,r)
        i = i + 1
```

## PDF page 581

```text
18
Loop : Until specified sum/volume
def draw_rain_drops_until(volume):
    sum = 0
    while (sum < volume):
        ... 
        # sum = sum + r; // simplified calculation for volume?
```

## PDF page 582

```text
19
Loop : Until specified condition
def draw_rain_drops_until_r_below(int value):
    r_flag = True; // use of flag
           
 
    while (r_flag)
                 int x = (int) random(100,400)
                 int y = (int) random(150,350)
                 int r = (int) random(3,30)
        draw_circle(x,y,r)
        if ( r < value ):
            r_flag = False
```

## PDF page 583

```text
20
Question?
```

## PDF page 584

```text
21
Review Questions
```

## PDF page 585

```text
22
...
```

## PDF page 586

```text
23
Sum from 1 to n
n = 5
sum = 0
count = 1
while count <= n:
    sum = sum + count
    count = count + 1
print("Sum =", sum)
```

## PDF page 587

```text
24
Sum many variables
...
sum = 0
sum = sum + x
sum = sum + y
sum = sum + z
...
# 3 variables ok
# 5, 10, ..?
```

## PDF page 588

```text
25
Array of variables
a = [ 5, 9, 2 ]
...
sum = 0
sum = sum + x
sum = sum + y
sum = sum + z
...
```

## PDF page 589

```text
26
Array of variables
a = [ 5, 9, 2 ]
# Python use "list" (similar but not the same as array)
# image from pythontutor.com
```

## PDF page 590

```text
27
Array of variables
a = [ 5, 9, 2 ]
# Python use "list" (similar but not the same as array)
# from this example: size or length is 3 
# index start from 0 (up to 2)
index
element
```

## PDF page 591

```text
28
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
element
index
```

## PDF page 592

```text
29
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
# can i start from ...?
element
index
```

## PDF page 593

```text
30
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print( a[i] )     # print element at i
    i = i + 1
```

## PDF page 594

```text
31
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print( a[i] )     # print element at i
    i = i + 1
# draw flowchart
```

## PDF page 595

```text
32
Show index
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print("a[", i , "] = ", a[i]);
    i = i + 1
# draw flowchart
```

## PDF page 596

```text
33
...
```

## PDF page 597

```text
34
Sum elements of Array
a = [ 5, 9, 2 ]
...
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    ...
    i = i + 1
# draw flowchart
```

## PDF page 598

```text
35
Sum elements of Array
a = [ 5, 9, 2 ]
sum = 0  # as before
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    ...
    i = i + 1
# draw flowchart
```

## PDF page 599

```text
36
Sum elements of Array
a = [ 5, 9, 2 ]
sum = 0
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    sum = sum + ...
    i = i + 1
# draw flowchart
```

## PDF page 600

```text
37
Sum elements of Array
a = [ 5, 9, 2 ]
sum = 0
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    sum = sum + a[i]  # element at index i
    i = i + 1
# draw flowchart
```

## PDF page 601

```text
38
...
```

## PDF page 602

```text
39
Average?
a = [ 5, 9, 2 ]
sum = 0
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    sum = sum + a[i]  # element at index i
    i = i + 1
# draw flowchart
```

## PDF page 603

```text
40
Problem Solving
Find the maximum of 2 values
```

## PDF page 604

```text
41
Problem Solving
Find the maximum of 2 values 
if-else?
```

## PDF page 605

```text
42
Problem Solving
Find the maximum of 3 values
```

## PDF page 606

```text
43
Problem Solving
Find the maximum of 3 values 
more if-else?
```

## PDF page 607

```text
44
Problem Solving
Find the maximum of 3 values
tmp = max of the first 2 values
result = max of tmp and the third value
```

## PDF page 608

```text
45
Problem Solving
Find the maximum of 4 values
tmp = max of the first 2 values
tmp2 = max of tmp and the third value
result = max of tmp2 and the forth value
```

## PDF page 609

```text
46
Problem Solving
Can only compare 2 values at a time?
```

## PDF page 610

```text
47
Maximum value?
a = [ 5, 9, 2 ]
max = ...
# start from the fist element?
```

## PDF page 611

```text
48
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = ...
# start from the fist element?
```

## PDF page 612

```text
49
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 0  # index
while ( i < len(a)):  
    ...
        ...
    i = i + 1
```

## PDF page 613

```text
50
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 0  # index
while ( i < len(a)):  
    if max < a[i]:
        max = a[i]
    i = i + 1
```

## PDF page 614

```text
51
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 1  # index can start from 1?
while ( i < len(a)):  
    if max < a[i]:
        max = a[i]
    i = i + 1
```

## PDF page 615

```text
52
Buit-in function
# for debug
# not in exam : )
print( a )
print( sum(a) )
print( max(a) )
```

## PDF page 616

```text
53
...
```

## PDF page 617

```text
54
Parallel Arrays
x = [ 1, 4, 2, 9, 3 ]
y = [ 5, 3, 1, 7, 2 ]
# what could they be?
```

## PDF page 618

```text
55
Parallel Arrays
def draw():
    i = 0
    while ( i < len(x)):
        ...
        i = i + 1
```

## PDF page 619

```text
56
Parallel Arrays
def draw():
    i = 0
    while ( i < len(x)):  
        draw_circle( x[i], y[i], 20)
        ...
        i = i + 1
```

## PDF page 620

```text
57
Parallel Arrays
def draw():
    i = 0
    while ( i < len(x)):  
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + 2
        ...
        i = i + 1
```

## PDF page 621

```text
58
Parallel Arrays
def draw():
    i = 0
    while ( i < len(x)):  
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + 2
        x[i] = x[i] + 2 # need it?
        i = i + 1
```

## PDF page 622

```text
59
...
```

## PDF page 623

```text
60
Start from empty list
n = 10
x = [ ]
y = [ ]
```

## PDF page 624

```text
61
Add (append) element
def setup():
    size(1000,1000)
    i = 0
    while ( i < n ):  
        x.append( random(100,900) )
        y.append( random(100,500) ) 
        i = i + 1
```

## PDF page 625

```text
62
Change n
n = ...
x = [ ]
y = [ ]
```

## PDF page 626

```text
63
Add speed
n = 108
x = [ ]
y = [ ]
s = [ ]
```

## PDF page 627

```text
64
Add speed
def setup():
    size(1000,1000)
    i = 0
    while ( i < n ):  
        x.append( random(100,900) )
        y.append( random(100,500) )
        s.append( random(1,5) ) 
        i = i + 1
```

## PDF page 628

```text
65
Add speed
def draw():
    background(255)
    i = 0
    while ( i < n ):  
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + s[i]
        i = i + 1
```

## PDF page 629

```text
66
Add?
- Animation
- Interaction
```

## PDF page 630

```text
67
more Parallel Arrays
id = [ 001, 007, 199 ]
health = [100, 70, 80]
score = [50, 120, 90]
```

## PDF page 631

```text
68
more Parallel Arrays
product = ["Apple", "Banana", "Orange"]
price = [1.20, 0.80, 1.50]
stock = [30, 50, 20]
```

## PDF page 632

```text
69
...
```

## PDF page 633

```text
70
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

## PDF page 634

```text
71
Assessment
Lecture 10% consists of
- After class quizzes (individual)
- Task 1 (group work)
- Task 2 (group work)
(maybe adjusted)
```

## PDF page 635

```text
72
Assessment
Lecture 10% consists of
- Task 1 (group work)
   - find exercises (coding 
question) and write solution
   - create quizzes (google form)
w1 for group 1, w2 for group 2, ...
```

## PDF page 636

```text
73
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

## PDF page 637

```text
74
Ideas for A1
Animation & Interactive program
- Help to prepare for midterm exam : maths,    
     physics, english
- What you like or interested
Objective: Review programming fundamentals 
(variable, function, conditional, loop, array)
```

## PDF page 638

```text
75
Lab 5
```

