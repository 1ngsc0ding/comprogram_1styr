# Week 04 — Classes and objects: animated balloons

Source PDF pages 211–283. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 211

```text
010123138 
Computer Programming
```

## PDF page 212

```text
2
Check Attendance..
```

## PDF page 213

```text
3
Review
```

## PDF page 214

```text
4
Need a Volunteer
```

## PDF page 215

```text
5
Class
A class is a blueprint/template for creating objects
An Object is an item/entity/คน/สัตว์/สิ่งของ
Specify what you are interested in
- Attributes (Data/state)
- Methods (Behaviour/action/calculation/function)
```

## PDF page 216

```text
6
Big Picture
Consists of many item/entity/คน/สัตว์/สิ่งของ
- Balloon
- Cloud
- Cat, Dog, House, Tree, Car, Bike, ...
Solve the problem, and reuse later?
```

## PDF page 217

```text
7
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

## PDF page 218

```text
8
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

## PDF page 219

```text
9
Create Object
b = Balloon(400, 600, 50)
# this will call its constructor
# In Python __init__() will be called
# A Class is a template/blueprint of an object
```

## PDF page 220

```text
10
Call a method
b = Balloon(400, 600, 50)
def setup():
    size(1000, 1000)
    b.show()
# graphic mode - should draw on screen :)
```

## PDF page 221

```text
11
Add another method
    def move(self):
        if self.y > width / 2:
            self.y = self.y - 2
        else:
            self.y = self.y - 4
# only 1 parameter, "self"
```

## PDF page 222

```text
12
Call move() to animate
def draw():
    background(255)
    b.show()
    b.move()
# do not need to change its data (attributes)?
# only call its methods, it knows what to do :)
```

## PDF page 223

```text
13
...
```

## PDF page 224

```text
14
Array of objects
balloons = []  # create an empty array
def setup():
    size(1000, 1000)
    ...
```

## PDF page 225

```text
15
Array of objects
def setup():
    size(1000, 1000)
    x_coords = [100, 200, 400, 500, 600]
    y_coords = [900, 850, 600, 700, 950]
    
    i = 0
    while i < len(x_coords):
        balloons.append(Balloon(x_coords[i], y_coords[i], 
50))
        i = i + 1
```

## PDF page 226

```text
16
Array of objects
def draw():
    background(255)
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        i = i + 1
```

## PDF page 227

```text
17
...
```

## PDF page 228

```text
18
Class
A class is a blueprint/template for creating objects
Specify what you are interested in
- Attributes (Data/state)
- Methods (Behaviour/action/calculation/function)
```

## PDF page 229

```text
19
User-defined
User-defined Variable
User-defined Function
```

## PDF page 230

```text
20
User-defined
User-defined Variable
User-defined Function
User-defined Type (data type/Class)
```

## PDF page 231

```text
21
Similar Idea in Biology
Kingdom
  ↓
Phylum
  ↓
Class 
  ↓
Order
  ↓
Family
  ↓
Genus
  ↓
Species
```

## PDF page 232

```text
22
OOP is a programming approach that organizes programs 
around objects
"Procedural programming" organizes a program as a 
sequence of procedures or functions
(what we did at the beginning)
Object-Oriented Programming (OOP)
```

## PDF page 233

```text
23
The four main concepts of Object-Oriented Programming 
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
4 Pillars of OOP
```

## PDF page 234

```text
24
Encapsulation — Bundling data and methods together 
                    and controlling access to them
Python does not enforce access control
(Python does not strictly enforce private/protected access like 
some languages do)
later we will try it with Java
Encapsulation
```

## PDF page 235

```text
25
Abstaction
Abstraction — Hiding unnecessary details 
                and showing only what is needed
We use the brake pedal to stop the car.
we don't need to know:
 - How the braking system works internally
 - Whether it uses disc brakes or drum brakes
 - How brake pressure is generated
```

## PDF page 236

```text
26
...
```

## PDF page 237

```text
27
Inheritance
Inheritance — Creating a new class based on an existing class
```

## PDF page 238

```text
28
Inheritance
Inheritance — Creating a new class based on an existing class
* New class will inherit (from an existing class)
   - ...
   - ...
```

## PDF page 239

```text
29
Inheritance
Inheritance — Creating a new class based on an existing class
* New class will inherit (from an existing class)
   - Attributes
   - Methods
```

## PDF page 240

```text
30
Inheritance
Inheritance — Creating a new class based on an existing class
* Subclass will inherit (from Superclass)
   - Attributes
   - Methods
```

## PDF page 241

```text
31
Inheritance
Inheritance — Creating a new class based on an existing class
* class EsBalloon will inherit (from class Balloon)
   - Attributes
   - Methods
Wait for class EsBalloon
```

## PDF page 242

```text
32
Inheritance
Different naming
* Superclass and subclass
* Base class and derived class
* Parent class and child class
```

## PDF page 243

```text
33
...
```

## PDF page 244

```text
34
Subclass
class EsBalloon( Balloon ):
    # EsBalloon is a sublcass of Balloon
    # for expanding and shinking balloon
    ...
```

## PDF page 245

```text
35
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        # define the constuctor
        ...
```

## PDF page 246

```text
36
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        # call the constuctor of the superclass
        ...
```

## PDF page 247

```text
37
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.change = 1
        # add a new attribute
```

