import turtle
w=turtle.Screen()
import random
ttl=turtle.Turtle()
# for _ in range(4):
#     ttl.forward(150)
#     ttl.left(90)
# for i in range(30):
#     ttl.pendown()
#     ttl.forward(5)
#     ttl.penup()
#     ttl.forward(5)
# for i in range(70):
#     ttl.pendown()
#     ttl.forward(5)
#     ttl.penup()
#     ttl.forward(5)
n=3
colors=["red","green","blue"]
def shapes(n):
    angle=360/n
    for _ in range(n):
        ttl.forward(100)
        ttl.right(angle)
for i in range(3,11):
    ttl.color(random.choice(colors))
    shapes(i)
    

turtle.done()