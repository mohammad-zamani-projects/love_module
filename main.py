import turtle
import math


if __name__ == "__main__":

    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    turtle.bgcolor("black")


    def corazon(num):
        xi = 16 * math.sin(num) ** 3
        yi = 13 * math.cos(num) - 5 * \
            math.cos(2 * num) - 2 * math.cos(3 * num) - \
            math.cos(4 * num)
        return xi, yi


    t.penup()
    for i in range(15):
        t.goto(0, 0)
        t.pendown()
        for n in range(0, 100, 2):
            x, y = corazon(n / 10)
            t.goto(x*i, y*i)
        t.penup()

    t.hideturtle()
    turtle.done()
