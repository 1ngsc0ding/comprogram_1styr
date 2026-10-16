# Week 01 — Processing basics: output, coordinates, variables, functions, Java mode

Source PDF pages 1–97. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 1

```text
010123138 
Computer Programming
```

## PDF page 2

```text
2
Check Attendance..
```

## PDF page 3

```text
3
Need a Volunteer
```

## PDF page 4

```text
4
Hello Java
```

## PDF page 5

```text
5
Start with Java-mode Processing
```

## PDF page 6

```text
6
setup() in Python-mode
def setup():
    size(500, 500)
    ellipse(200,200,100,100)
    line(200,250,200,400)
```

## PDF page 7

```text
7
setup() in Java-mode
void setup() {
    size(500, 500);
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// “void” == “def” ?  (please wait)
```

## PDF page 8

```text
8
Same function?
void setup() {
    size(500, 500);
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// Java comment (use two slashes)
// The name of the function is setup()
```

## PDF page 9

```text
9
Same result?
void setup() {
    size(500, 500);
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// setup() works as before
```

## PDF page 10

```text
10
Semicolon ;
void setup() {
    size(500, 500);  // must put semicolon at the end
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
```

## PDF page 11

```text
11
Curly Brackets { }
void setup() {  // use { at the begin of block
    size(500, 500);
    ellipse(200,200,100,100);
    line(200,250,200,400);
}              // use } at the end of block
```

## PDF page 12

```text
12
Block of code
void setup() {  // use { at the begin of block
    size(500, 500);
    ellipse(200,200,100,100);
    line(200,250,200,400);
}              // use } at the end of block
// should also indent 4 spaces as in Python
```

## PDF page 13

```text
13
Java do not care about space/indent
void setup() {size(500, 
500);ellipse(200,200,100,100);line(200,250,200,400);
}
// Give the same result, but should not do it
```

## PDF page 14

```text
14
...
```

## PDF page 15

```text
15
User-defined function
void draw_balloon(){
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// “void” == “def” ?  (please wait a little more)
```

## PDF page 16

```text
16
Semicolon ;
void draw_balloon(){
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// same as earlier
```

## PDF page 17

```text
17
Curly Brackets { }
void draw_balloon(){
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// same as earlier
```

## PDF page 18

```text
18
Block of code
void draw_balloon(){
    ellipse(200,200,100,100);
    line(200,250,200,400);
}
// same as earlier
```

## PDF page 19

```text
19
Function Call
void setup(){
    size(500,500);
    draw_balloon();
}
  // Just call its name (as in Python)
  // and follow it with a semicolon
```

## PDF page 20

```text
20
Function Parameter
void draw_balloon(... x, ... y){
    // specify the name of parameter 
    ...
}
```

## PDF page 21

```text
21
Function Parameter
void draw_balloon(int x, int y){
    // specify the type 
    ...
}
```

## PDF page 22

```text
22
Function Parameter
void draw_balloon(int x, int y){
    // specify the type 
    // int == integer
    ...
}
```

## PDF page 23

```text
23
Function Parameter
void draw_balloon(int x, int y){
    ...
}
```

## PDF page 24

```text
24
Function Parameter
void draw_balloon(int x, int y){
    ellipse(x, y, 100, 100);
    line(x, y+50, x, y+200);
}
// as before
```

## PDF page 25

```text
25
Function Call
void setup(){
    size(500,500);
    draw_balloon( 200 , 200 );
}
// send arguments
// same concept
```

## PDF page 26

```text
26
Call it twice
void setup(){
    size(500,500);
    draw_balloon( 200 , 200 );
    draw_balloon( 400 , 300 );
}
   // send different arguments
   // same concept
```

## PDF page 27

```text
27
Call it twice
void setup(){
    size(500,500);
    draw_balloon( 200 , 200 );
    draw_balloon( 400 , 300 );
}
   // as expected
```

## PDF page 28

```text
28
Animation
What are needed?
```

## PDF page 29

```text
29
Animation
global variable
setup()
draw()
```

