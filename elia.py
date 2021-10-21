import turtle 

     

wn = turtle.Screen() 

wn.bgcolor("black") 

  

t=turtle.Turtle() #turtle for circles, eyes, nose, mouth 

t.speed(8) 

t.hideturtle() 

  

def drawcircle(x,y): 

    t.color("orangered") 

    t.penup() 

    t.goto(x,y) 

    t.begin_fill() 

    t.circle(70) #draws the circle 

    t.end_fill() 

drawcircle(20,0) #right 

drawcircle(-20,0) #left 

  

def triangle(x,y): 

    t.color("black") 

    t.penup() 

    t.goto(x,y) 

    t.begin_fill() 

    for i in range(3): 

      t.forward(40) 

      t.left(360/3) 

    t.end_fill() 

triangle(15, 80) #rt eye 

triangle(-55, 80) #lt eye 

triangle(-20, 50) 

  

def mouth(): 

    t.color("black") 

    t.up() 

    t.goto(-60,40) #start xy 

    t.down() 

    t.begin_fill() 

    t.goto(-30,20) #pos 2 

    t.goto(30,20) #pos 3 

    t.goto(60,40) #pos 4 

    t.goto(0,30) #pos 4 

    t.end_fill() 

mouth() 

  

def stem(): 

    t.color("green") 

    t.up() 

    t.goto(-40,130) # pos 1 start xy 

    t.down() 

    t.begin_fill() 

    t.goto(40,130) #pos 2 

    t.goto(20,150) #pos 3 

    t.goto(10,170) #pos 4 

    t.goto(0,180) #pos 5 

    t.goto(-15,175) #pos 6 

    t.goto(-10,155) #pos 7 

    t.goto(-15,140) #pos 8 

    t.goto(-40,130) #pos 9 - same as start 

    t.end_fill() 

stem() 

  

turtle.write("TRICK OR TREAT", align="center") 

 

 

 

 


 

Question = input("TRICK OR TREAT! May i have candy?") 

if Question == ("yes"):

    print ("here you go") 

if Question == ("no"):

    print ("sorry im all out of candy") 
