import turtle
turtle.bgcolor("lightblue")
turtle.title("Складна фігура: Зірка всередині кола")
turtle.speed(10)
turtle.pensize(2)
turtle.color("darkblue")
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("red")

for i in range(36):
    turtle.forward(200)
    turtle.backward(200)
    turtle.left(10)

turtle.hideturtle()
turtle.done()