## PDF page 30

```text
30
Global Variable
int x=100;
   // must specify its type
   // similar to parameter
```

## PDF page 31

```text
31
Global Variable
int x=100;
   // must specify its type
   // similar to parameter
  // In native Java language 
  // global variables are not allowed
```

## PDF page 32

```text
32
OOP
// In native Java language 
  // global variables are not allowed
  Java tries to enforce an OOP-style structure
     everything must be inside a class
```

## PDF page 33

```text
33
draw()
int x = 100;
void setup(){
    size(500,500);
}
void draw(){
    draw_balloon(x, 200);
    x = x + 10;
}
```

## PDF page 34

```text
34
draw()
void draw(){
    draw_balloon(x, 200);
    x = x + 10;
}
// same concept as in Python-mode
```

## PDF page 35

```text
35
...
```

## PDF page 36

```text
36
if-statement
void draw(){
    draw_balloon(x, 200);
    x = x + 10;
    if (x > 500){
        x = 100;
    }
}
// same concept as in Python-mode
```

## PDF page 37

```text
37
Block of code
void draw(){
    draw_balloon(x, 200);
    x = x + 10;
    if (x > 500){
        x = 100;
    }
}
// See also: if-else and nested if statements
```

## PDF page 38

```text
38
Built-in Global variable
void draw(){
    draw_balloon(x, 200);
    x = x + 10;
    if (x > width){
        x = 100;
    }
}
// same concept as in Python-mode
```

## PDF page 39

```text
39
Local Variable
void draw(){
    int x = 90;
    draw_balloon(x, 80);
}
// must specify its type
// same syntax as global variable
```

## PDF page 40

```text
40
Built-in Function
void draw(){
    int x = random(100,400);
    draw_balloon(x, 80);
}
// Error?
// random() return floating-point number
// Type mismatch: cannot convert from float to int
```

## PDF page 41

```text
41
Type Casting
void draw(){
    int x = (int) random(100,400);
    draw_balloon(x, 80);
}
// (int) will try to cast to int
```

## PDF page 42

```text
42
Type Casting
void draw(){
    int x = (int) "70" ;
    draw_balloon(x, 80);
}
// (int) will try to cast to int
// Error: Cannot cast from String to int
```

## PDF page 43

```text
43
String Parsing
void draw(){
    int x = Integer.parseInt( "70" );
    draw_balloon(x, 80);
}
// Call a method (parseInt)
// in class Integer
```

## PDF page 44

```text
44
...
```

## PDF page 45

```text
45
User defined Function 
(with return value)
... cal_middle(... x1, ... x2) {
    
// To calculate the middle of x1 and x2
// and return the result
// type of parameters?
}
```

## PDF page 46

```text
46
User defined Function 
(with return value)
... cal_middle(int x1, int x2) {
    
// To calculate the middle of x1 and x2
// and return the result
    return (x1 + x2)/2
// type of return value?
}
```

## PDF page 47

```text
47
Integer Division
print( 5/2 );
  // In Java (and many programming languages)
  // the result is 2
  // when both operands are integer
print( 5/2.0 );  // when one operand is float?
```

## PDF page 48

```text
48
User defined Function 
(with return value)
float cal_middle(int x1, int x2) {
    
// To calculate the middle of x1 and x2
// and return the result
    return (x1 + x2)/2.0 // return floating point value
// type of return value
}
```

## PDF page 49

```text
49
User defined Function 
(with return value)
float cal_middle(int x1, int x2) {
    
// To calculate the middle of x1 and x2
// and return the result
    return (x1 + x2)/2.0  // return floating point value
// type of return value
}
```

## PDF page 50

```text
50
... cal_distance(... x1, ... y1, ... x2, ... y2) {
    
// To calculate the distance between 2 points
// and return the result  (from w3)
// exercise
}
User defined Function 
(with return value)
```

## PDF page 51

```text
51
User defined Function 
(with no return value)
void draw_balloon(int x, int y){
    ellipse(x, y, 100, 100);
    line(x, y+50, x, y+200);
}
// void == empty
// the function does not return a value
```

