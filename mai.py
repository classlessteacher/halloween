import turtle 

  

wn = turtle.Screen() 

wn.bgcolor("purple") 

  

t = turtle.Turtle()  # turtle for circles, eyes, nose, mouth 

t.speed(8) 

t.hideturtle() 

  

  

def drawellipse(x, y): 

    t.color("orangered") 

    t.penup() 

    t.goto(x, y) 

    t.begin_fill() 

    t.circle(65)  # draws the circle 

    t.end_fill() 

drawellipse(0, -35) 

drawellipse(30, -35) 

drawellipse(-30, -35) 

  

def drawcircle(x, y): 

    t.color("black") 

    t.penup() 

    t.goto(x, y) 

    t.begin_fill() 

    t.circle(20)  # draws the circle 

    t.end_fill() 

drawcircle(40, 20) 

drawcircle(-40, 20) 

  

  

def triangle(x, y): 

    t.color("black") 

    t.penup() 

    t.goto(x, y) 

    t.begin_fill() 

    for i in range(3): 

      t.forward(15) 

      t.left(360/3) 

    t.end_fill() 

triangle(-6.5, 19) 

  

def mouth(): 

    t.color("black") 

    t.up() 

    t.goto(-60, 10) 

    t.down() 

    t.begin_fill() 

    t.goto(-26, -10) 

    t.goto(26, -10) 

    t.goto(60, 10) 

    t.goto(0, 0) 

    t.end_fill() 

mouth() 

  

def stem(): 

    t.color("green") 

    t.up() 

    t.goto(-45, 85) 

    t.down() 

    t.begin_fill() 

    t.goto(50, 85) 

    t.goto(15, 100) 

    t.goto(5, 135) 

    t.goto(-5, 135) 

    t.goto(-20, 130) 

    t.goto(-15, 110) 

    t.goto(-20, 95) 

    t.goto(-50, 85) 

    t.end_fill() 

stem() 

  

import turtle 

tina = turtle.Turtle() 

tina.shape("turtle") 

  

tina.color("white") 

tina.penup() 

tina.goto(-35,-80) 

tina.write('TRICK OR TREAT!', None, "100pt bold") 

tina.goto(-50,-80) 

tina.left(90) 

 
