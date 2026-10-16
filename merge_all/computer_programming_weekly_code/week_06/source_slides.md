# Week 06 — Text files and file processing

Source PDF pages 374–438. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 374

```text
010123138 
Computer Programming
```

## PDF page 375

```text
2
Check Attendance..
```

## PDF page 376

```text
3
Review
```

## PDF page 377

```text
4
Non-Volatile data
File on Storage (e.g. HDD/SSD)
- Persists without power, can be reused later
- Slower read/write speed 
  (compared to RAM)
```

## PDF page 378

```text
5
File Types
- Text File (e.g. .txt, .csv, .json, .html)
  They are human-readable, stored as characters (string)
- Binary File (e.g. .jpg, .mp3, .exe)
  for program to read
```

## PDF page 379

```text
6
File Operations
# Open a text file for reading ("r")
file = open("example.txt", "r")
# Read the entire content and print it
content = file.read()  # call a method 
print( content )  # Content is a string
# Always close the file when finished
file.close()
```

## PDF page 380

```text
7
with statement
with open("example.txt", "r") as file:
    content = file.read()
    print( content )
# Recommended Way
# The file will be automatically closed
```

## PDF page 381

```text
8
while the line is not empty
with open("example.txt", "r") as f:
    line = f.readline()   # Read a line from file
    while line :
        print( line )
 # print it
        ...
```

## PDF page 382

```text
9
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

## PDF page 383

```text
10
for (each) loop
with open("example.txt", "r") as file:
    for line in file:    # for each line in file
```

## PDF page 384

```text
11
Print line-by-line
with open("example.txt", "r") as file:
    for line in file:    # for each line in file
        print( line )    # print it
# Loop condition ?
```

## PDF page 385

```text
12
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

## PDF page 386

```text
13
Process a line
a = [] # start from empty list
with open("example.txt", "r") as file:
    for line in file:
        # process and append to array
# string exercise?
# [5, 2, 7]
        
5,2,7
```

## PDF page 387

```text
14
Process a line
- Find a word in file
# string exercise?
```

## PDF page 388

```text
15
Write to file
with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")
# similar to print()?
# must add newline (\n) manually
```

## PDF page 389

```text
16
Write values of Array
with open("output.txt", "w") as file:
    ...
# exercise
```

## PDF page 390

```text
17
Invalid data from file
- String processing?
  isalpha(), isdigit(), is..?
```

## PDF page 391

```text
18
...
```

## PDF page 392

```text
19
Array of variables
a = [ 5, 9, 2 ]
# Python use "list" (similar but not the same as array)
# from this example: size or length is 3 
# index start from 0 (up to 2)
index
element
```

## PDF page 393

```text
20
Print elements of Array
a = [ 5, 9, 2 ]
i = 0  # index
while ( i < len(a)):  # len(a) is length of a
    print( a[i] )     # print element at i
    i = i + 1
```

## PDF page 394

```text
21
Function and Array
def print_all(a):
    i = 0  # index
    while ( i < len(a)):  # len(a) is length of a
        ...               # print element at i
        i = i + 1
a = [ 5, 9, 2 ]
...  # call the function
```

## PDF page 395

```text
22
Function and Array
def print_all(a):
    i = 0  # index
    while ( i < len(a)):  # len(a) is length of a
        print( a[i] )     # print element at i
        i = i + 1
a = [ 5, 9, 2 ]
print_all(a)
```

## PDF page 396

```text
23
Function and Array
a = [ 5, 9, 2 ]
print_all(a)
b = [ 6, 1, 8 ]
print_all(b)
```

## PDF page 397

```text
24
Function and Array
def add_all(a, x):
    i = 0  # index
    while ( i < len(a)):  # len(a) is length of a
        a[i] = a[i] + x   # add x to a[i]
        i = i + 1
a = [ 5, 9, 2 ]
add_all(a, 3)
# pass by reference?
print_all(a)
```

## PDF page 398

```text
25
Function and Array
a = [ 5, 9, 2 ]
add_all(a, 3)
print_all(a)
# can change elements in a
b = [ 6, 1, 8 ]
add_all(b, 2)
print_all(b)       # can change elements in b
```

## PDF page 399

```text
26
Pass by value
def add_x(a, x):
    a = a + x
a = 5
add_x(a, 3)
print(a)
```

## PDF page 400

```text
27
Pass by value
def add_x(a, x):
    a = a + x
a = 5
add_x(a, 3)
print(a)
# value of a is unchanged
```

## PDF page 401

```text
28
Pass by value
def add_x(a, x):
    a = a + x
b = 2
add_x(b, 7)
print(b)
# value of b is unchanged
```

## PDF page 402

```text
29
Pass by value
def add_x(a, x):
    a = a + x
b = 2
add_x(b, 7)        # value of b is copied to a
print(b)
# b is unchanged
                   # try on pythontutor.com
```

## PDF page 403

```text
30
Need a Volunteer
```

## PDF page 404

```text
31
2D Array
# 1D array (list of elements)
a = [ 3, 8, 2 ]
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ]
```

## PDF page 405

```text
32
2D Array
# 1D array (list of elements)
a = [ 3, 8, 2 ]
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ] 
#          m[0]         m[1]         m[2]
```