## PDF page 52

```text
52
Function return type
void setup(){
    ...
}
// void == empty
// the function does not return a value
```

## PDF page 53

```text
53
Function return type
... draw(){
    ...
}
// void == empty
// the function does not return a value
```

## PDF page 54

```text
54
Function return type
void draw(){
    ...
}
// void == empty
// the function does not return a value
```

## PDF page 55

```text
55
Function return type
float cal_middle(int x1, int x2) {
    
// To calculate the middle of x1 and x2
// and return the result
    return (x1 + x2)/2.0  // return floating point value
// type of return value
}
```

## PDF page 56

```text
56
...
```

## PDF page 57

```text
57
Array of variables
a = [ 5, 9, 2 ] # Python-mode
```

## PDF page 58

```text
58
Array of variables
a = [ 5, 9, 2 ] # Python-mode
int[] a = ...
// specify its type, [] mean ...
```

## PDF page 59

```text
59
Array of variables
a = [ 5, 9, 2 ] # Python-mode
int[] a = ...
// specify its type, [] mean array
```

## PDF page 60

```text
60
Array of variables
a = [ 5, 9, 2 ] # Python-mode
int[] a = ...
// int[] mean array of integers
```

## PDF page 61

```text
61
Array of variables
a = [ 5, 9, 2 ] # Python-mode
int[] a = { 5, 9, 2 };
// initialise its values, use { }
```

## PDF page 62

```text
62
While Loop
int[] a = { 5, 9, 2 };
int i = 0;
while (i < ...){
    // print all elelments
}
```

## PDF page 63

```text
63
While Loop
int[] a = { 5, 9, 2 };
int i = 0;
while (i < a.length){ // length is an attribute of a
    // print all elelments
}
```

## PDF page 64

```text
64
While Loop
int[] a = { 5, 9, 2 };
int i = 0;
while (i < a.length){
    print( a[i] );               // no new line?
    i = i + 1;
    // similar to Python? 
}
592
```

## PDF page 65

```text
65
println()
int[] a = { 5, 9, 2 };
int i = 0;
while (i < a.length){ 
    println( a[i] );          // will add a new line 
    i = i + 1;
    // it is similar to Python print()
}
5
9
2
```

## PDF page 66

```text
66
For Loop
int[] a = { 5, 9, 2 };
for(int i = 0; i < a.length; i = i + 1){ 
    println( a[i] );
}
// same flowchart as while loop
```

## PDF page 67

```text
67
For Loop
int[] a = { 5, 9, 2 };
for(int i = 0; i < a.length; i = i + 1){ 
    println( a[i] );
}
// put important parts together at the top
// similar in many programming languages, but not Python
```

## PDF page 68

```text
68
For-each Loop
int[] a = { 5, 9, 2 };
for(int x : a){ 
    println( x );
}
// similar to for loop in Python?
```

## PDF page 69

```text
69
Array of variables
int[] a = { 5, 9, 2 }; // initialise its values, use { }
int[] b = ...       // not initialise its values
```

## PDF page 70

```text
70
Array of variables
int[] b = new int[5]; // array of size/length = 5
// create a new array
```

## PDF page 71

```text
71
Array of variables
int[] b = new int[5]; // array of size = 5
// the size is fixed, cannot be changed
// learn how to solve this in the next subject
```

## PDF page 72

```text
72
Array of variables
int[] b = new int[5]; // array of size = 5
b[0] =  2;
b[1] =  7;
b[3] =  8;
// initialise later
```

## PDF page 73

```text
73
Array of variables
int[] b = new int[5]; 
b[0] =  2;
b[1] =  7;
b[3] =  8;
// initialise later
// how about b[2] and b[4]?
```

## PDF page 74

```text
74
Array of variables
int[] b = new int[5]; 
b[0] =  2;
b[1] =  7;
b[3] =  8;
// initialise later
// how about b[2] and b[4]? 
// Java will initialise them to zero
// Not all languages do that, better do it yourself
```

