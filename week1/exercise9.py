# -*- coding: utf-8 -*-

import turtle
import time
turtle.speed('fastest')
turtle.pensize(1)
for x in range(100):
	turtle.forward(2*x)
	turtle.left(90)
wait = raw_input('press any button')
print 'break'