# Week 08 — Functions, sum ranges and fixed-count loops

Source PDF pages 495–563. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 495

```text
010123138 
Computer Programming
```

## PDF page 496

```text
2
Check Attendance..
```

## PDF page 497

```text
3
Review
```

## PDF page 498

```text
4
Sum from 1 to n
n = 5
sum = 0
count = 1
while count <= n:
    sum = sum + count
    count = count + 1
print("Sum =", sum)
```

## PDF page 499

```text
5
Define a function
def sum_1_to_n( n ):
    sum = 0
    count = 1
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum
```

## PDF page 500

```text
6
Call the function
n = 5
print("Sum from 1 to",n,"=", sum_1_to_n( n ))
n = 10
print("Sum from 1 to",n,"=", sum_1_to_n( n ))
```

## PDF page 501

```text
7
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

## PDF page 502

```text
8
sum m to n
def sum_m_to_n( m, n ):
    sum = 0
    count = ...
```

## PDF page 503

```text
9
sum m to n
def sum_m_to_n( m, n ):
    sum = 0
    count = m
    while count <= n:
        ...
    return sum
```

## PDF page 504

```text
10
sum m to n
def sum_m_to_n( m, n ):
    sum = 0
    count = m
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum
```

## PDF page 505

```text
11
Loop : Fixed number
def draw_stairs(x,y,s):
      _
    _|
  _|
_|
# text-mode or graphic-mode
```

## PDF page 506

```text
12
...
```

## PDF page 507

```text
13
Array of variables
a = [ 5, 9, 2 ]
# Python use "list" (similar but not the same as array)
# from this example: size or length is 3 
# index start from 0 (up to 2)
index
element
```

## PDF page 508

```text
14
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print( a[i] )     # print element at i
    i = i + 1
```

## PDF page 509

```text
15
Sum elements of Array
a = [ 5, 9, 2 ]
sum = 0
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    sum = sum + a[i]  # element at index i
    i = i + 1
# draw flowchart
```

## PDF page 510

```text
16
Average?
a = [ 5, 9, 2 ]
sum = 0
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    sum = sum + a[i]  # element at index i
    i = i + 1
print( sum/len(a) )
```

## PDF page 511

```text
17
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 0  # index
while ( i < len(a)):  
    ...
        ...
    i = i + 1
```

## PDF page 512

```text
18
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 0  # index
while ( i < len(a)):  
    if max < a[i]:
        max = a[i]
    i = i + 1
```

## PDF page 513

```text
19
Maximum value?
a = [ 5, 9, 2 ]
max = a[0]
i = 1  # index can start from 1?
while ( i < len(a)):  
    if max < a[i]:
        max = a[i]
    i = i + 1
```

## PDF page 514

```text
20
is_sorted?
a = [ 5, 9, 2 ]
i = 0
while ( i < ... ):  
    if a[i] < a[i+1]:
        ...
    i = i + 1
```

## PDF page 515

```text
21
is_sorted?
a = [ 5, 9, 2 ]
i = 0
while ( i < (len(a)-1) ):  
    if a[i] < a[i+1]:
        ...
    i = i + 1
```

## PDF page 516

```text
22
is_sorted?
a = [ 5, 9, 2 ]
i = 0
while ( i < (len(a)-1) ):  
    if a[i] > a[i+1]: # ?
        ...
    i = i + 1
```

## PDF page 517

```text
23
Algorithms
- find max
- check array is sorted
- sort array?
- calculate factorial
```

## PDF page 518

```text
24
...
```

## PDF page 519

```text
25
Parallel Arrays
x = [ 1, 4, 2, 9, 3 ]
y = [ 5, 3, 1, 7, 2 ]
# what could they be?
```

## PDF page 520

```text
26
Parallel Arrays
def draw():
    i = 0
    while ( i < len(x)):  
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + 2
        i = i + 1
```

## PDF page 521

```text
27
Start from empty list
n = 10
x = [ ]
y = [ ]
```

## PDF page 522

```text
28
Add (append) element
def setup():
    size(1000,1000)
    i = 0
    while ( i < n ):  
        x.append( random(100,900) )
        y.append( random(100,500) ) 
        i = i + 1
```

## PDF page 523

```text
29
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

## PDF page 524

```text
30
Add speed
def draw():
    background(255)
    i = 0
    while ( i < n ):  
        draw_circle( x[i], y[i], 20)
        y[i] = y[i] + s[i]
        i = i + 1
```

## PDF page 525

```text
31
more Parallel Arrays
id = [ 001, 007, 199 ]
health = [100, 70, 80]
score = [50, 120, 90]
```

## PDF page 526

```text
32
more Parallel Arrays
product = ["Apple", "Banana", "Orange"]
price = [1.20, 0.80, 1.50]
stock = [30, 50, 20]
```

## PDF page 527

```text
33
Question?
```

