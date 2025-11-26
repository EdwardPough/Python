import turtle

turtle.shape("turtle")
turtle.color("purple")
turtle.Screen().bgpic(r"C:\Users\EdwardPough\OneDrive - joblinge.de\Programmieren\Python\Tag 4\katzetanze.gif")



def mandala():
    wieoft = int(input("Wie viele Quadrate? "))
    wieschnell = int(input("Wie schnell? (3 ist Standart) "))
    turtle.speed(wieschnell)
    for x in range(wieoft):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left((360/wieoft)+90)
        turtle.penup()

mandala()