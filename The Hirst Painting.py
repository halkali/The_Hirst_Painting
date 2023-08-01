import turtle

import colorgram
from turtle import Turtle, Screen
from random import randint

inci = Turtle()
turtle.colormode(255)


def color():
    color_palette = []
    colors = colorgram.extract('image.jpg', 20)
    for count in range(len(colors)):
        rgb = colors[count]
        color = rgb.rgb
        color_palette.append(color)
    return color_palette[randint(0,19)]

def main():
    y = -100
    for i in range(0, 10):
        inci.speed("fastest")
        inci.penup()
        inci.goto(-200, y)

        for i in range(0, 10):
            inci.speed("slowest")
            inci.pendown()
            inci.dot(20, (color()))
            inci.penup()
            inci.forward(50)

        y += 50
main()

screen = Screen()
screen.exitonclick()