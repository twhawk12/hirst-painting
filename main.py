# import colorgram
#
# colors = colorgram.extract('SpotPainting04.jpg', 30)
# # first_color = colors[0]
# # rgb = first_color.rgb
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255)


color_list = [(154, 80, 38), (244, 231, 236), (207, 159, 105),
 (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
 (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169),
 (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46),
 (132, 79, 90), (18, 75, 105)]

emma = Turtle()
emma.shape("turtle")
emma.speed("fastest")
emma.penup()
emma.setheading(225)
emma.forward(300)
emma.setheading(0)

number_of_dots = 100


def painting_hirst():
 for dot_count in range(1, number_of_dots + 1):
  emma.dot(20, random.choice(color_list))
  emma.penup()
  emma.forward(50)

  if dot_count % 10 == 0:
   emma.left(90)
   emma.forward(50)
   emma.left(90)
   emma.forward(500)
   emma.right(180)

painting_hirst()
emma.ht()

screen = Screen()
screen.exitonclick()