## PDF page 406

```text
33
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ]
```

## PDF page 407

```text
34
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ]
```

## PDF page 408

```text
35
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ] 
print( m[0][0] )
print( m[0][1] )
print( m[1][0] )
```

## PDF page 409

```text
36
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ] 
print( m[0][0] )  # 5   use 2 indexes (row,col)
print( m[0][1] )  # 7
print( m[1][0] )  # 2
```

## PDF page 410

```text
37
2D Array
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], \
      [ 2, 4, 6 ], \
      [ 8, 3, 1 ] ] 
print( m[1][1] )     # use 2 indexes (row,col)
print( m[2][2] )  
print( m[1][2] )
```

## PDF page 411

```text
38
2D Array
# 2D array (list of lists)
# use 2 indexes (row,col)
m[1][2] = 7
m[2][2] = 5
```

## PDF page 412

```text
39
2D Array
# 1D array (list of elements)
a = [ 3, 8, 2 ]
# 2D array (list of lists)
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ] 
#          m[0]         m[1]         m[2]
```

## PDF page 413

```text
40
Array of Arrays
def print_all(a):      # same as before (for 1D array)
    i = 0  # index
    while ( i < len(a)):  
        print( a[i] )
        i = i + 1
print_all( m[1] )  # send an array, m[1]
```

## PDF page 414

```text
41
Array of Arrays
# print every element
print_all( m[0] )
print_all( m[1] )
print_all( m[2] )
```

## PDF page 415

```text
42
Array of Arrays
# print every element
print_all( m[0] )
print_all( m[1] )
print_all( m[2] )
# need a loop?
```

## PDF page 416

```text
43
Array of Arrays
def print_2D(m):      
    i = 0  # index
    while ( i < len(m)):  
        ...
        i = i + 1
print_2D( m )  # send an array, m
```

## PDF page 417

```text
44
Array of Arrays
def print_2D(m):      
    i = 0  # index
    while ( i < len(m)):  
        print_all( m[i] )  # send an array, m[i]
        i = i + 1
print_2D( m )  # send an array, m
```

## PDF page 418

```text
45
Array of Arrays
def print_2D(m):      
    i = 0  # index
    while ( i < len(m)):   # loop
        print_all( m[i] )  # another loop?
        i = i + 1
print_2D( m )  # send an array, m
```

## PDF page 419

```text
46
Nested Loop
def print_2Dn(m):      
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( ... )):   # inner loop
            print( ... )
            j = j + 1
        i = i + 1
```

## PDF page 420

```text
47
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

## PDF page 421

```text
48
Sum
def sum_2Dn(m):
    ...      
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( m[i] )):   # inner loop
            ...
            j = j + 1
        i = i + 1
    ...
```

## PDF page 422

```text
49
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

## PDF page 423

```text
50
Sum
m = [ [ 5, 7, 9 ], [ 2, 4, 6 ], [ 8, 3, 1 ] ] 
print( sum_2Dn(m) )
```

## PDF page 424

```text
51
Count
def count_2Dn(m , x):
    ...
    i = 0  # index
    while ( i < len(m)):   # outer loop
        j = 0
        while ( j < len( m[i] )):   # inner loop
            ...
            ...
            j = j + 1
        i = i + 1
    ...
```

## PDF page 425

```text
52
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

## PDF page 426

```text
53
...
```

## PDF page 427

```text
54
Algorithms
1D Array
- find max/min/sum/avg
- find element/index (linear/binary search)
- count occurrences
- check array is sorted
- sort array (bubble sort?)
```

## PDF page 428

```text
55
Algorithms
2D Array
- find max/min/sum/avg (all/row/col)
- find element/index (all/row/col)
- count occurrences (all/row/col)
- check array is sorted ?
```

## PDF page 429

```text
56
Algorithms
- Can we use a 2D array 
   to keep the history of a 1D array being sorted?
```

## PDF page 430

```text
57
...
```

## PDF page 431

```text
58
Matrix
A = [[1, 2],\
     [3, 4]]
B = [[5, 6],\
     [7, 8]]
# can use 2D array?
```

## PDF page 432

```text
59
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

## PDF page 433

```text
60
A = [[1, 2],\
     [3, 4]]
B = [[5, 6],\
     [7, 8]]
print( addm(A, B) )
# Try and see on pythontutor.com
Add 2 Matrices
```

## PDF page 434

```text
61
Multi-dimension Array
# 2D array (list of lists)
# use 2 indexes (row,col)
# 3D array ...
# use ... indexes
```

## PDF page 435

```text
62
Multi-dimension Array
# 2D array (list of lists)
# use 2 indexes (row,col)
# 3D array (list of 2D array :)
# use 3 indexes ( i, j, k ?)
```

## PDF page 436

```text
63
Multi-dimension Array
# 2D array (list of lists)
# use 2 indexes (row,col)
# 3D array (list of 2D array :)
# use 3 indexes ( i, j, k ?)
# 4D ?
```

## PDF page 437

```text
64
Multi-dimension Array
# do not need to be 3 x 3 x 3
# 2 x 3 x 3 ?
```

## PDF page 438

```text
65
...
```

