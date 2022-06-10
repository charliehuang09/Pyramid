import turtle
import queue

turtle = turtle.Turtle()


def rectangle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


def get_blocks(input):
    output = 1
    prev_layer = 1
    for i in range(0):
        output = output + prev_layer + 1
        prev_layer = prev_layer + 1
    return output


layers = input()
layers = int(layers) - 1
if layers == -1:
    while True:
        x = 1
queue_x = queue.Queue()
queue_y = queue.Queue()
queue_layer = queue.Queue()
queue_x.put(0)
queue_y.put(0)
queue_layer.put(0)
while(True):
    x = queue_x.get()
    y = queue_y.get()
    layer = queue_layer.get()
    rectangle(x, y)

    if layer < layers:
        queue_x.put(x - 50)
        queue_y.put(y - 50)
        queue_layer.put(layer + 1)

        queue_x.put(x + 50)
        queue_y.put(y - 50)
        queue_layer.put(layer + 1)

while True:
    x = 1