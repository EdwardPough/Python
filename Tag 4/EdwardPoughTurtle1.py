import turtle

turtle.shape("turtle")
turtle.color("green")

def schild_ada():
    #Letter A
    turtle.pendown()
    turtle.left(75)
    turtle.forward(100)
    turtle.right(150)
    turtle.forward(100)
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.left(75)
    turtle.forward(25)
    turtle.penup()
    turtle.left(180)
    turtle.forward(25)
    turtle.right(75)
    turtle.forward(50)
    turtle.left(75)
    #Move to next Letter
    turtle.forward(10)
    #Letter D
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    for x in range(157):
        turtle.forward(1)
        turtle.right(1.15)
    turtle.penup()
    #Move to next Letter
    turtle.right(179.85)
    turtle.forward(60)
    #Letter A
    turtle.pendown()
    turtle.left(75)
    turtle.forward(100)
    turtle.right(150)
    turtle.forward(100)
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.left(75)
    turtle.forward(25)
    turtle.penup()
    turtle.left(180)
    turtle.forward(25)
    turtle.right(75)
    turtle.forward(50)
    turtle.left(75)

def schild_space():
    turtle.forward(30)


def schild_quadrat():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()

schild_ada()
schild_space()
schild_quadrat()