## PDF page 248

```text
38
Add a method
    def expand_shrink(self):
        self.r = self.r + self.change
        # to make it expand and shrink
        ...
```

## PDF page 249

```text
39
Add a method
    def expand_shrink(self):
        self.r = self.r + self.change
        if self.r >= 60:
            self.change = -1
        elif self.r <= 30:
            self.change = 1
```

## PDF page 250

```text
40
Setup
def setup():
    size(1000, 1000)
    x_coords = [100, 200, 400, 500, 600]
    y_coords = [900, 850, 600, 700, 950]
    
    i = 0
    while i < len(x_coords):        
        balloons.append( EsBalloon(x_coords[i], y_coords[i], 50) )
        i = i + 1
```

## PDF page 251

```text
41
Draw
def draw():
    background(255)
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        balloons[i].expand_shrink()
        i = i + 1
```

## PDF page 252

```text
42
Draw
def draw():
    background(255)
    i = 0
    while i < len(balloons):
        balloons[i].show()
        balloons[i].move()
        # balloons[i].expand_shrink() # include it in move()?
        i = i + 1
```

## PDF page 253

```text
43
Inheritance
Inheritance — Creating a new class based on an existing class
* Subclass will inherit (from Superclass)
   - Attributes
   - Methods
```

## PDF page 254

```text
44
Method Override
Inheritance — Creating a new class based on an existing class
* Subclass will inherit (from Superclass)
   - Attributes
   - Methods
   
Can override a method of the superclass
  - move() in EsBalloon may include expand_shrink()
```

## PDF page 255

```text
45
Method Override
class EsBalloon(Balloon):
    ...
    def move(self):  
        # override move() in the superclass
        # so it will not do the same thing
        ...
```

## PDF page 256

```text
46
Method Override
class EsBalloon(Balloon):
    ...
    def move(self):  # override move() in the superclass
        super().move()  # call the superclass method
        self.expand_shrink()  # call its own method
```

## PDF page 257

```text
47
...
```

## PDF page 258

```text
48
Text Mode
Person
# subclass?
```

## PDF page 259

```text
49
Text Mode
Person
    Student
```

## PDF page 260

```text
50
Text Mode
Person
    Student
```

## PDF page 261

```text
51
Text Mode
Person
    Student
    Employee
```

## PDF page 262

```text
52
Text Mode
Person
    Student
    Employee
// show_info() ?
```

## PDF page 263

```text
53
Text Mode
Person
    Student
    Employee
// show_info() ? call superclass method
```

## PDF page 264

```text
54
Text Mode
Person
    Student
    Employee
// getBMI() ? call superclass method
```

## PDF page 265

```text
55
Example Classes
Person
    Student
    Employee
        Manager
```

## PDF page 266

```text
56
Example Classes
Person
    Student
    Employee
        Manager
// staff discount?
```

## PDF page 267

```text
57
...
```

## PDF page 268

```text
58
Polymorphism — Many shapes/forms
Polymorphism
```

## PDF page 269

```text
59
Polymorphism — Many shapes/forms
 - Method overriding
 - Subtype
Polymorphism
```

## PDF page 270

```text
60
Polymorphism — Many shapes/forms
 - Method overriding
   A method with the same name 
        can have different behaviour
Polymorphism
```

## PDF page 271

```text
61
Polymorphism — Many shapes/forms
 - Method overriding
   A method with the same name 
        can have different behaviour
move() in EsBalloon can be different from its superclass
Polymorphism
```

## PDF page 272

```text
62
Polymorphism — Many shapes/forms
 - Method overriding
 - Subtype
     EsBalloon is a Balloon?
     Person can be a student?
     have the same set of methods?
Polymorphism
```

## PDF page 273

```text
63
Polymorphism — Many shapes/forms
 - Method overriding
 - Subtype
     EsBalloon is a Balloon?
     Person can be a student?
Polymorphism
```

## PDF page 274

```text
64
...
```

## PDF page 275

```text
65
Old Syntax 
Python-mode Processing
super().__init__(x, y, r)
# does not work, must change to
super(EsBalloon, self).__init__(x, y, r)
   
   # get the superclass of EsBalloon, then call its constructor
```

## PDF page 276

```text
66
Old Syntax 
Python-mode Processing
class Balloon( object ):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
# Specify object as the superclass of Balloon
```

## PDF page 277

```text
67
...
```

## PDF page 278

```text
68
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

## PDF page 279

```text
69
Assessment
Lecture 10% consists of
- After class quizzes (individual)
- Task 1 (group work)
- Task 2 (group work)
```

## PDF page 280

```text
70
Assessment
Lecture 10% consists of
- Task 1 (group work)
   - find exercises (coding 
question) and write solution
   - create quizzes (google form)
w1 for group 1, w2 for group 2, ...
```

## PDF page 281

```text
71
Assessment
Lecture 10% consists of
- Task 2 (group work)
   - find 5 example classes from 
other textbooks in the library
     (may not in Python)
   - note their attributes and 
methods
```

## PDF page 282

```text
72
Assessment
Lecture 10% consists of
- Task 2 Part 2 (group work)
   - find 5 example class inheritance 
from other textbooks in the library
     (may not in Python)
   - note their attributes and methods 
(create slides and submit by Friday, and every member 
prepare to present next week)
```

## PDF page 283

```text
73
...
```

