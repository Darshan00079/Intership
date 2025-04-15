

import another_module

print(another_module.another_variable)

#timmy=turtle.Turtle
#print(timmy)

from turtle import Turtle, Screen

timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(200)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

