# import turtle
#
# turtle.bgcolor("white")
# turtle.pensize(20)
# turtle.speed(8)
#
# for i in range(90):
#     for colours in ["gold", "red", "yellow", "gray"]:
#         turtle.color(colours)
#         turtle.circle(15)
#         turtle.left(20)
#
# turtle.hideturtle()


import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("red")
t.pencolor("blue")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()






# import turtle
#
# turtle.bgcolor("purple")
# turtle.pensize(3)
# turtle.speed(9)
#
# for i in range(6):
#     for colours in ["red", "gray", "blue", "cyan", "green", "yellow", "white"]:
#         turtle.color(colours)
#         turtle.circle(150)
#         turtle.left(20)
#
# turtle.hideturtle()




# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# done = False
#
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#     state = pygame.key.get_pressed()
#     if state[pygame.K_SPACE]:
#         print("spacebar was pressed")
#     if state[pygame.K_q]:
#         done = True
#
# pygame.quit()



# import turtle
#
# turtle.hideturtle()
#
# turtle.pen(pencolor="green", pensize=35)
#
# turtle.begin_fill()
#
# for i in range(19):
#     turtle.forward(158)
#     turtle.right(192)
#     turtle.fillcolor("pink")
#
# turtle.end_fill()
#
# import turtle
#
# colors = ["red", "blue", "green", "gray", "orange", "black"]
# a = turtle.Turtle()
# a.speed(5)
#
# for i in range(130):
#
#     a.color(colors[i % 6])
#
#     if i % 2 == 0:
#         # a.pendown()
#         a.forward(i / 10)
#         a.hideturtle()
#     else:
#         # a.penup()
#         a.forward(5 + i / 10)
#         a.showturtle()
#
#     a.left(40 - i / 1.5)
#
# turtle.exitonclick()


# import turtle
#
# colors = ["red", "blue", "green", "gray", "orange", "black"]
# a = turtle.Turtle()
# a.speed(52)
#
# for i in range(130):
#
#     a.color(colors[i % 6])
#
#     if i % 2 == 0:
#         # a.pendown()
#         a.forward(i / 100)
#         a.hideturtle()
#     else:
#         # a.penup()
#         a.forward(5 + i / 10)
#         a.showturtle()
#
#     a.left(79 - i / 1.5)
#
# turtle.exitonclick()