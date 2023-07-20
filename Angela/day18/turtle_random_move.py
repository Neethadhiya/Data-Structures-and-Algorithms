import turtle
import random
tim=turtle.Turtle()
# for _ in range(10):
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.right(90)
def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    a=(r,g,b)
    return a
directions=[0,90,180,270]
tim.pensize(10)
tim.speed("fastest")
for _ in range(200):
    tim.color(colors())
    tim.forward(30)
    
    tim.setheading(random.choice(directions))
tim.done()
