import turtle 

 

wn = turtle.Screen() 

wn.bgcolor("lavender") 

 

t=turtle.Turtle() #turtle for circle, eyes, nose, mouth 

t.hideturtle() 

   

def drawcircle(z,y): 

  t.color("orangered") 

  t.penup()  

  t.goto(z,y) 

  t.begin_fill() 

  t.circle(70) #draws the circle 

  t.end_fill() 

drawcircle(10,0) #right 

 

   

def square(x,y): 

  t.color("yellow") 

  t.penup() 

  t.goto(x,y) 

  t.begin_fill() 

  for i in range(3): 

    t.forward(20) 

    t.left(180/2) 

  t.end_fill() 

square(20,80) #right eye 

square(-40,100) #left eye 

square(10,60) #nose 

 

def mouth(): 

  t.color("orange") 

  t.up() 

  t.goto(-20,20) #start xy 

  t.down() 

  t.begin_fill() 

  t.goto(-30,20) #position 2 

  t.goto(30,20) #position 3 

  t.goto(30,30) #position 4 

 

  t.end_fill() 

mouth() 

 

def stem(): 

  t.color("green") 

  t.up() 

  t.goto(-20,130) #positio 1 start xy 

  t.down() 

  t.begin_fill() 

  t.goto(20,120) #position 2 

  t.goto(30,130) #position 3 

  t.goto(0,160) #position 4 

  t.goto(0,170) #position 5 

  t.goto(-20,170) #position 6  

  t.goto(-20,175) #position 7 

  t.goto(-20,175) #position 8 

  t.goto(-20,155) #position 9 same as start 
  
stem()

Question = input('Hi there! Do you want a trick or treat?') 


if "treat" in Question: 

  print ("Happy Halloween! I don't have any candy but i do have a cat and a dog, so choose!") 

  answer = input() 

  if "cat" in answer: 

    print('=(^o^)=___') 

    print('       ||||-') 

    print('Here you go! Happy halloween!') 

  if "dog" in answer: 

    print('Oh, sorry, i forgot that I kind of adopted him... heheh.. Happy halloween though!') 

if "trick" in Question: 

    print ("Booooooooo! Haha tricked you! It's just me! don't worry, I'm in a mummy COSTUME!") 

    print('(U_U)') 

    print(' -|-') 

    print(' | |')  

     
