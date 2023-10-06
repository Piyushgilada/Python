import turtle as t
import random
tim= t.Turtle()

colors=["saddle brown","pale green","cadet blue","maroon","hot pink"]
def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

tim =t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions=[0,90,180,270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))