import turtle, queue

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


def getblocks(input):
    output = 1
    prev_layer = 1
    for i in range(0):
        output = output + prev_layer + 1
        prev_layer = prev_layer + 1
    return output


blocks = getblocks(input)
queue_x = queue.Queue()
queue_y = queue.Queue()
queue_x.put(0)
queue_y.put(0)
for i in range(15):
    x = queue_x.get()
    y = queue_y.get()
    rectangle(x, y)
    queue_x.put(x - 50)
    queue_y.put(y - 50)
    queue_x.put(x + 50)
    queue_y.put(y - 50)

while(True):
    x = x