# -*- coding: utf-8 -*-

import turtle


turtle.color('red')
turtle.pensize(2)
turtle.setx(-200)
turtle.sety(200)

turtle.forward(200)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(200)
turtle.penup()
turtle.goto(300,300)
turtle.pendown()
turtle.setheading(0)#向东
raw_input('for stop the turtle')