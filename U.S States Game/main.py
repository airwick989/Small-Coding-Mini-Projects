import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()

correct = 0
not_guessed = []

while len(states) > 0:
    answer_state = ((screen.textinput(title= f"{correct}/50 States Guessed", prompt= "Name a State!")).title()).strip()

    if answer_state == "Exit":
        break

    if answer_state in states:
        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)

        t.goto(state_x, state_y)
        t.write(state_data.state.item()) #The item() is to get only the raw data, none of that other junk after
        states.remove(answer_state)
        correct += 1

if len(states) > 0:
    for state in states:
        not_guessed.append(state)

states_to_learn = pandas.DataFrame(not_guessed)
states_to_learn.to_csv("states_to_learn.csv")