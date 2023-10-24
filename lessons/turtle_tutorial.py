"""EX05- Turtle Scene."""
__author__ = "730400711"

from turtle import Turtle, colormode, done
colormode(255)
# Creating first turtle- Leo
leo: Turtle = Turtle()

leo.speed(50)
leo.pencolor("pink")
leo.fillcolor("pink")
leo.begin_fill()
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.goto(0, 15)

bob: Turtle = Turtle()

bob.pencolor("black")
bob.penup()
bob.speed(70)

# Creating first bob triangle to fit inside of Leo
side_length: int = 300
bob_one: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    bob_one = bob_one + 1
bob.goto(0, 15)

# Creating  second bob traingle to fit inside Leo
bob_two: int = 0
while (i < 8):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
bob.penup()
bob.goto(45, 60)
bob.pendown()

done()



