import colorgram
import turtle as turtle_module
import random

#used to extract colors (color_list)
'''
rgb_colors = []
colors = colorgram.extract('hirst_damien.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(21, 112, 168), (181, 19, 63), (227, 147, 77), (203, 232, 243), (242, 219, 77), (168, 46, 103), (224, 126, 157), (40, 51, 118), (116, 169, 205), (222, 79, 62), (219, 62, 112), (126, 188, 149), (67, 167, 78), (131, 77, 49), (20, 138, 66), (18, 50, 94), (15, 171, 201), (153, 209, 219), (206, 151, 12), (25, 96, 44), (114, 43, 35), (252, 228, 0), (7, 77, 49), (70, 75, 41), (235, 164, 186), (155, 208, 195), (231, 173, 164)]

tim.setheading(210)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()