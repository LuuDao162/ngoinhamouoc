import turtle

#màu background
turtle.bgcolor ("lightskyblue")

#sun
turtle.penup()
turtle.goto( 200, 350)
turtle.pendown()
turtle.goto( 200, 150)

turtle.penup()
turtle.goto( 100, 250)
turtle.pendown()
turtle.goto( 300, 250)

turtle.penup()
turtle.goto( 125, 325)
turtle.pendown()
turtle.goto( 275, 175)

turtle.penup()
turtle.goto( 275, 325)
turtle.pendown()
turtle.goto( 125, 175)

turtle.penup()
turtle.goto( 200, 210)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor("black")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

#house
#mặt trước
turtle.penup()
turtle.goto( -100, -100)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor("black")
turtle.fillcolor("blue")
turtle.begin_fill()

for i in range(4):
    turtle.forward(170)
    turtle.right(90)
turtle.end_fill()

#door
turtle.penup()
turtle.goto( -65, -270)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor("black")
turtle.fillcolor("aquamarine3")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

#mặt bên
turtle.penup()
turtle.goto(70, -100)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.left(30)
turtle.forward(150)
turtle.right(120)
turtle.forward(170)
turtle.right(60)
turtle.forward(150)
turtle.end_fill()

##window
turtle.penup()
turtle.goto(110, -130)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor("black")
turtle.fillcolor("red")
turtle.begin_fill()

turtle.backward(50)
turtle.left(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)

turtle.end_fill()

#roof
turtle.penup()
turtle.goto( -100, -100)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor("black")

turtle.fillcolor("darkorchid1")
turtle.begin_fill()
for i in range(3):
    turtle.right(30)
    turtle.forward(168)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto( -16, 47)
turtle.pendown()
turtle.fillcolor("darkgoldenrod2")
turtle.begin_fill()

turtle.right(60)
turtle.forward(151)
turtle.right(90)
turtle.forward(168)
turtle.right(90)
turtle.forward(151)
turtle.end_fill()

#tree
turtle.penup()
turtle.goto( -300, -250)
turtle.pendown
turtle.goto( -300, -350)

turtle.penup()
turtle.goto( -350, -350)
turtle.pendown()
turtle.goto( -350, -250)

turtle.penup()
turtle.goto( -425, -250)
turtle.pendown()
turtle.goto( -225, -250)





turtle.done()