## PDF page 528

```text
34
Review Questions
```

## PDF page 529

```text
35
...
```

## PDF page 530

```text
36
String
s = "Hello"  # string of characters
```

## PDF page 531

```text
37
String
s = "Hello"  # string of characters
print(s)    # display string in text mode
```

## PDF page 532

```text
38
String
s = "Hello"  # similar to array of characters
i = 0
while(i < len(s)):  # can use the same loop?
    print( ... )
    i = i + 1
```

## PDF page 533

```text
39
String
s = "Hello"  # similar to array of characters
i = 0
while(i < len(s)):
    print( s[i] )
    i = i + 1
H
e
l
l
o
```

## PDF page 534

```text
40
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

## PDF page 535

```text
41
ASCII code
s = "Hello"  # similar to array of characters
i = 0
while(i < len(s)):
    print( ord(s[i]) )
    i = i + 1
# In Python, a character is a string of length one
# but not in Java or C
72
101
108
108
111
```

## PDF page 536

```text
42
ASCII code
print( ord("a") )  # Output: 97
print( ord('a') )  # same in Python
# single and double quotes give the same string 
# but in many languages, 'a' is a character (not string)
```

## PDF page 537

```text
43
ASCII code
print( ord('a') )  # Output: 97
print( ord('A') )  # Output: 65
# see https://en.wikipedia.org/wiki/ASCII
```

## PDF page 538

```text
44
ASCII code
print( ord('a') )  # Output: 97
print( ord('A') )  # Output: 65
print( ord('0') )  # Output: 48
print( ord(0) )    # TypeError: ord() expected string of length 1, but int found
```

## PDF page 539

```text
45
ASCII code
print( chr(97) )    # Output a
# reverse of ord()
```

## PDF page 540

```text
46
ASCII code
print( chr(97) )    # Output a
print( chr(65) )    # Output A
```

## PDF page 541

```text
47
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

## PDF page 542

```text
48
String Concatenation ( + )
s = "Hello"  
t = "Joe"
print( s + t )
```

## PDF page 543

```text
49
String Concatenation ( + )
s = "Hello"
t = ""     # t is an empty string
i = 0
while(i < len(s)):   # loop
    ...
    i = i + 1
```

## PDF page 544

```text
50
String Concatenation ( + )
s = "Hello"
t = ""     
i = 0
while(i < len(s)):
    t = t + str(i)  # add i to t ?   str() will convert integer to string
    i = i + 1
```

## PDF page 545

```text
51
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

## PDF page 546

```text
52
String Concatenation ( + )
s = "Hello"
t = ""     
i = 0
while(i < len(s)):
    t = t + str(i) + s[i] + "\n"
    i = i + 1
print( t )
0H
1e
2l
3l
4o
```

## PDF page 547

```text
53
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

## PDF page 548

```text
54
Display String (graphic-mode)
def draw():
    fill(0)
# text color
    textSize(100)  # text size :)
    text("ABC", mouseX, mouseY)
```

## PDF page 549

```text
55
...
```

## PDF page 550

```text
56
Array is mutable
a = [ 5, 9, 2 ]
a[0] = 7
Can change element in array
```

## PDF page 551

```text
57
String is immutable
s = "Hello"
s[0] = "J"   # Error
# TypeError: 'str' object does not support item assignment
# Cannot change element in array
```

## PDF page 552

```text
58
Create a new string
s = "Hello"
s = "J" + s[4] + s[1]
# Assign it to the same variable
```

## PDF page 553

```text
59
Create a new string
s = "Hello"
s = "J" + s[4] + s[1]
# Assign it to the same variable   
# Similar to earlier example
# t = t + str(i) + "\t" + s[i] + "\n"
```

## PDF page 554

```text
60
String Method (Function)
s = "Hello"
print( s.upper() )
# Call function in a different way
# variable_name.function_name()   
HELLO
```

## PDF page 555

```text
61
String Method (Function)
s = "Hello"
print( s.lower() )
hello
```

## PDF page 556

```text
62
String Method (Function)
s = "A"
print( s.isalpha() )
True
```

## PDF page 557

```text
63
String Method (Function)
s = "3"
print( s.isalpha() )
# boolean function
False
```

## PDF page 558

```text
64
String Method (Function)
s = "3"
print( s.isdigit() )
True
```

## PDF page 559

```text
65
String Method (Function)
s = "3"
print( s.isalnum() )
# See
# https://py.processing.org/reference/string
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# (not the main focus)
True
```

## PDF page 560

```text
66
...
```

## PDF page 561

```text
67
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

## PDF page 562

```text
68
Ideas for A1
Animation & Interactive program
- Help to prepare for midterm exam : maths,    
     physics, english
- What you like or interested
Objective: Review programming fundamentals 
(variable, function, conditional, loop, array)
```

## PDF page 563

```text
69
Lab 6
```

