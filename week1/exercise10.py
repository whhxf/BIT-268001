# -*- coding: utf-8 -*-

import turtle
import time
turtle.speed('fastest')
turtle.pensize(2)
turtle.bgcolor('black')
colors = ['red','yellow','purple','blue']
turtle.tracer(True)
for x in range(400):
	turtle.forward(2*x)
	turtle.color(colors[x % 3])
	turtle.left(92)
turtle.tracer(True)
wait = raw_input('press any button')
print 'break'