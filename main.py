import random
import turtle as turtle

turtle.colormode(255)
travis = turtle.Turtle()


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    generated_color = (r, g, b)
    return generated_color


travis.pensize(10)
travis.speed("fastest")

for _ in range(200):
    travis.color(generate_color())
    travis.forward(30)
    travis.setheading(random.choice([0, 90, 180, 270]))

screen = turtle.Screen()
screen.exitonclick()
