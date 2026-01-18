import turtle

screen = turtle.Screen()
screen.bgcolor('black')
screen.title("A")
screen.setup(width=1.0, height=1.0)

t = turtle.Turtle()
t.color('purple')
t.pensize(20)
t.speed(1)

# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
t.penup()
t.goto(-200,-50)
t.left(90)
t.pendown()
t.forward(200)
t.right(140)
t.forward(150)
t.left(100)
t.forward(150)
t.right(140)
t.forward(200)


# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
t.penup()
t.setx(50)
t.left(90)
t.pendown()
t.forward(80)
t.penup()
t.backward(80)
t.pendown()
t.left(90)
t.forward(190)
t.right(90)
t.forward(80)
t.penup()
t.backward(80)
t.right(90)
t.forward(95)
t.pendown()
t.left(90)
t.forward(80)

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

t.penup()
t.goto(200, -50)
t.pendown()
t.left(90)
t.forward(200)
t.backward(100)
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.backward(200)
t.penup()


# DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

t.goto(350,150)
t.pendown()
t.forward(200)
t.left(90)
t.circle(100, 180)
t.penup()

# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

t.goto(515, -50)
t.circle(2)
t.pendown()
t.right(90)
t.forward(200)



turtle.done()