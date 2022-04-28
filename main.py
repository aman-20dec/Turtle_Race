from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.listen()
screen.setup(width= 600, height=600)


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
race_turtles = []
bet =""

def draw_lines(x_axis, y_axis):
    line_length = 400
    refr = Turtle()
    refr.hideturtle()
    refr.penup()
    refr.setpos(x=x_axis, y= y_axis )
    refr.right(90)
    refr.pendown()
    refr.forward(line_length)

def draw_start_finish_lines():
    draw_lines(-233, 200)
    draw_lines(243, 200)

def generate_turtles():
    gap = 0
    for color in colors:
        name = color +"_turtle"
        name = Turtle("turtle")
        name.color(color)
        name.penup()
        name.speed("slow")
        name.setpos(x=-250, y= -150 + gap)
        gap +=50
        race_turtles.append(name)

def start_race():
    race_continue = True
    while race_continue:
        pick = random.randint(0,6)
        steps = random.randint(1,10)
        race_turtles[pick].forward(steps)
        if race_turtles[pick].xcor() > 250:
            winner = race_turtles[pick].pencolor()
            # message =""
            # if winner == bet:
            #     message = "Your turtle won!!"
            # else:
            #     message = f"You lost. {winner} won the race."
            # print( message)
            race_continue = False

def place_bet():
    return screen.textinput("Place your bet!!", "Which turtle will win the race? Enter your color:")





generate_turtles()

# bet = place_bet()

draw_start_finish_lines()

start_race()


screen.exitonclick()














##############  key listner ##################
# def move_forward():
#     ninja.fd(10)

# def move_backward():
#     ninja.backward(10)

# def counter_clockwise():
#     ninja.left(10)

# def clockwise():
#     ninja.right(10)

# def clear():
#     ninja.reset()

# screen.onkey(fun =move_forward, key = "w")
# screen.onkey(move_backward, key = "s")
# screen.onkey(counter_clockwise, key = "a")
# screen.onkey(clockwise, key = "d")
# screen.onkey(clear, key = "c")

###