## PDF page 75

```text
75
Array of variables
int[] b = new int[5]; 
b[0] =  2;
b[1] =  7;
b[3] =  8;
// exercise: random the values
```

## PDF page 76

```text
76
...
```

## PDF page 77

```text
77
Class
A class is a blueprint/template for creating objects
An Object is an item/entity/คน/สัตว์/สิ่งของ
Specify what you are interested in
- Attributes (Data/state)
- Methods (Behaviour/action/calculation/function)
```

## PDF page 78

```text
78
Create Class
class Balloon { // specify class name
}
```

## PDF page 79

```text
79
Add Attributes
class Balloon { // specify class name
// specify its attributes 
    int x;
    int y;
    int r;
}
```

## PDF page 80

```text
80
Add Constructor
class Balloon {
    ...
    Balloon(int x, int y, int r){  // specify constructor
        this.x = x;
        this.y = y;
        this.r = r;
    }
// similar concept to Python, this == self
```

## PDF page 81

```text
81
Constructor
class Balloon {
    ...
    Balloon(int x, int y, int r){  // specify constructor
        this.x = x;
        this.y = y;
        this.r = r;
    }
// the name of constructor is the same as the class name
```

## PDF page 82

```text
82
Constructor
class Balloon {
    ...
    Balloon(int x, int y, int r){  // specify constructor
        this.x = x;
        this.y = y;
        this.r = r;
    }
// Same name as the class and no return type
```

## PDF page 83

```text
83
Add Method
class Balloon {
    ...
    void show(){
        line(this.x, this.y, this.x, this.y + 100);
        ellipse(this.x, this.y, this.r, this.r);
    }
}
// similar concept to Python, this == self
```

## PDF page 84

```text
84
Create an Object
void setup(){
    size(500,500);
    Balloon t = new Balloon(200, 200, 70);
    // create a new Balloon object
}
```

## PDF page 85

```text
85
Call its Method
void setup(){
    size(500,500);
    Balloon t = new Balloon(200, 200, 70);
    t.show();
}
```

## PDF page 86

```text
86
Add another Method
void move(){
    // exercise
}
```

## PDF page 87

```text
87
Animation
global variable
setup()
draw()
```

## PDF page 88

```text
88
Global Variable
// int x=100;
// must specify its type
Balloon t;
// Declare t as a variable 
// that can refer to a Balloon object
// but not create an object yet
```

## PDF page 89

```text
89
setup()
Balloon t; // declare t as a variable...
void setup(){
    size(500,500);
    t = new Balloon(200, 200, 70); // create object
}
// create new object of class Balloon
```

## PDF page 90

```text
90
draw()
void draw(){
    background(255);
    t.show();
    t.move();
}
// similar to Python
```

## PDF page 91

```text
91
Array of objects
//Balloon t; // declare t as a variable...
Balloon[] b; 
// Declare b as a variable 
// that can refer to an array of Balloon objects
// but not create an object yet
```

## PDF page 92

```text
92
setup()
Balloon[] b; // declare b as a variable...
void setup(){
    size(500,500);
    b = new Balloon[ 5 ]
      ...
}
```

## PDF page 93

```text
93
setup()
void setup(){
    size(500,500);
    b = new Balloon[ 5 ]
    for (int i = 0; i < b.length; i=i+1) {
        int x = (int) random(50, 450);
        int y = (int) random(50, 500);
        int r = (int) random(30, 80);
        b[i] = new Balloon(x, y, r);
    }
}
```

## PDF page 94

```text
94
draw()
void draw(){
    background(255);
    for (int i = 0; i < b.length; i=i+1) {
        b[i].show();
        b[i].move();
    }
}
```

## PDF page 95

```text
95
...
```

## PDF page 96

```text
96
To try Native Java
- Install JDK (Java SDK)
- Find and follow Java tutorials
- Compile java source code (to create byte code)
  e.g. javac Hello.java
- Run java byte code (on JVM)
  e.g. java Hello
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 97

```text
97
...
```

