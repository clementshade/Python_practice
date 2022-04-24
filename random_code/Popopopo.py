import turtle
turtle.getscreen()
x =0
y =-0
t = turtle.Turtle()
t.pencolor("red")

t.speed(100)


t.goto(0,0)
def move(H,Y,colour):
    t.penup()
    t.goto(H,Y)
    t.pendown()
    t.pencolor(colour)
    global x
    x += 1

def shape(z,y):
    t.right(z)
    t.forward(50)
    t.right(y)
    t.forward(50)
    t.right(z)
    t.forward(50)
    t.right(y)
    t.forward(50)
def shape1(z,y):
    t.right(y)
    t.forward(50)
    t.right(z)
    t.forward(50)
    t.right(y)
    t.forward(50)
def shape2(z,y):
    t.right(y)
    t.forward(20)
    t.left(z)
    t.forward(20)
    t.right(y)
    t.backward(50)
    t.left(z)
    t.backward(50)
    t.right(y)
    t.forward(20)
    t.left(z)
    t.forward(20)
    t.right(y)
    t.backward(50)
    t.left(z)
    t.backward(50)
while x < 10:
    shape(20,170)
    
    x += 1
if x ==10:
    move(-200,100,"blue")

while 10 < x < 20:
    shape(-20,130)
    x += 1

if x ==20:
    move(130,200,"purple")

while 20 < x < 30:
    shape(-30,170)
    x += 1

if x ==30:
    move(-120,-70,"green")

while 30 < x < 45:
    shape1(160,30)
    x += 1

if x ==45:
    move(200,20,"orange")

while 45 < x < 60:
    shape1(130,40)
    x += 1
   
if x ==60:
    move(130,-190,"purple")
while 60 < x < 80:
    shape1(-30,120)
    x += 1

if x ==80:
    move(-130,-210,"blue")
while 80 < x < 90:
    shape2(30,-40)
    x += 1

