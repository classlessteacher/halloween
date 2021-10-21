import turtle

tina = turtle.Turtle()

 

 

def make_triangle(x, y, color):

  turtle.penup()

  turtle.goto(x,y)

  turtle.begin_fill()

  turtle.color(color)

  tina.pendown()

  for count in range(3):

    turtle.forward(50)

    turtle.left(120)

  turtle.end_fill()

 

def make_square(x, y, color):

  turtle.penup()

  turtle.goto(x,y)

  turtle.begin_fill()

  turtle.color(color)

  turtle.pendown()

  for count2 in range(3):

    turtle.forward(50)

    turtle.left(90)

  turtle.end_fill()

 

 

turtle.penup()

turtle.goto(0,-150)

turtle.color('#FF8000')

turtle.begin_fill()

turtle.circle(150)

turtle.end_fill()

turtle.left(180)

 

 

 

 

make_triangle(-35, -20, '#000000')

make_triangle(0, -20, '#000000')

make_triangle(35, -20, '#000000')

 

 

turtle.left(180)

 

 

make_square(-70, 50, '#CC0000')

make_square(20, 100, '#CC0000')

 

 

 

turtle.penup()

turtle.goto(-100,-185)

turtle.write( "trick or treat!" )

turtle.goto(-200,-185)

turtle.left(180)
