# Week 03 — OOP inheritance, polymorphism, Tkinter GUI

Source PDF pages 151–210. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 151

```text
010123138 
Computer Programming
```

## PDF page 152

```text
2
Check Attendance..
```

## PDF page 153

```text
3
Review
```

## PDF page 154

```text
4
Need a Volunteer
```

## PDF page 155

```text
5
Class
A class is a blueprint/template for creating objects
An Object is an item/entity/คน/สัตว์/สิ่งของ
Specify what you are interested in
- Attributes (Data/state)
- Methods (Behaviour/action/calculation/function)
```

## PDF page 156

```text
6
User-defined
User-defined Variable
User-defined Function
User-defined Type (data type/Class)
```

## PDF page 157

```text
7
OOP is a programming approach that organizes programs 
around objects
"Procedural programming" organizes a program as a 
sequence of procedures or functions
(what we did at the beginning)
Object-Oriented Programming (OOP)
```

## PDF page 158

```text
8
The four main concepts of Object-Oriented Programming 
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
4 Pillars of OOP
```

## PDF page 159

```text
9
Inheritance
Inheritance — Creating a new class based on an existing class
* Subclass will inherit (from Superclass)
   - Attributes
   - Methods
```

## PDF page 160

```text
10
Subclass
class EsBalloon( Balloon ):
    # EsBalloon is a sublcass of Balloon
    # for expanding and shinking balloon
    ...
```

## PDF page 161

```text
11
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        # define the constuctor
        ...
```

## PDF page 162

```text
12
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        # call the constuctor of the superclass
        ...
```

## PDF page 163

```text
13
Subclass
class EsBalloon( Balloon ):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.change = 1
        # add a new attribute
```

## PDF page 164

```text
14
Add a method
    def expand_shrink(self):
        self.r = self.r + self.change
        if self.r >= 60:
            self.change = -1
        elif self.r <= 30:
            self.change = 1
```

## PDF page 165

```text
15
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

## PDF page 166

```text
16
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

## PDF page 167

```text
17
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

## PDF page 168

```text
18
Method Override
Inheritance — Creating a new class based on an existing class
* Subclass will inherit (from Superclass)
   - Attributes
   - Methods
   
Can override a method of the superclass
  - move() in EsBalloon may include expand_shrink()
```

## PDF page 169

```text
19
Method Override
class EsBalloon(Balloon):
    ...
    def move(self):  
        # override move() in the superclass
        # so it will not do the same thing
        ...
```

## PDF page 170

```text
20
Method Override
class EsBalloon(Balloon):
    ...
    def move(self):  # override move() in the superclass
        super().move()  # call the superclass method
        self.expand_shrink()  # call its own method
```

## PDF page 171

```text
21
Polymorphism — Many shapes/forms
Polymorphism
```

## PDF page 172

```text
22
Polymorphism — Many shapes/forms
 - Method overriding
   A method with the same name 
        can have different behaviour
move() in EsBalloon can be different from its superclass
Polymorphism
```

## PDF page 173

```text
23
Polymorphism — Many shapes/forms
 - Method overriding
 - Subtype
     EsBalloon is a Balloon?
     Person can be a student?
     have the same set of methods?
Polymorphism
```

## PDF page 174

```text
24
...
```

## PDF page 175

```text
25
User Interface
A User Interface (UI) is the system through which a 
human interacts with a computer
```

## PDF page 176

```text
26
Command-Line Interface
Early user interfaces were primarily text-based 
Command-Line Interface (CLI)
users interacted with computers 
by typing in commands
e.g. dir, cd, md
   
ls, mkdir
https://en.wikipedia.org/wiki/VT100
```

## PDF page 177

```text
27
Graphical User Interface
Graphical User Interface (GUI)
https://en.wikipedia.org/wiki/Microsoft_Windows
users interacted with computers 
by pointing, clicking 
also typing, touching, tapping
```

## PDF page 178

```text
28
Widget
Widget - Basic GUI element 
https://en.wikipedia.org/wiki/Microsoft_Windows
- Window
- Menu
- Icon
- Textbox
- Button
- Label
- Canvas
  ...
```

## PDF page 179

```text
29
Event
Event - an action or occurrence in GUI
https://en.wikipedia.org/wiki/Microsoft_Windows
- Mouse click
- Mouse move
- Mouse enter
- Mouse leave
- Keyboard press
- Window resize
  ...
