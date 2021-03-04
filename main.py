from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race, make your bet!",
                            prompt="Which cowabunga turtle will first hit Shredder? Write your pick:\n(Raphael: (red), Michelangelo: (orange), Donatello: (purple),Leonardo: (blue), April: (yellow) or Vermin: (coral)\n(( Two of those are not actually turtles ))")
colors = ["red", "orange", "purple", "blue", "yellow", "coral"]
turtle_names = ["Raphael", "Michelangelo",
                "Donatello", "Leonardo", "April O' Neil", "Vermin"]

y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

shredder = Turtle(shape='classic')
shredder.penup()
shredder.shapesize(3, 3)
shredder.color('SteelBlue')
shredder.goto(x=240, y=0)

goal_line = Turtle()
goal_line.hideturtle()
goal_line.color('white')
goal_line.pu()
goal_line.goto(x=210, y=-140)
goal_line.setheading(90)
goal_line.pd()
goal_line.forward(260)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 180:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You got it! The {winning_color} turtle was the first one to hit him!")
            else:
                print(
                    f"So close! Sorry! The {winning_color} turtle made the first hit this time!")

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

screen.exitonclick()
