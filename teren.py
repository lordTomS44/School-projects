
import turtle as t
import random as rnd


def obloha(r,g,b):
    t.ht()
    t.speed(0)
    t.pencolor(0,0,0)
    t.penup()
    t.fillcolor(r,g,b)
    t.begin_fill()
    t.goto(1000,1000)
    t.goto(1000,-1000)
    t.goto(-1000,-1000)
    t.goto(-1000, 1000)
    t.goto(1000,1000)
    t.end_fill()
    t.speed(5)

def sun(r,g,b):
    t.pencolor(r,g,b)
    
    t.goto(-50,100)
    t.pendown()
    t.fillcolor(r,g,b)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()

def terrain():
    t.speed(3)
    t.goto(-1000, -100)
    t.pendown()
    t.pencolor(0,1,0)
    t.fillcolor(0,1,0)
    t.begin_fill()
    def turn_up():
        t.left(90)
        t.forward(50)
        t.right(90)

    def turn_down():
        t.right(90)
        t.forward(50)
        t.left(90)


    def strom():
        a = t.pos()
        t.forward(50)
        t.penup()
        home(-1000,-1000)
        t.end_fill()
        t.left(180)
        t.goto(a)
        t.pendown()
        t.fillcolor(0.3,0,0)
        t.pencolor(0.3,0,0)
        t.begin_fill()
        t.left(90)
        for i in range(2):
            t.forward(100)
            t.right(90)
            t.forward(50)
            t.right(90)
        t.end_fill()
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.pencolor(0,0.5,0)
        t.fillcolor(0,0.5,0)
        t.begin_fill()
        for i in range(2):
            t.left(90)
            t.forward(100)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(150)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        for i in range(2):
            t.left(90)
            t.forward(100)
        t.end_fill()
        t.penup()
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.pencolor(0,1,0)
        t.fillcolor(0,1,0)
        t.pendown()
        t.begin_fill()

    for i in range(35):
        choice = rnd.randint(0,100)

        if choice <= 33:
            turn_up()
        elif choice >= 66:
            turn_down()
        elif choice > 40 and choice < 60:
            strom()
            pass
        else:
            t.forward(50)
        t.forward(50)
        print(choice)
    
def home(h1, h2):
    t.speed(0)
    t.right(90)
    t.forward(1500)
    t.right(90)
    t.forward(4000)
    t.goto(h1 , h2)
    t.speed(3)
    


obloha(0,1,1)
sun(1,1,0)
terrain()
home(-1000,-1000)
t.end_fill()
t.done()
