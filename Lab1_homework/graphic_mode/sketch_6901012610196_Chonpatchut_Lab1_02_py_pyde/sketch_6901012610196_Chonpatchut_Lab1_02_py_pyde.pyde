#canva size declaration
size(950, 750)

#variable declaration
x = 100
y = 200
w = 120
h = 300
gap = 80

#draw L
line(x, y, x, y+h)
line(x, y+h, x+w, y+h)

#draw I
x = x + w + gap
line(x,y, x+w, y)
line(x+w/2, y, x+w/2, y+h)
line(x, y+h, x+w, y+h)

#draw N
x = x + w + gap
line(x, y, x, y+h)
line(x, y, x+w, y+h)
line(x+w, y, x+w, y+h)

#draw E
x = x + w + gap
line(x,y, x+w, y)
line(x, y+h/2, x+w, y+h/2)
line(x, y+h, x+w, y+h)
line(x, y, x, y+h)
