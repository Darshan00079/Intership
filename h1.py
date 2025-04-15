from turtle import Screen,Turtle

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("white")
screen.title("Saanp ka Game")

segment_1=Turtle("square")
segment_1.color("black")

segment_2=Turtle("square")
segment_2.color("black")
segment_2.goto(-20,0)

segment_3=Turtle("square")
segment_3.color("black")
segment_3.goto(-40,0)

screen=screen.exitonclick()