```

## PDF page 180

```text
30
Event Handler
Event Handler - A Function or method that is called   
                  when an event occur
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 181

```text
31
Tkinter
Python’s built-in library for creating GUI applications
A library is a collection of pre-written code that you can 
use in your own programs
e.g. math, os, mathplotlib, numpy
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 182

```text
32
Create a Window
import tkinter
window = tkinter.Tk()  # create main window
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 183

```text
33
Window settings
import tkinter
window = tkinter.Tk()  # create main window
window.title("My tk App") # set title
window.geometry("500x500") # set size
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 184

```text
34
Event Listener Loop
import tkinter
window = tkinter.Tk()  # create main window
window.title("My tk App") # set title
window.geometry("500x500") # set size
window.mainloop()  
# loop to wait for an event, e.g. user click
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 185

```text
35
...
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 186

```text
36
Add a Label
... # after create window
label = tkinter.Label(window, text="Hello")
... # before mainloop
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 187

```text
37
Call layout manager
... # after create window
label = tkinter.Label(window, text="Hello")
label.pack()
# to manage this label (before showing it on window)
... # before mainloop
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 188

```text
38
...
```

## PDF page 189

```text
39
Add Textbox Entry
... # after create label
entry1 = tkinter.Entry(window)
entry1.pack()
entry2 = tkinter.Entry(window)
entry2.pack()
... # before mainloop
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 190

```text
40
Add a Button
... # after create textboxes
button = tkinter.Button(window, text="Multiply")
button.pack()
... # before mainloop
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 191

```text
41
Add Event Handler
def multiply():  # create a function
    
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 192

```text
42
Get value from Textbox
def multiply():  # create a function
    num1 = float( entry1.get() ) 
    # get input value from textbox
    
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 193

```text
43
Get value from Textbox
def multiply():  # create a function
    num1 = float( entry1.get() ) 
    num2 = float( entry2.get() )
    
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 194

```text
44
Calculate result
def multiply():
    num1 = float( entry1.get() )
    num2 = float( entry2.get() )
    result = num1 * num2     
    
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 195

```text
45
Set Label
def multiply():
    num1 = float( entry1.get() )
    num2 = float( entry2.get() )
    result = num1 * num2
    label.config( text=result )
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 196

```text
46
Set Event handler
# add command when create button
# button = tkinter.Button(window, text="Multiply")
button = tkinter.Button(window, text="Multiply", 
command=multiply )
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 197

```text
47
Set Event handler
# add command when create button
# button = tkinter.Button(window, text="Multiply")
button = tkinter.Button(window, text="Multiply", 
command=multiply )
  # when this button is pressed
  # it will call multiply()
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 198

```text
48
...
```

## PDF page 199

```text
49
Try layout manager setting/option
pady - add vertical padding
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 200

```text
50
Add veritcal padding
label.pack( pady=20 )
entry1.pack( pady=20 )
button.pack( pady=40 )
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 201

```text
51
Add a Frame
entry_frame = tkinter.Frame(window)
entry_frame.pack(pady=20)
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 202

```text
52
Add a Frame
window 
│
├── label
├── entry1
├── entry2
└── button
# without frame
https://en.wikipedia.org/wiki/Microsoft_Windows
window
│
├── label
├── entry_frame
│   ├── entry1
│   └── entry2
└── button
# use frame to 
manage layout
```

## PDF page 203

```text
53
Add Entry to the Frame
entry1 = tkinter.Entry(entry_frame, width=10)
entry1.pack(side="left", padx=5)
entry2 = tkinter.Entry(entry_frame, width=10)
entry2.pack(side="left", padx=5)
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 204

```text
54
Add Entry to the Frame
# entry1 = tkinter.Entry(window)
entry1 = tkinter.Entry(entry_frame, width=10)
# not to window directly
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 205

```text
55
Try layout manager setting/option
pady - add vertical padding
grid layout
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 206

```text
56
Try other widgets
https://tkdocs.com/tutorial/widgets.html
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 207

```text
57
...
```

## PDF page 208

```text
58
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

## PDF page 209

```text
59
Assessment
A2 
10%
app/game based on 2D array
Discussed with your group members?
```

## PDF page 210

```text
60
...
```

