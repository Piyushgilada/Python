import colorgram
colors=colorgram.extract('im.jpg',30)
rgb_color=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb_color.append((r,g,b))

print(rgb_color)
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
color_list=[(223, 227, 235), (239, 231, 210), (239, 225, 235), (222, 238, 228), (189, 166, 128), (142, 166, 190), (218, 207, 134), (68, 101, 133), (135, 96, 58), (183, 150, 167), (145, 175, 156), (11, 19, 52), (52, 18, 7), (176, 156, 42), (127, 82, 100), (75, 113, 85), (51, 13, 25), (179, 185, 218), (9, 27, 14), (104, 118, 169), (214, 177, 191), (22, 47, 128), (171, 206, 182), (162, 108, 129), (121, 27, 46), (121, 36, 24), (99, 149, 101), (30, 87, 50), (163, 203, 211), (219, 180, 173)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
def draw():
    for _ in range (10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
draw()

for _ in range(10):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    draw()

screen=turtle_module.Screen()
screen.exitonclick()
#
