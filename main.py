from turtle import Turtle, Screen
import random


race_is_on = False
canvas = Screen()
canvas.setup(width=500, height=400)
canvas.title("Turtle race")
user_bet = canvas.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-100 + turtle_index * 40))
#    new_turtle.pendown()
    turtles.append(new_turtle)
if user_bet:
    race_is_on = True
while race_is_on:
    for turtle_index in turtles:
        turtle_index.fd(random.randint(1, 10))
        if turtle_index.xcor() > 230:
            winner = turtle_index.pencolor()
            race_is_on = False
            break

if user_bet == winner:
    print(f"You've won! The winner is {winner}")
else:
    print(f"You've lost! The winner is {winner}")

canvas.exitonclick()
