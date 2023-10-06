import random
from turtle import Turtle,Screen
screen =Screen()
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt= "Enter color of turtle")
for turtle_index in range(0,6):
    tim =Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_index])
    tim.color(colors[turtle_index])

if user_bet:
    is_race_on =True

while is_race_on:
    rand_distance=random.randint(0,10)
    turtle.forward(rand_distance)
    
screen.exitonclick()